import os
import time

import docker
import redis

client = docker.from_env()

LB_SYSTEM_EVENT_QUEUE = "lorabridge:events:system"

redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    db=int(os.environ.get("REDIS_DB", 0)),
)

container_anomaly_cnt = {"bridge-lorawan-interface-1": 0}


def update_container_status():
    for container_name in container_anomaly_cnt.keys():
        c = client.containers.get(container_name)
        if c.status != "running":
            container_anomaly_cnt[container_name] += 1
            if container_anomaly_cnt[container_name] > 10:
                redis_client.lpush(LB_SYSTEM_EVENT_QUEUE, "Anomaly: "+container_name)
                container_anomaly_cnt[container_name] = 0


while True:
    update_container_status()
    c = client.containers.get("bridge-lorawan-interface-1")
    # print("Bridge lorawan interface container status: ", c.status)
    if c.status == "exited" and c.attrs["State"]["ExitCode"] != 137:
        try:
            c.start()
            print("container started")
        except docker.errors.APIError as err:
            if (
                err.is_server_error()
                and "error gathering device information while adding custom device" in str(err)
            ):
                print(err)
            else:
                raise err
    time.sleep(0.5)
