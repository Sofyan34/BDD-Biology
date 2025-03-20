from fastapi import FastAPI
from src.routes import clients, commandes, objets, details  # Utiliser des imports relatifs
from src.database import engine, Base  # Importez engine et Base de database.py
from src.models import classification, informations,  repartition, Detail
# Initialiser l'application FastAPI
app = FastAPI()

# Créer les tables dans la base de données si elles n'existent pas encore
Base.metadata.create_all(bind=engine)

# Inclure les routeurs secondaires
app.include_router(classification.router)
app.include_router(informations.router)
app.include_router(repartition.router)
app.include_router(details.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API BDD Biology !"}
