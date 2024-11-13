import docker
import time

client = docker.from_env()
while True:
    c = client.containers.get("bridge-lorawan-interface-1")
    if c.status == "exited" and c.attrs["State"]["ExitCode"] != 137:
        c.start()
        print("container started")
    time.sleep(2)
