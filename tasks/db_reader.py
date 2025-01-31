import os
from loguru import logger

from pymssql import connect


class DBReader:
    def __init__(self):
        self.type = os.getenv('NDW_TYPE')
        self.host = os.getenv('NDW_HOST')
        self.port = os.getenv('NDW_PORT')
        self.user = os.getenv('NDW_USER')
        self.password = os.getenv('NDW_PASS')
        self.database = os.getenv('NDW_DB')

    def get_connection(self):
        try:
            logger.info(f'Connecting to {self.host}...')
            cn = connect(
                server=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                as_dict=True
            )
            logger.info(f'Connected to {self.host}')
            return cn.cursor()
        except Exception as e:
            logger.error(e)
            raise

    def get_data(self, sql: str):
        cn = self.get_connection()
        cn.execute(sql)
        return cn.fetchall()

    def get_schema(self,tableName:str):
        sql = (f"SELECT "
               f"   COLUMN_NAME,DATA_TYPE,IS_NULLABLE "
               f"FROM "
               f"   INFORMATION_SCHEMA.COLUMNS "
               f"WHERE "
               f"   TABLE_NAME = '{tableName}' "
               f"ORDER BY "
               f"   ORDINAL_POSITION;")
        return self.get_data(sql)

