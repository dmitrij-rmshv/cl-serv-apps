from socket import socket, AF_INET, SOCK_STREAM
import pickle
import time
from sys import argv, exit

def send_msg(socket, msg_type):    
    socket.send(pickle.dumps(msg_type))

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
        print(f'{server_msg["alert"]} at {time.strftime("%H:%M:%S", time.localtime(server_msg["time"]))} with code {server_msg["response"]}')


    s.close()

            
if __name__ == '__main__':

    main()