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

def new_listen_socket(sock_parms):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((sock_parms.address, int(sock_parms.port)))
    sock.listen(5)
    return sock


def main():
    parser = create_parser()
    arg = parser.parse_args(argv[1:])

    s = new_listen_socket(arg)

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


if __name__ == '__main__':

    main()
        

