from socket import socket, AF_INET, SOCK_STREAM
import time
import pickle
from sys import argv
from argparse import ArgumentParser
import logging
import log.server_log_config

logger = logging.getLogger('server_app')

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=7777)
    parser.add_argument('-a', '--address', default='')
    logger.info('function "create_parser()" executed')
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
            logger.info('presence message received from client %s', addr[0])
            response = {
                "response": 202,
                "time": time.time(),
                "alert": "chat-server confirm connection"
            }
            client.send(pickle.dumps(response))

        client.close()
