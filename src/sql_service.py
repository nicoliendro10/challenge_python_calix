import pandas as pd
from sqlalchemy import create_engine
from decouple import config


class SQLService:
    def __init__(self):
        
        self.conn_string = ''
        self.engine = None

    def create_table(self, table_name, df):
        """ Create a table in the database using the dataframe and the table name """
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def execute_sql_script(self, script):
        """ Execute the sql script """
        self.engine.execute(script)

    def config_credentials(self):
        """ Configure the credentials to connect to the database from a .env file"""
        USER = config('USER', default='postgres')
        PASSWORD = config('PASSWORD')
        HOSTNAME = config('HOSTNAME', default='localhost')
        PORT = config('PORT', default=5432)
        DB_NAME = config('DB_NAME')
        db_string = "postgresql://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB_NAME}".format(
            USER=USER, PASSWORD=PASSWORD, HOSTNAME=HOSTNAME, PORT=PORT, DB_NAME=DB_NAME)
        self.conn_string = db_string
        self.engine = create_engine(self.conn_string)
