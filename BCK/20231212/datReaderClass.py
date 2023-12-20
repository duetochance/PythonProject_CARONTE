import configparser
 
class DatReader:
    def __init__(self, file_path='OracleDat.dat'):
        # Inizializza il parser di configurazione
        self.config = configparser.ConfigParser()
        # Carica il file di configurazione
        self.config.read(file_path)
 
    def get_password(self):
        # Restituisci la password dal file di configurazione
        try:
            return self.config.get('OracleSettings', 'PASSWORD')
        except:
            print("Errore di lettura: PASSWORD")
            return ''
    def get_server(self):
        # Restituisci la password dal file di configurazione
        return self.config.get('OracleSettings', 'SERVER_NAME')
    def get_user(self):
        # Restituisci la password dal file di configurazione
        return self.config.get('OracleSettings', 'USER_NAME')
    def get_sid(self):
        # Restituisci la password dal file di configurazione
        return self.config.get('OracleSettings', 'SID')
    def get_dbName(self):
        # Restituisci la password dal file di configurazione
        return self.config.get('OracleSettings', 'DATABASE_NAME')
    def get_driver(self):
        # Restituisci la password dal file di configurazione
        return self.config.get('OracleSettings', 'DRIVER')
    def get_port(self):
        # Restituisci la password dal file di configurazione
        return self.config.get('OracleSettings', 'PORT')
    
 
# Esempio di utilizzo
# if __name__ == "__main__":
#     # Crea un'istanza della classe DatReader
#     dat_reader = DatReader()
 
    # Utilizza il metodo get_password per ottenere la password
    # password = dat_reader.get_password()
 
    # # Stampa la password
    # print(f"Password: {password}")