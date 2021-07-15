import os
import socket
import logging

import backoff


@backoff.on_exception(
    backoff.expo, ConnectionRefusedError, max_time=os.environ.get("INPUT_MAXTIME", 60)
)
def netcat(host, port, content=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    if content:
        s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(repr(data))
    s.close()


def main():
    logging.getLogger("backoff").addHandler(logging.StreamHandler())
    my_host = os.environ["INPUT_REMOTEHOST"]
    my_port = os.environ["INPUT_REMOTEPORT"]

    try:
        netcat(my_host, my_port)
    except TimeoutError:
        print("Timed out waiting for connection")
        raise Exception("Timed out waiting for connection")

    my_output = "Yay!"
    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
