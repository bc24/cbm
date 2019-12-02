def create_person(id, vorname, nachname):
    dict={'ID':id, 'vorname': vorname, 'nachname': nachname }
    return dict                                  # Weitergabe an create_person
    
def person_data():
    id=input('Bitte eine ID angeben ')           # Wird mit ID gefühllt
    vorname = input('Vorname eingaben ')         # Wird mit Vorname gefühllt
    nachname = input('Nachname eingeben ')       # Wird mit Nachname gefühllt
    return create_person(id,vorname,nachname)    # Weitergabe an person_data
    
liste=[]                                         # leere Liste wird erzeugt
liste.append(person_data())                      # Wird an der Liste angefügt
print(liste)

