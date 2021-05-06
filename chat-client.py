'''Практическое задание

Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
    клиент отправляет запрос серверу;
    сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.

Функции клиента:
    сформировать presence-сообщение;
    отправить сообщение серверу;
    получить ответ сервера;
    разобрать сообщение сервера;
    параметры командной строки скрипта client.py <addr> [<port>]:
        addr — ip-адрес сервера;
        port — tcp-порт на сервере, по умолчанию 7777.'''

from socket import socket, AF_INET, SOCK_STREAM
import pickle
import time
from sys import argv, exit

if len(argv) < 2:
	exit('Необходимо указать IP-адрес сервера')
addr = argv[1]
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
	print(f'{server_msg["alert"]} at {time.strftime("%H:%M:%S", time.localtime(server_msg["time"]))} with code {server_msg["response"]}')

s.close()
