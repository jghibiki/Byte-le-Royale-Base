
import sys

from game.server.broadcast_server import start_server
from game.server.custom_server import CustomServer


def start(verbose=False, port=9000, no_wait=False):
    server_logic = CustomServer(verbose=verbose, wait_on_client=not no_wait)
    start_server("0.0.0.0", str(port), server_logic, verbose=verbose)
