# Maschinenvorlage erstellen

class Maschine:
    def __init__(self, maschinen_id, maschinentyp, installationsdatum,
                 standort, betriebsstatus):
        self.maschinen_id = maschinen_id
        self.maschinentyp = maschinentyp
        self.installationsdatum = installationsdatum
        self.standort = standort
        self.betriebsstatus = betriebsstatus

    def status_aendern(self, neuer_status):
        self.betriebsstatus = neuer_status

    def __str__(self):
        return f"{self.maschinen_id}: {self.maschinentyp}, {self.standort}, {self.betriebsstatus}, installiert am {self.installationsdatum}"


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


#  Status ändern
#--- nur Test, wird später entfernt ---
print(fraese.betriebsstatus)
fraese.status_aendern("Wartung")
print(fraese.betriebsstatus)

# Maschine anzeigen
#--- nur Test, wird später entfernt ---
print(fraese)
print(fraese2)
