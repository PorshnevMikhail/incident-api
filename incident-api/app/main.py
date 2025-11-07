from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Incident API",
    description="API для учёта инцидентов",
    version="1.0.0"
)

@app.post("/incidents/", response_model=schemas.IncidentResponse)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    return crud.create_incident(db=db, incident=incident)

@app.get("/incidents/", response_model=List[schemas.IncidentResponse])
def read_incidents(
    status: Optional[models.IncidentStatus] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_incidents(db=db, status=status, skip=skip, limit=limit)

@app.patch("/incidents/{incident_id}", response_model=schemas.IncidentResponse)
def update_incident_status(
    incident_id: int,
    status_update: schemas.IncidentUpdate,
    db: Session = Depends(get_db)
):
    db_incident = crud.update_incident_status(db=db, incident_id=incident_id, status=status_update.status)
    if db_incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return db_incident

@app.get("/")
def root():
    return {"message": "Incident API is running"}