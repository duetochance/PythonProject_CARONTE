import oracledb as oraDB
import json
 
# Resto del tuo codice...
 
# Eseguire una query di esempio
def tableExportJson (table, conn):
    cursor = conn.cursor
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
 
# Recuperare i risultati
    results = []
    for row in cursor:
        results.append(row)
 
# Chiudere il cursore e la connessione
    cursor.close()
 
# Creare il file JSON e salvare i risultati
    with open(f'{table}.json', 'w') as file:
        json.dump(results, file, indent=4)
 
    print(f"Dati della tabella salvati in formato JSON nel file '{table}.json'.")