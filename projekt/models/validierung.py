import math
from datetime import datetime

def konvertiere_zeitstemple(eingabe):                                                      
      print("eingabe",eingabe)                                 
      zeitstemple = datetime.strptime(eingabe,"%Y.%m.%d %H:%M")
      return zeitstemple     
  
                                                                                                        
def pruefe_zeittemple(zeitstemple):                                                             
       zeitstemple=konvertiere_zeitstemple(zeitstemple)                                            
       if not isinstance(zeitstemple,datetime):                                                         
           raise TypeError("Zeitstempel soll als nur als Datum_Uhrzeit und vollständige eingeschrieben")
       #if zeittemple.tzinfo is None or zeittemple.utcoffset() is None:                                 
        #   raise ValueError("Zeitstemple benötigt eine Zeitzone") 
        
       return zeitstemple


def pruefe_maschinen_id(maschinen_id):                                                                      
    if not isinstance(maschinen_id,str):                       
        raise TypeError("Maschinen_ID muss als Text sein")     
    if not maschinen_id.strip():                               
        raise ValueError ("Maschienen_ID darf nicht leer sein")
    return maschinen_id.strip()   


def pruefe_nicht_negative_zahl(wert,name):                                  
        if isinstance(wert,bool) or not (wert,(int,float)): #reicht nur ein?
            raise TypeError (f"{name} muss eine Zahl sein")                 
        if wert<0:                                                          
            raise ValueError(f"{name} darf nicht negativ sein")             
        if name == "Prozesstemperatur" or name == "Lufttemperatur":         
            if wert == 0:                                                   
                  raise ValueError(f"{name} darf nicht null sein")          
        if not math.isfinite(wert):                                         
            raise ValueError (f"{name} muss endliche sein")                 