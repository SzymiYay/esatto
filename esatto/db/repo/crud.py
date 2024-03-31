from mysql.connector import Error, pooling
from typing import Any
from datetime import date, datetime
from contextlib import contextmanager

import inflection
import logging
import functools

logging.basicConfig(level=logging.INFO)


class CrudRepo:

    def __init__(self, connection_pool, entity):
        self._connection_pool = connection_pool
        self._entity = entity
        self._entity_type = type(entity())

    @contextmanager
    def _get_connection(self):
        try:
            connection = self._connection_pool.get_connection()
            if connection.is_connected():
                cursor = connection.cursor()
                yield cursor
                connection.commit()
        except Error as err:
            logging.error(err)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def create_table(self, columns: dict[str, str]):
        with self._get_connection() as cursor:
            column_definitions = ', '.join(f'{name} {type}' for name, type in columns.items())
            query = f"CREATE TABLE IF NOT EXISTS {self._table_name()} ({column_definitions});"
            cursor.execute(query)


    def insert(self, item: Any) -> int:
        with self._get_connection() as cursor:
            query = f"""
                        INSERT INTO {self._table_name()}
                        ({self._column_names_for_insert()})
                        VALUES ({self._column_values_for_insert(item)});
                     """
            cursor.execute(query)

            return cursor.lastrowid


    def insert_many(self, items: list[Any]) -> list[Any]:
        with self._get_connection() as cursor:
            values = ', '.join([f"({CrudRepo._column_values_for_insert(item)})" for item in items])
            query = f"""
                        INSERT INTO {self._table_name()}
                        ({self._column_names_for_insert()}) VALUES {values};
                     """
            cursor.execute(query)

            return [item.id for item in self.get_n_last(len(items))]


    def update(self, item_id: int, item: Any) -> list[int]:
        with self._get_connection() as cursor:
            query = f"""
                        UPDATE {self._table_name()}
                        SET {CrudRepo._column_names_and_values_for_update(item)}
                        WHERE id = {item_id};
                     """
            cursor.execute(query)

            return self.get_one(item_id)


    def get_one(self, item_id: int) -> Any:
        with self._get_connection() as cursor:
            query = f"""
                        SELECT * FROM {self._table_name()}
                        WHERE id = {item_id};
                     """
            cursor.execute(query)

            result = cursor.fetchone()
            if result is None:
                raise RuntimeError('Not found')

            return self._entity(*result)


    def get_n_last(self, n: int) -> list[Any]:
        with self._get_connection() as cursor:
            query = f"""
                        SELECT * FROM {self._table_name()}
                        ORDER BY id DESC
                        LIMIT {n};
                     """
            cursor.execute(query)

            return [self._entity(*row) for row in cursor.fetchall()]

    def get_columns_with_condition(self, columns: list[str] = None, condition: str = None):
        with self._get_connection() as cursor:
            columns = ', '.join(columns) if columns else '*'
            query = f'SELECT {columns} FROM {self._table_name()}'

            if condition:
                query += f' WHERE {condition};'

            cursor.execute(query)

            return cursor.fetchall()


    def get_all(self) -> list[Any]:
        with self._get_connection() as cursor:
            query = f'SELECT * FROM {self._table_name()};'
            cursor.execute(query)

            return [self._entity(*row) for row in cursor.fetchall()]


    def delete_one(self, item_id: int) -> int:
        with self._get_connection() as cursor:
            query = f"""
                        DELETE FROM {self._table_name()}
                        WHERE id = {item_id}
                     """
            cursor.execute(query)

            return item_id


    def delete_all(self) -> list[int]:
        with self._get_connection() as cursor:
            all_deleted_ids = [item.id for item in self.get_all()]
            query = f"""
                        DELETE FROM {self._table_name()}
                        WHERE id >= 0
                     """
            cursor.execute(query)

            return all_deleted_ids


    def _table_name(self) -> str:
        return inflection.tableize(self._entity_type.__name__)

    def _field_names(self) -> list[str]:
        return self._entity().__dict__.keys()

    def _column_names_for_insert(self):
        fields = [field for field in self._field_names() if field.lower() != 'id']
        return ', '.join(fields)

    @classmethod
    def _column_values_for_insert(cls, item: Any) -> str:

        def to_str(entry: Any) -> str:
            return f"'{entry[1]}'" if isinstance(entry[1], (str, datetime, date)) else str(entry[1])

        return ", ".join([to_str(entry) for entry in item.__dict__.items() if entry[0].lower() != 'id'])

    @classmethod
    def _column_names_and_values_for_update(cls, entity) -> str:

        def to_str(entry: Any) -> str:
            return entry[0] + '=' + (f"'{entry[1]}'" if isinstance(entry[1], (str, datetime, date)) else str(entry[1]))

        return ', '.join([to_str(item) for item in entity.__dict__.items() if item[0].lower() != 'id'])