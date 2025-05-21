from fastapi import FastAPI


# FastAPI-App erstellen
app = FastAPI() #Erstellt eine neue API-Instanz

# Einfachen GET-Endpunkt hinzufügen -> gibt JSON zurück
@app.get("/test") # Definiert einen Endpunkt, der auf GET /test reagiert
def read_test():
    return {"message": "Hallo Welt! Das ist meine erste API!"}
