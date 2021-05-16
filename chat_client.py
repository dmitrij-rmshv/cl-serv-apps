from socket import socket, AF_INET, SOCK_STREAM
import pickle
import time
from sys import argv, exit
import logging
import log.client_log_config

log = logging.getLogger('client')

try:
    addr = argv[1]
except IndexError:
    log.error("attempt to start without specifying the server")
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
s.send(pickle.dumps(presence))

server_data = s.recv(640)
server_msg = pickle.loads(server_data)
if server_msg['response']:
    log.info("%(alert)s with code %(response)s", server_msg)

s.close()
