import docker
import time

client = docker.from_env()
while True:
    c = client.containers.get("bridge-lorawan-interface-1")
    if c.status == "exited" and c.attrs["State"]["ExitCode"] != 137:
        try:
            c.start()
            print("container started")
        except docker.errors.APIError as err:
            if (
                err.is_server_error()
                and "error gathering device information while adding custom device"
                in str(err)
            ):
                print(err)
            else:
                raise err
    time.sleep(2)
