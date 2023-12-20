import oracledb as oraDB
import datReaderClass

connOracle = datReaderClass.DatReader('OracleDat.dat')

 
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

except:  
    print("Error Message: Connessione fallita.")
    exit()


# query
query ="INSERT INTO TABOCAMPIONI (CODICECAMPIONE, IDCAMPIONE) VALUES (:codice, :id)"
codice_campione ='23XX00003'
id_campione ='TEST'

# Creare un cursore
try:
    cursor = connection.cursor()
 
# Eseguire una query di esempio
    cursor.execute(query, codice=codice_campione,id=id_campione)
    connection.commit()
    print("Inserimento riuscito")

except oraDB.IntegrityError as e:    
    error_obj, = e.args 
    print("Error query:", query)    
    print("Error Full Code:", error_obj.full_code)    
    print("Error Message:", error_obj.message)

finally:
    
    cursor.execute("SELECT * FROM taboanalisi")
    for row in cursor:
        print(row)
    
    cursor.close()
    connection.close()

 