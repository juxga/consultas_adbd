import psycopg2

# Ignore pandas warning for using directly psycopg2 instead of sqlalchemy
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning)

import pandas as pd

# DB login (very insecure)
host = "localhost"
database = "bdepython"
user = "usuariopython"
password = "clavepython"

# DB utilities
def query(text):
    
    """
    Execute a query to the postgreSQL DB and
    convert it to a pandas dataframe.
    
    Parameters
    ----------
    cons: str
        The query
        
    """
    conn = psycopg2.connect(host=host,database=database,user=user,password=password)
    cur = conn.cursor()
    dat = pd.io.sql.read_sql_query(text,conn)
    cur.close()
    conn.close()
    return dat

def build(script_path):
    
    """
    Builds the database from the sql script.
    
    Warning
    -------
        Or whatever the script does.
    """
    
    with open(script_path,"r") as file:
        script = file.read()
    
    conn = psycopg2.connect(host=host,database=database,user=user,password=password)
    cur = conn.cursor()
    
    cur.execute(script)
    conn.commit()
    
    cur.close()
    conn.close()
