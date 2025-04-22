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
