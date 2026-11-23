#Maschinenvorlage erstellen

class Machine:
    def __init__(self, machine_id, machine_type, installation_date,
                 location, operating_status):
        self.machine_id = machine_id
        self.machine_type = machine_type
        self.installation_date = installation_date
        self.location = location
        self.operating_status = operating_status

#eine Maschine anlegen und anzeigen lassen
#--- die fraese ist Test, wird später entfernt ---
fraese = Machine("M-01", "Fräse", "2026-11-18", "Halle 1", "in Betrieb")
print(fraese.machine_id)
print(fraese.machine_type)
print(fraese.installation_date)
print(fraese.location)
print(fraese.operating_status)

#eine zweite Maschine anlegen
#--- die fraese2 ist Test, wird später entfernt ---
fraese2 = Machine("M-02", "Fräse", "2026-05-18", "Halle 2", "in Betrieb")
#beide print's sind nur Test, wird später entfernt
print(fraese.location)
print(fraese2.location)