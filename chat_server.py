'''Практическое задание

Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
    клиент отправляет запрос серверу;
    сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.

Функции сервера:
    принимает сообщение клиента;
    формирует ответ клиенту;
    отправляет ответ клиенту;
    имеет параметры командной строки:
        -p <port> — TCP-порт для работы (по умолчанию использует 7777);
        -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).'''

from socket import socket, AF_INET, SOCK_STREAM
import time
import pickle
from sys import argv
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=7777)
    parser.add_argument('-a', '--address', default='')
    return parser


if __name__ == '__main__':
        
    parser = create_parser()
    arg = parser.parse_args(argv[1:])

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((arg.address, int(arg.port)))
    s.listen(5)

    while True:
        client, addr = s.accept()
        data = pickle.loads(client.recv(640))
        if data['action'] == 'presence':
            print(f'presence message received from client {addr[0]} at {time.strftime("%H:%M:%S", time.localtime(data["time"]))}')
            response = {
                "response": 202,
                "time": time.time(),
                "alert": "chat-server confirm connection"
            }
            client.send(pickle.dumps(response))

        client.close()
