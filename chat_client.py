from socket import socket, AF_INET, SOCK_STREAM
import pickle
import time
from sys import argv, exit
import logging
import log.client_log_config

logger = logging.getLogger('client')

def log(func):
    def deco(*args, **kwargs):
        r = func(*args, **kwargs)
        logger.info(f'{func.__name__} running')        
        return r
    return deco

@log
def send_msg(socket, msg_type):    
    socket.send(pickle.dumps(msg_type))

@log
def rcv_msg(socket):    
    server_data = socket.recv(640)
    return pickle.loads(server_data)

def main():
    try:
        addr = argv[1]
    except IndexError:
        logger.error("attempt to start without specifying the server")
        exit('Необходимо указать IP-адрес сервера')
    port = int(argv[2]) if len(argv) > 2 else 7777

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((addr, port))

    presence = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
        }
    }
    send_msg(s, presence)

    server_msg = rcv_msg(s)
    if server_msg['response']:
        logger.info("%(alert)s with code %(response)s", server_msg)

    s.close()

            
if __name__ == '__main__':

    main()