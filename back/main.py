
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from dotenv import load_dotenv

import os
import resend

from database import engine, Base, get_db
import models

from schema import ContactResponse


# Load environment variables
load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
resend.api_key = RESEND_API_KEY


app = FastAPI()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5186"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables
#Base.metadata.create_all(bind=engine)


# Request schema
class Contact(BaseModel):
    name: str
    email: str
    message: str


# CREATE
@app.post("/contact")
def create_contact(
    contact: Contact,
    db: Session = Depends(get_db)
):
    new_contact = models.Contact(
        name=contact.name,
        email=contact.email,
        message=contact.message
    )

    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    # Send email notification
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": "bathi2389@gmail.com",
        "subject": "New Portfolio Contact",
        "html": f"""
            <h2>New Contact Message</h2>

            <p>
                <strong>Name:</strong> {contact.name}
            </p>

            <p>
                <strong>Email:</strong> {contact.email}
            </p>

            <p>
                <strong>Message:</strong> {contact.message}
            </p>
        """
    })

    return {
        "message": "Contact saved successfully",
        "id": new_contact.id
    }


# READ
@app.get("/contacts", response_model=list[ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    contacts = db.query(models.Contact).all()

    return contacts


# UPDATE
@app.put("/contacts/{contact_id}", response_model=ContactResponse)
def update_contact(
    contact_id: int,
    contact: Contact,
    db: Session = Depends(get_db)
):
    existing_contact = db.query(models.Contact).filter(
        models.Contact.id == contact_id
    ).first()

    if existing_contact is None:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )

    existing_contact.name = contact.name
    existing_contact.email = contact.email
    existing_contact.message = contact.message

    db.commit()
    db.refresh(existing_contact)

    return existing_contact


# DELETE
@app.delete("/contacts/{contact_id}")
def delete_contact(
    contact_id: int,
    db: Session = Depends(get_db)
):
    existing_contact = db.query(models.Contact).filter(
        models.Contact.id == contact_id
    ).first()

    if existing_contact is None:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )

    db.delete(existing_contact)
    db.commit()

    return {
        "message": "Contact deleted successfully"
    }
@app.get("/")
def health_check():
    return {"message": "API is running"}

