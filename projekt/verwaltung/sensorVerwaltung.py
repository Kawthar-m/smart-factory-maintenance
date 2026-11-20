from models.sensormessung import Sensormessung
from models import validierung
import math

class Sensorverwaltung:
    def __init__(self):
        self.messungenDict = {}

    def messung_hinzufuegen(self,neuSensormessung):
           if  not isinstance(neuSensormessung,Sensormessung):
                raise TypeError ("Fehler beim Eingabe" )
           machine_id = neuSensormessung.maschinen_id
           if machine_id  in self.messungenDict:  
             self.messungenDict[neuSensormessung.maschinen_id].append(neuSensormessung) 
           else:
             self.messungenDict[neuSensormessung.maschinen_id]=[neuSensormessung]  #neue Liste nizufügen
                

    def messungen_nach_maschine_suchen(self,maschinen_id):
       maschinen_id = validierung.pruefe_maschinen_id(maschinen_id)
       return self.messungenDict.get(maschinen_id,[])
    
    
    def liste_von_Messungen_ausgeben(gefundene_messungen):
        for messung in gefundene_messungen:
            print(messung.to_dict())   
        

    def nach_min_Betriebstunden_filtern(self,min_stunden):
        ergebnis =[]
        for liste_messungen in self.messungenDict.values():
            for sensor_messung in liste_messungen:
                if sensor_messung.betriebsstunden >= min_stunden:
                    ergebnis.append(sensor_messung.betriebsstunden)
        return ergebnis

    def letzte_messungen_suchen(self,maschinen_id):
        messungen = self.messungen_nach_maschine_suchen(maschinen_id)
        letzte_zeitstemple= max(messungen,key = lambda messung : messung.zeitstemple)#lambda vergleicht jede zeitstemple von jeder objekt 
        return letzte_zeitstemple
    
        
    def to_dict(self):
        return self.messungenDict












