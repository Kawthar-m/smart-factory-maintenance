# Maschinenvorlage erstellen

class Maschine:
    def __init__(self, maschinen_id, maschinentyp, installationsdatum,
                 standort, betriebsstatus):
        self.maschinen_id = maschinen_id
        self.maschinentyp = maschinentyp
        self.installationsdatum = installationsdatum
        self.standort = standort
        self.betriebsstatus = betriebsstatus

# eine Maschine anlegen und anzeigen lassen
#--- die fraese ist Test, wird später entfernt ---
fraese = Maschine("M-01", "Fräse", "2026-11-18", "Halle 1", "in Betrieb")
print(fraese.maschinen_id)
print(fraese.maschinentyp)
print(fraese.installationsdatum)
print(fraese.standort)
print(fraese.betriebsstatus)

# eine zweite Maschine anlegen
#--- die fraese2 ist Test, wird später entfernt ---
fraese2 = Maschine("M-02", "Fräse", "2026-05-18", "Halle 2", "in Betrieb")
# beide print's sind nur Test, wird später entfernt
print(fraese.standort)
print(fraese2.standort)