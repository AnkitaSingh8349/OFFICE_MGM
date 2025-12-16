from dotenv import load_dotenv, find_dotenv
import os
from passlib.context import CryptContext
from sqlalchemy.orm import Session

# Load env vars
load_dotenv(find_dotenv())

from app.database import engine, Base, SessionLocal
from app.employees.models import Employee
from werkzeug.security import generate_password_hash

def create_admin():
    db: Session = SessionLocal()
    
    # ---------------- ADMIN DETAILS ----------------
    # Change these if you want different credentials
    EMAIL = "ankita@ajxtechnologies.com"
    PASSWORD = "admin"  # Will be hashed
    NAME = "Admin User"
    # -----------------------------------------------

    print(f"Checking if admin '{EMAIL}' exists...")
    existing_user = db.query(Employee).filter(Employee.email == EMAIL).first()
    
    if existing_user:
        print(f"User {EMAIL} already exists!")
    else:
        print(f"Creating new admin user: {EMAIL}")
        hashed_password = generate_password_hash(PASSWORD)
        
        new_admin = Employee(
            email=EMAIL,
            password_hash=hashed_password,
            name=NAME,
            role="admin",  # Important
            status="active"
        )
        
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        print("Admin user created successfully!")
        print(f"Login with: {EMAIL} / {PASSWORD}")

    db.close()

if __name__ == "__main__":
    create_admin()
