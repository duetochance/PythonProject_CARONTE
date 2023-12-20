import oracledb as oraDB
import json
from datetime import datetime
import pandas as pd
import subprocess
 
# Resto del tuo codice...
 
# Eseguire una query di esempio
def tableExportJson (table, conn):
    cursor = conn.cursor()
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
 
    results = pandas.DataFrame (cursor.fetchall())
# Recuperare i risultati
    # results = []
    # for row in cursor:
    #     results.append(row)
 
# Chiudere il cursore e la connessione
    cursor.close()
 
# Creare il file JSON e salvare i risultati
    data = datetime.now().strftime("%Y%m%d")
    resultsJSON = results.to_json (f'JSON\{data}_{table}.json')
    print (results)

   
def output_type_handler(cursor, name, default_type, size, precision, scale):
    if default_type == oraDB.DB_TYPE_CLOB:
        return cursor.var(oraDB.DB_TYPE_LONG, arraysize=cursor.arraysize)
    if default_type == oraDB.DB_TYPE_BLOB:
        return cursor.var(oraDB.DB_TYPE_LONG_RAW, arraysize=cursor.arraysize)
 
def _debug_json(table:str, conn:oraDB.Connection):
    conn.outputtypehandler = output_type_handler
    cursor = conn.cursor()
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    #results=pandas.read_sql(query,con=conn)
    lobResults=cursor.fetchall()
    #print(lobResults[4][3])
    # Get column names from the cursor description
    columns = [col[0] for col in cursor.description]

    # Create a DataFrame using the fetched results and column names
    df = pd.DataFrame(lobResults, columns=columns)
    data = datetime.now().strftime("%Y%m%d")
    
    df.to_json (f'JSON\{data}_{table}.json',orient='records',indent=True)
    ##subprocess.Popen(r'explorer /select,"\\srvopenco\Open-Co\Personali\03 - Temporanea\Samuele\PythonProject\JSON\"')
    
    cursor.close()

#main "fittizio" per testare direttamente da qui le funzioni    
if __name__=='__main__':
    import ConnORC_DB
    import expJ

    connection = ConnORC_DB.openDbConnection('OracleDat.dat')
    expJ._debug_json('TABCLSCRIPT',connection)
    #expJ._debug_json('TABCCAMPIONI',connection)
    
    ConnORC_DB.closeDbConnection(connection)