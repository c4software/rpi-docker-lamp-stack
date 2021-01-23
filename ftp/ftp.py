import os
import sys
import logging

from pyftpdlib.authorizers import (DummyAuthorizer,AuthenticationFailed)
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

BANNER = os.environ.get("BANNER", "Basic FTP")
MAX_CONNS = os.environ.get("MAX_CONNS", 100)
MAX_CONNS_PER_IP = os.environ.get("MAX_CONNS_PER_IP", 5)
PASV_PORT_START = os.environ.get("PASV_PORT_START", 5000)
PASV_PORT_END = os.environ.get("PASV_PORT_END", 5100)

class WebHookAuthorizer(DummyAuthorizer):
    def validate_authentication(self, username, password, handler):
        if username != password:
            raise AuthenticationFailed

    def has_user(self, username):
        return True

    def has_perm(self, username, perm, path=None):
        return perm in ("l", "w", "e")

    def get_msg_login(self, username):
        return "Welcome"

    def get_msg_quit(self, username):
        return "Bye"

    def get_perms(self, username):
        return "elw"

    def get_home_dir(self, username):
        directories = ["/ftp/{}/".format(username), "/ftp/{}/public_html/".format(username)]
        for directory in directories:
            if not os.path.exists(directory):
                print ("Creating directory: {}".format(directory))
                os.makedirs(directory)
        return directories[0]


def main(port):
    authorizer = WebHookAuthorizer()
    
    handler = FTPHandler
    handler.permit_foreign_addresses = True   
    handler.authorizer = authorizer
    handler.banner = BANNER
    handler.passive_ports = range(int(PASV_PORT_START), int(PASV_PORT_END))
    server = FTPServer(("0.0.0.0", port), handler)
    server.max_cons = int(MAX_CONNS)
    server.max_cons_per_ip = int(MAX_CONNS_PER_IP)
    server.serve_forever()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No port specified")
        exit(-1)
    main(sys.argv[1])
