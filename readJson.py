import pandas as pd
import os
import re

def _read_script(df:pd.DataFrame,tipo:str,df_line:int=0)->str:
    """
    Riceve in input un data frame , il tipo di script che si vuole gestire e (opzionalmente) la riga
    del dataframe che si vuole gestire in particolare, altrimenti di default legge la riga 0
    """
    tmp=df[df['TIPO']==tipo]
    return tmp['CODICE'][df_line]
 

def _handle_script(script:str,dizionario:pd.DataFrame)->str:
    """
    Riceve in input una stringa che rappresenta lo script da gestire
    e un data frame dizionario ed esegue la replace come descritto nel dizionario
    """
    script_converted=script
    for index, row in dizionario.iterrows():
        what_to_find=row['ORACLE']
        what_to_replace=row['SQL']
        print(row['SQL']+' ---> '+row['ORACLE']+' | '+row['DESCRIZIONE'])
        if  what_to_find=='36':#$
            occurrences=[match.start() for match in re.finditer(re.escape(chr(int(what_to_find))), script_converted,flags=re.IGNORECASE)]
            
        else:
            occurrences=[match.start() for match in re.finditer(rf'{what_to_find}', script_converted,flags=re.IGNORECASE)]
        
        if occurrences:
            print(f"Occurrences of {what_to_find} with space before and after: {occurrences}")
            if what_to_find=='36':#$
                script_converted=re.sub(rf'\$', what_to_replace, script_converted,flags=re.IGNORECASE)
            else:
                script_converted=re.sub(rf'{what_to_find}', what_to_replace, script_converted,flags=re.IGNORECASE)
        else:
            print(f"No {what_to_find} occurrences found.")
    return script_converted

def _load_trad_dict()->pd.DataFrame:
    """
    Carica come data frame un dizionario
    """
    print("...carico dizionario...")
    diz=pd.read_csv(r"UTILITY\Dizionario.csv",delimiter=';',header=0)
    diz.fillna(' ', inplace=True)
    print(diz)
    return diz

def _generate_standard_insert(table:str):
    """
    Genera istruzione insert per la tabella selezionata
    """
    found_file = find_file_by_name(r"JSON" , table)
    
    if found_file:
        print("Trovato file "+found_file)
        df=pd.read_json(found_file) #leggo il file
        #print(df)
        
    else:
        print("No file found.")
    
    return None

def _generate_standard_create(table:str)->str:
    """
    Genera istruzione CREATE per la tabella selezionata
    Ritorna una stringa.
    """
    found_file = find_file_by_name(r"JSON" , table)
    table_create_cmd=f"CREATE TABLE {table} ("
    if found_file:
        print("Trovato file "+found_file)
        df=pd.read_json(found_file) #leggo il file
        #print(df)
        for index, row in df.iterrows():
            if row['DATA_TYPE'].apply(lambda x: "VARCHAR" in x):
                table_create_cmd=table_create_cmd+row['COLUMN_NAME']+" VARCHAR("+row['DATA_LENGTH']+")"
            elif row['DATA_TYPE']=='NUMBER':
                table_create_cmd=table_create_cmd+row['COLUMN_NAME']+" NUMERIC("+row['DATA_PRECISION']+","+row['DATA_SCALE']+")"
            else:
                table_create_cmd=table_create_cmd+row['COLUMN_NAME']+" "+row['DATA_TYPE']
        table_create_cmd=table_create_cmd+");"
    else:
        print("No file found.")
        return ""
    
    return table_create_cmd

def _help_()->str:
    """Fornisce piccolo tutorial di come lanciare i comandi"""
    print("Comandi da lanciare in sequenza:\n"+
          "1) _read_script(DataFrame,Tipo script,(opzionale) numero riga)\n"+
          "2) dizionario=_load_trad_dict()\n"+
          "3) script=_handle_script(script_convert,dizionario)"
          )
    
    
    
def find_file_by_name(directory, target_string):
    # Get a list of files in the directory
    files = os.listdir(directory)
    target_string='_CONF_'+target_string
    # Filter files based on the specified string
    matching_files = [file for file in files if target_string in file]

    if not matching_files:
        print(f"No files found with the specified string: {target_string}")
        return None

    # Assume you want to get the first matching file
    file_to_find = matching_files[0]

    # Construct the full path to the file
    file_path = os.path.join(directory, file_to_find)

    return file_path


    
if __name__=='__main__':
    df=pd.read_json(r"JSON\20231219_TABCLSCRIPT.json")
    script_convert=_read_script(df,'SCRIPT')
    #print(script_convert)
    #dizionario=_load_trad_dict()
    #script=_handle_script(script_convert,dizionario)
    #print(script)
    _generate_standard_insert('TABCCAMPIONI')
    
