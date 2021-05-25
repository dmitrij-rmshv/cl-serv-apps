from socket import socket, AF_INET, SOCK_STREAM
import argparse
import pytest
from sys import argv
from chat_client import send_msg, rcv_msg
import pickle

def test_send_msg():
    sock_srv = socket(AF_INET, SOCK_STREAM)
    sock_srv.bind(("localhost", 5678))
    sock_srv.listen(5)

    sock_cli = socket(AF_INET, SOCK_STREAM)
    sock_cli.connect(("localhost", 5678))
    data_cli = {'some_parm': 'some_value'}
    send_msg(sock_cli, data_cli)

    client, addr = sock_srv.accept()

    data_ser = pickle.loads(client.recv(640))
    assert data_ser == data_cli
    client.close()
    sock_cli.close()

def test_rcv_msg():
    sock_srv = socket(AF_INET, SOCK_STREAM)
    sock_srv.bind(("localhost", 6789))
    sock_srv.listen(5)
    data_ser = {'some_parm': 'some_value'}

    sock_cli = socket(AF_INET, SOCK_STREAM)
    sock_cli.connect(("localhost", 6789))

    client, addr = sock_srv.accept()
    client.send(pickle.dumps(data_ser))

    assert rcv_msg(sock_cli) == data_ser
    
    client.close()
    sock_cli.close()
