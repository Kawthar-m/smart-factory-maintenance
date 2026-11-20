from enum import Enum
from models import validierung
class Schweregrad(Enum):
    NIEDRIG = "niedrig"
    MITTEL = "mittel"
    HOCH = "hoch"
    KRITISCH = "kritisch"

class Wartungsereignis:   
    def __init__(self,maschinen_id,zeitstemple,betriebsstunden,
                 vorfall_type,schweregrad,techniker_notizen):
        self.maschinen_id = validierung.pruefe_maschinen_id(maschinen_id)

        self.zeitstemple = validierung.pruefe_zeittemple(zeitstemple)           # Zeitpunkt des Ereignisses

        validierung.pruefe_nicht_negative_zahl(betriebsstunden,"Betriebsstunden")
        self.betriebsstunden= betriebsstunden
        
        self.vorfall_type= vorfall_type                                   # oder Stoerungsart?  z.B. "Tool Wear Failure", "Routine Check"
       
        self.schweregrad= self.pruefe_schweregrad(schweregrad)            # "low", "medium", "high", "critical"
        
        self.techniker_notizen= techniker_notizen


    @staticmethod
    def pruefe_schweregrad(schweregrad):
        
        
        if not isinstance(schweregrad,Schweregrad):         #umwandlung von string zu Schweregrad wird danach im main geschrieben
            raise TypeError("Ungültiger Schweregrad.Schreib einer dieser Wörter : niedrig,mittel,hoch,kritisch")
        return schweregrad

    
    def to_dict(self):
        return{
        "Maschinen_id ":self.maschinen_id  ,            
        "Zeitstemple":self.zeitstemple.isoformat() ,          
        "Betriebsstunden":self.betriebsstunden ,   
        "Vorfall_type  ":self.vorfall_type,       
        "Schweregrad":self.schweregrad.value  ,          
        "Techniker_notizen":self.techniker_notizen
        }