import math
from models import validierung
from datetime import datetime,timezone #mapping tabelle

class Sensormessung:
   def __init__(self,maschinen_id,zeitstemple,betriebsstunden, luftemperatur,prozesstemperatur,drehzahl,drehmoment,werkzuegverschleiss):
      self.maschinen_id = validierung.pruefe_maschinen_id(maschinen_id)
      
      self.zeitstemple = validierung.pruefe_zeittemple(zeitstemple)
      
      validierung.pruefe_nicht_negative_zahl(betriebsstunden,"Betriebsstunden")  #operating_hours  float
      self.betriebsstunden = betriebsstunden
      
      validierung.pruefe_nicht_negative_zahl(luftemperatur,"Lufttemperatur")
      self.luftemperatur =luftemperatur             # in Kelvin 0k=-273c
      
      validierung.pruefe_nicht_negative_zahl(prozesstemperatur,"Prozesstemperatur")
      self.prozesstemperatur= prozesstemperatur     # in Kelvin
      
      validierung.pruefe_nicht_negative_zahl(drehzahl,"Drehzahl")   #  rotational_speed in U/min
      self.drehzahl = drehzahl


      validierung.pruefe_nicht_negative_zahl(drehmoment,"Drehmoment")
      self.drehmoment= drehmoment  # torque in Nm
                        
      validierung.pruefe_nicht_negative_zahl(werkzuegverschleiss,"Werkzuegverschleiss") #  tool_wear   in Minuten
      self.werkzuegverschleiss = werkzuegverschleiss

   def to_dict(self):
       return {
         "Maschinen_id " :self.maschinen_id  ,           
         " Zeittemple " :self.zeitstemple.isoformat(),                 
         "Betriebsstunden" :self.betriebsstunden ,        
         " Luftemperatur ":self.luftemperatur,           
         " Prozesstemperatur ":self.prozesstemperatur ,  
         " Drehzahl":self.drehzahl ,                     
         " Drehmoment ":self.drehmoment ,                
         "Werkzuegverschleiss":self.werkzuegverschleiss
       }
 
"""
zeitprobe = datetime(2026,11,17) 
ergebnis= Sensormessung.pruefe_zeittemple(zeitprobe)
assert ergebnis==zeitprobe
print(zeitprobe)
 """       
      