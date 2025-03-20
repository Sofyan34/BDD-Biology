# src/schemas/client_schema.py
from pydantic import BaseModel

class SpeciesCreate(BaseModel):
    genrecli: str | None = None
    nomcli: str | None = None
    prenomcli: str | None = None
    adresse1cli: str | None = None
    adresse2cli: str | None = None
    adresse3cli: str | None = None
    villecli_id: int | None = None
    telcli: str | None = None
    emailcli: str | None = None
    portcli: str | None = None
    newsletter: int | None = None

class SpeciesUpdate(SpeciesCreate):
    genrecli: str | None = None
    nomcli: str | None = None
    prenomcli: str | None = None
  
