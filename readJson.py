import pandas as pd
import re

def _read_script(df:pd.DataFrame,tipo:str,df_line:int=0)->str:
    """Riceve in input un data frame , il tipo di script che si vuole gestire e (opzionalmente) la riga
    del dataframe che si vuole gestire in particolare, altrimenti di default legge la riga 0"""
    tmp=df[df['TIPO']==tipo]
    return tmp['CODICE'][df_line]
 

def _handle_script(script:str,dizionario:pd.DataFrame)->str:
    """Riceve in input una stringa che rappresenta lo script da gestire
    e un data frame dizionario ed esegue la replace come descritto nel dizionario"""
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
    """Carica come data frame un dizionario"""
    print("...carico dizionario...")
    diz=pd.read_csv(r"\\srvopenco\Open-Co\Personali\03 - Temporanea\Samuele\PythonProject\UTILITY\Dizionario.csv",delimiter=';',header=0)
    diz.fillna(' ', inplace=True)
    print(diz)
    return diz


def _help_()->str:
    print("Comandi da lanciare in sequenza:\n"+
          "1) _read_script(DataFrame,Tipo script,(opzionale) numero riga)\n"+
          "2) dizionario=_load_trad_dict()\n"+
          "3) script=_handle_script(script_convert,dizionario)"
          )
if __name__=='__main__':
    df=pd.read_json(r"\\srvopenco\Open-Co\Personali\03 - Temporanea\Samuele\PythonProject\JSON\20231219_TABCLSCRIPT.json")
    script_convert=_read_script(df,'SCRIPT')
    #print(script_convert)
    dizionario=_load_trad_dict()
    script=_handle_script(script_convert,dizionario)
    print(script)