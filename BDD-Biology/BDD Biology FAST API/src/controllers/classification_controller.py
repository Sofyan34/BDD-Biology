from sqlalchemy.orm import Session
from src.models import Client
from fastapi import HTTPException
from src.schemas.species_schema import SpeciesCreate, SpeciesUpdate

def get_all_clients(db: Session):
    return db.query(classification).all()

def create_client(db: Session, client_data: SpeciesCreate):
    if db.query(classification).filter(Client.emailcli == client_data.emailcli).first():
        raise HTTPException(status_code=400, detail="Email already in use")
    
    new_client = Client(**client_data.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_client_by_id(db: Session, client_id: int):
    client = db.query(classification).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

def update_client(db: Session, client_id: int, client_data: ClientUpdate):
    client = db.query(classification).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    if client_data.emailcli and client_data.emailcli != client.emailcli:
        if db.query(classification).filter(Client.emailcli == client_data.emailcli).first():
            raise HTTPException(status_code=400, detail="Email already in use")

    for key, value in client_data.dict(exclude_unset=True).items():
        setattr(client, key, value)
    db.commit()
    db.refresh(classification)
    return client

def delete_client(db: Session, client_id: int):
    client = db.query(classification).filter(Client.codcli == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Espèce non trouvée")
    db.delete(classification)
    db.commit()
    return {"message": "Espèce supprimée avec succès"}


def get_client_by_name(db: Session, client_name: str):
    client = db.query(classification).filter(Client.nomcli == client_name).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client