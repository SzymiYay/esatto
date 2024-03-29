from .crud import CrudRepo
from ..model.address import Address


class AddressRepo(CrudRepo):
    def __init__(self, connection_pool):
        super().__init__(connection_pool, Address)