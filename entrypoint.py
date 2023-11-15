import os
import socket
import logging
from typing import Optional

import backoff


@backoff.on_exception(
    backoff.expo, ConnectionRefusedError, max_time=int(os.environ.get("INPUT_MAXTIME", "60"))
)
def netcat(host: str, port: int, content: Optional[str] = None) -> None:
    """
    Establish a TCP connection to the specified host and port.
    
    Args:
        host: The target hostname or IP address
        port: The target port number
        content: Optional content to send after connection
    """
    BUFFER_SIZE = 4096
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        if content:
            s.sendall(content.encode())
        s.shutdown(socket.SHUT_WR)
        
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            print(repr(data))
    finally:
        s.close()


def validate_inputs(host: str, port: str) -> tuple[str, int]:
    """
    Validate and convert input parameters.
    
    Args:
        host: The hostname or IP address
        port: The port number as string
        
    Returns:
        Tuple of (host, port) with validated values
        
    Raises:
        ValueError: If inputs are invalid
    """
    if not host or not host.strip():
        raise ValueError("Host cannot be empty")
    
    try:
        port_num = int(port)
        if not (1 <= port_num <= 65535):
            raise ValueError("Port must be between 1 and 65535")
    except ValueError as e:
        raise ValueError(f"Invalid port number: {port}") from e
    
    return host.strip(), port_num


def main() -> None:
    """Main function to handle TCP connection test."""
    logging.getLogger("backoff").addHandler(logging.StreamHandler())
    
    try:
        my_host = os.environ["INPUT_REMOTEHOST"]
        my_port = os.environ["INPUT_REMOTEPORT"]
        
        # Validate inputs
        host, port = validate_inputs(my_host, my_port)
        
        # Attempt connection
        netcat(host, port)
        
        # Use new GitHub Actions output syntax
        output_message = "Connection successful!"
        print(f"myOutput={output_message}")
        
    except TimeoutError:
        error_msg = "Timed out waiting for connection"
        print(f"error={error_msg}")
        raise Exception(error_msg)
    except ValueError as e:
        error_msg = f"Invalid input: {str(e)}"
        print(f"error={error_msg}")
        raise Exception(error_msg)
    except Exception as e:
        error_msg = f"Connection failed: {str(e)}"
        print(f"error={error_msg}")
        raise


if __name__ == "__main__":
    main()
