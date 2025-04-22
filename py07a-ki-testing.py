def test_ist_in_einer_klasse():

	einzelschueler1 = {"Nachname": "Mustermann", "Vorname": "Max", "Klassenbezeichnung": "BFI10A"}
	einzelschueler2 = {"Nachname": "Musterfrau", "Vorname": "Maria", "Klassenbezeichnung": "WIT11C"}
	einzelschueler3 = {"Nachname": "Mustermann", "Vorname": "Markus", "Klassenbezeichnung": "MIK11A"}
	
	eine_klasse = "WIT11C"

	assert ist_in_klasse(einzelschueler1, eine_klasse) == False
	assert ist_in_klasse(einzelschueler2, eine_klasse) == True
	assert ist_in_klasse(einzelschueler3, eine_klasse) == False

def test_ist_in_mehreren_klasse():

	einzelschueler1 = {"Nachname": "Mustermann", "Vorname": "Max", "Klassenbezeichnung": "BFI10A"}
	einzelschueler2 = {"Nachname": "Musterfrau", "Vorname": "Maria", "Klassenbezeichnung": "WIT11C"}
	einzelschueler3 = {"Nachname": "Mustermann", "Vorname": "Markus", "Klassenbezeichnung": "MIK11A"}

	mehrere_klassen = "WIT11C,WIT12F"

	assert ist_in_klasse(einzelschueler1, mehrere_klassen) == False
	assert ist_in_klasse(einzelschueler2, mehrere_klassen) == True
	assert ist_in_klasse(einzelschueler3, mehrere_klassen) == False

def test_ist_in_ein_bereich():

	einzelschueler1 = {"Nachname": "Mustermann", "Vorname": "Max", "Klassenbezeichnung": "BFI10A"}
	einzelschueler2 = {"Nachname": "Musterfrau", "Vorname": "Maria", "Klassenbezeichnung": "WIT11C"}
	einzelschueler3 = {"Nachname": "Mustermann", "Vorname": "Markus", "Klassenbezeichnung": "MIK11A"}

	ein_bereich = "WIT11"

	assert ist_in_klasse(einzelschueler1, ein_bereich) == False
	assert ist_in_klasse(einzelschueler2, ein_bereich) == True
	assert ist_in_klasse(einzelschueler3, ein_bereich) == False

def test_ist_in_mehreren_bereichen():

	einzelschueler1 = {"Nachname": "Mustermann", "Vorname": "Max", "Klassenbezeichnung": "BFI10A"}
	einzelschueler2 = {"Nachname": "Musterfrau", "Vorname": "Maria", "Klassenbezeichnung": "WIT11C"}
	einzelschueler3 = {"Nachname": "Mustermann", "Vorname": "Markus", "Klassenbezeichnung": "MIK11A"}

	mehrere_bereiche = "WIT11,BFI"

	assert ist_in_klasse(einzelschueler1, mehrere_bereiche) == True
	assert ist_in_klasse(einzelschueler2, mehrere_bereiche) == True
	assert ist_in_klasse(einzelschueler3, mehrere_bereiche) == False

def test_ist_in_misch_masch():

	einzelschueler1 = {"Nachname": "Mustermann", "Vorname": "Max", "Klassenbezeichnung": "BFI10A"}
	einzelschueler2 = {"Nachname": "Musterfrau", "Vorname": "Maria", "Klassenbezeichnung": "WIT11C"}
	einzelschueler3 = {"Nachname": "Mustermann", "Vorname": "Markus", "Klassenbezeichnung": "MIK11A"}

	misch_masch = "WIT11C,BFI"

	assert ist_in_klasse(einzelschueler1, misch_masch) == True
	assert ist_in_klasse(einzelschueler2, misch_masch) == True
	assert ist_in_klasse(einzelschueler3, misch_masch) == False


def ist_in_klasse(einzelschueler, klassen):

    # Extrahiere die Klassenbezeichnung des Schülers
    klassenbezeichnung = einzelschueler.get("Klassenbezeichnung")
    
    # Teile die übergebenen Klassenbereiche in eine Liste auf
    klassen_liste = klassen.split(',')
    
    # Überprüfe, ob die Klassenbezeichnung des Schülers in einer der Klassenbereiche enthalten ist
    for klasse in klassen_liste:
        # Überprüfe, ob die Klassenbezeichnung des Schülers mit der Klasse oder dem Bereich übereinstimmt
        if klassenbezeichnung == klasse or klassenbezeichnung.startswith(klasse):
            return True
            
    return False

# Dieses if sorgt dafür, dass der Code nur dann ausgeführt wird, wenn die py-Datei vom Interpreter selbst
# auf "Top-Level" ausgeführt wird; pytest ignoriert die nachfolgenden Zeilen
if __name__ == '__main__':

    # Unser Programm soll gar nix machen, dient nur dem Testen
    pass
