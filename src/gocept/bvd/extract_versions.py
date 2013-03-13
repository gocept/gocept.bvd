import sys
import os
import socket
import json


def main():
    versions = {}

    deployment_hash = '{}:{}'.format(socket.getfqdn(), os.getcwd())

    for line in sys.stdin:
        line = line.rstrip()
        if line == '[versions]':
            break

    for line in sys.stdin:
        line = line.rstrip()
        if line.startswith(' '):
            continue
        if line == '':
            break
        package, version = line.split('=',1)
        versions[package.strip()] = version.strip()

    print json.dumps({deployment_hash: versions})
