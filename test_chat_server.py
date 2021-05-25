from socket import socket, AF_INET, SOCK_STREAM
import argparse
import pytest
from sys import argv
from chat_server import create_parser, new_listen_socket

def test_create_parser():
    parser = argparse.ArgumentParser()
    assert type(create_parser()) == type(parser)

def test_parser_a_args():
    assert str(create_parser().parse_args(argv[1:])) == "Namespace(address='', port=7777)"

def test_new_socket():
    test_socket = socket(AF_INET, SOCK_STREAM)
    parser = create_parser()
    assert type(new_listen_socket(parser.parse_args(argv[1:]))) == type(test_socket)
