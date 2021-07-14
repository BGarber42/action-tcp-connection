import socket

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
    my_host = os.environ["INPUT_REMOTEHOST"]
    my_port = os.environ["INPUT_REMOTEPORT"]

    netcat(my_host, my_port)

    my_output = "Yay!"
    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
