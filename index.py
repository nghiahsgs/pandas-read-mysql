from sqlalchemy import create_engine
import pymysql
import pandas as pd

# db_connection_str = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
db_connection_str = 'mysql+pymysql://root:@localhost/bds_com_1'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM product', con=db_connection)
