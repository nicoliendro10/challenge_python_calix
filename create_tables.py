from src.sql_service import SQLService

sql_service = SQLService()
sql_service.config_credentials()
sql_script = open('create_table.sql', 'r').read()
sql_service.execute_sql_script(sql_script)