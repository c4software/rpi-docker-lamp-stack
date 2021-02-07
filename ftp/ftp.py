import os
import sys
import logging
import json

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
PASSWORD_PREFIX = os.environ.get("PASSWORD_PREFIX", "")
PASSWORD_SUFFIX = os.environ.get("PASSWORD_SUFFIX", "")
DISALLOWED_USERNAME = ["root", "admin", "administrator"]

class Authorizer(DummyAuthorizer):
    def validate_authentication(self, username, password, handler):
        if not self.validate_user(username.lower(), password):
            raise AuthenticationFailed

    def has_user(self, username):
        return True

    def has_perm(self, username, perm, path=None):
        return True

    def get_msg_login(self, username):
        return "Welcome {}".format(username)

    def get_msg_quit(self, username):
        return "Bye"

    def get_perms(self, username):
        return "elwadfmwMT"

    def get_home_dir(self, username):
        # Create folder according the current username
        folder_name = os.path.basename(username.lower())
        directories = ["/ftp/{}/".format(folder_name), "/ftp/{}/public_html/".format(folder_name)]
        for directory in directories:
            if not os.path.exists(directory):
                logging.info("Creating directory: {}".format(directory))
                os.makedirs(directory)

        return directories[0]

    def validate_user(self, username, password):
        try:
            with open('users.json', 'r') as json_file:
                users = json.load(json_file)
                if users and username in users:
                    return users[username] == password
                elif not users:
                    return self.validate_generated_user(username, password)
                else:
                    return False
        except:
            return self.validate_generated_user(username, password)

    def validate_generated_user(self, username, password):
        return username.lower() not in DISALLOWED_USERNAME and password == "{}{}{}".format(PASSWORD_PREFIX, username.lower(), PASSWORD_SUFFIX)


def main(port):
    authorizer = Authorizer()
    
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
        logging.error("No port specified")
        exit(-1)
    main(sys.argv[1])
