import ConnORC_DB
import expJ


print('1 --------------------------\n Inizio Connessione \n--------------------------\n')
try:
    connection = ConnORC_DB.openDbConnection('OracleDat_TRENTO_SRVCORSI.dat')
except:
    print('\nConnessione fallita!\n')
    exit

print('2 --------------------------\n Inizio Esportazione \n--------------------------\n')
try:
    expJ.tableExportJson('TABCLSCRIPT',connection)

except:
    print('\nEsportazione json fallita!\n')
    exit

print('3 --------------------------\n Chiusura connessione \n--------------------------\n')
ConnORC_DB.closeDbConnection(connection)

print('4 --------------------------\n Lettura file JSON \n--------------------------\n')

