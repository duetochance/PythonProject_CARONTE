import configparser
import datReaderClass


# Crea un oggetto ConfigParser
connOracle = datReaderClass.DatReader('OracleDat.dat')

 
# Carica il file di configurazione 
# Leggi i valori dalla sezione "OracleSettings"
driver = connOracle.get_driver()
database_name = connOracle.get_dbName()
sid = connOracle.get_sid()
serverName = connOracle.get_server()
userName = connOracle.get_user()
password = connOracle.get_password()

# Stampa i valori letti
print(f"DRIVER: {driver}")
print(f"DATABASE NAME: {database_name}")
print(f"SID: {sid}")
print(f"SERVER NAME: {serverName}")
print(f"USER NAME: {userName}")
print(f"PASSWORD: {password}")



print(f"Password: {connOracle.get_password()}")