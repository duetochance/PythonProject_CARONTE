import oracledb as oraDB
import json
from datetime import datetime
import pandas 
 
# Resto del tuo codice...
def output_type_handler(cursor, name, default_type, size, precision, scale):
    if default_type == oraDB.DB_TYPE_CLOB:
        return cursor.var(oraDB.DB_TYPE_LONG, arraysize=cursor.arraysize)
    if default_type == oraDB.DB_TYPE_BLOB:
        return cursor.var(oraDB.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)
    
# Eseguire una query di esempio
def tableExportJson (table, conn):
    conn.outputtypehandler = output_type_handler
    
    cursor = conn.cursor()
    
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    
    lobResults=cursor.fetchall()

    # Get column names from the cursor description
    columns = [col[0] for col in cursor.description]

    # Create a DataFrame using the fetched results and column names
    results = pandas.DataFrame(lobResults, columns=columns)

    data = datetime.now().strftime("%Y%m%d")
    resultsJSON = results.to_json (f'JSON\{data}_{table}.json',orient="records",indent=True)
    print (f'creato file: JSON\{data}_{table}.json')
    
# Eseguire una query di esempio
def confTableExportJson (table, conn):
    conn.outputtypehandler = output_type_handler
    print(f"Configurazione tabella {table}")
    cursor = conn.cursor()
    
    query = f"SELECT COLUMN_NAME, DATA_TYPE, DATA_LENGTH, DATA_PRECISION, DATA_SCALE, NULLABLE FROM USER_TAB_COLUMNS WHERE TABLE_NAME = '{table}'"
    cursor.execute(query)
    
    lobResults=cursor.fetchall()

    # Get column names from the cursor description
    columns = [col[0] for col in cursor.description]

    # Create a DataFrame using the fetched results and column names
    results = pandas.DataFrame(lobResults, columns=columns)
    print(results)
    data = datetime.now().strftime("%Y%m%d")
    resultsJSON = results.to_json (f'JSON\{data}_CONF_{table}.json',orient="records",indent=True)
    print (f'creato file: JSON\{data}_{table}.json')
