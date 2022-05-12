import mysql.connector as connection
import pandas as pd


class DBRead:
    def __init__(self, host: str, username: str, password: str):
        self.host = host
        self.username = username
        self.password = password
        self.db_connection = None

    def connect(self):
        try:
            self.db_connection = connection.connect(host=self.host,
                                                    username=self.username,
                                                    password=self.password)
        except Exception as conn_exception:
            print(f'ERROR: {conn_exception}')
        else:
            print('DB connection successful')

    def get_query_result(self, query):
        self.connect()
        conn_close_msg = ''
        query_result_msg = ''
        result_df = ''
        if self.db_connection is not None:
            try:
                result_df = pd.read_sql(query, self.db_connection)
            except Exception as e:
                print(f'ERROR: {e}')

            self.db_connection.close()
            conn_close_msg = 'DB connection closed'
            self.db_connection = None
        else:
            conn_close_msg = 'DB connection unavailable'

        query_result_msg = f'Query returned {len(result_df)} rows'
        print(conn_close_msg)
        print(query_result_msg)
        return result_df
