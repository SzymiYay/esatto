from mysql.connector.pooling import MySQLConnectionPool
from dotenv import load_dotenv
from typing import Self

import os

load_dotenv()


class MySQLConnectionPoolBuilder:
    def __init__(self):
        self._pool_config = {
            'pool_name': os.getenv('POOL_NAME'),
            'pool_size': int(os.getenv('POOL_SIZE')),
            'pool_reset_session': bool(os.getenv('POOL_RESET_SESSION')),
            'host': os.getenv('HOST'),
            'database': os.getenv('DATABASE'),
            'user': os.getenv('USER'),
            'password': os.getenv('PASSWORD'),
            'port': int(os.getenv('PORT'))
        }

    def set_pool_name(self, new_name: str) -> Self:
        self._pool_config['pool_name'] = new_name
        return self

    def set_pool_size(self, new_size: int) -> Self:
        self._pool_config['pool_size'] = new_size
        return self

    def set_reset_session(self, do_reset: bool) -> Self:
        self._pool_config['pool_reset_session'] = do_reset
        return self

    def set_host(self, new_host: str) -> Self:
        self._pool_config['host'] = new_host
        return self

    def set_database(self, new_database: str) -> Self:
        self._pool_config['database'] = new_database
        return self

    def set_user(self, new_user: str) -> Self:
        self._pool_config['user'] = new_user
        return self

    def set_password(self, new_password: str) -> Self:
        self._pool_config['password'] = new_password
        return self

    def set_port(self, new_port: int) -> Self:
        self._pool_config['port'] = new_port
        return self

    def build(self) -> MySQLConnectionPool:
        print(self._pool_config)
        return MySQLConnectionPool(**self._pool_config)