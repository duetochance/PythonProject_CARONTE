import oracledb as oraDB
import datReaderClass


def openDbConnection (dat):
    connOracle = datReaderClass.DatReader(dat)

    # Impostare le credenziali di connessione
    driver = connOracle.get_driver()
    database_name = connOracle.get_dbName()
    sid = connOracle.get_sid()
    serverName = connOracle.get_server()
    userName = connOracle.get_user()
    password = connOracle.get_password()
    port = connOracle.get_port()

    try:
    # Creare una stringa di connessione
        dsn_tns = oraDB.makedsn(serverName,port,sid)
        conn_str = f"{userName}/{password}@{dsn_tns}"
    # Connessione al database
        connection = oraDB.connect(conn_str)
        print(f"Connessione riuscita al database: {database_name}.")
        return connection
    except:  
        print("Error Message: Connessione fallita.")
        exit()

def closeDbConnection (connection):
    print(f"Connessione {connection.dsn} terminata")
    connection.close()
