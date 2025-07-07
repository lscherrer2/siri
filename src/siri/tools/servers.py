from abc import ABC, abstractmethod

__all__ = ["Server", "SERVERS", "register_servers"]

class Server(ABC):
    name: str
    @abstractmethod
    def query (self):
        pass

SERVERS: dict[str, Server] = {} 

def register_servers (servers: list[Server]):
    global SERVERS
    SERVERS = {server.name: server for server in servers}


