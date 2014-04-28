# coding: utf-8

import socket
import cPickle


class RPCServer(object):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 5448))
        self.socket.listen(1)
        self.procedures = {}

    def register(self, func):
        self.procedures[func.func_name] = func

    def unregister(self, name):
        del self.procedures[name]   # don't suppress error

    def serve_forever(self):
        while True:
            conn, addr = self.socket.accept()
            data = cPickle.loads(conn.recv(4096))

            if data['func'] in self.procedures:
                func_name = data['func']
                args = data['args']
                kwargs = data['kwargs']

                try:
                    result = self.procedures[func_name](*args, **kwargs)
                    conn.sendall(cPickle.dumps(result))
                except TypeError:
                    conn.sendall(cPickle.dumps('Incorrect arguments'))

            else:
                conn.sendall(cPickle.dumps('Procedure do not found'))

        self.socket.close()


class RPCClient(object):

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            data = {
                'func': name,
                'args': args,
                'kwargs': kwargs,
            }
            data = cPickle.dumps(data)

            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(('localhost', 5448))
            self.socket.sendall(data)
            result = cPickle.loads(self.socket.recv(4096)) # <<< c.some_call("hello" * 10000)
            self.socket.close()

            return result

        return wrapper
