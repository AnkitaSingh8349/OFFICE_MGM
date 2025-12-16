"""
Script to create an ADMIN user in the database.
------------------------------------------------
This script is the BEST and ONLY way to create an admin user.
It works for both Localhost and Cloud (Aiven) databases.
It uses 'werkzeug' strictly for password hashing, matching the app's login logic.

Usage:
1. Ensure .env has the correct database credentials.
2. Run: python create_admin.py
"""
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
    PASSWORD = "adminpass"  # Will be hashed
    NAME = "Admin User"
    # -----------------------------------------------

    print(f"Checking if admin '{EMAIL}' exists...")
    existing_user = db.query(Employee).filter(Employee.email == EMAIL).first()
    
    hashed_password = generate_password_hash(PASSWORD)

    if existing_user:
        print(f"User {EMAIL} already exists! Updating password...")
        existing_user.password_hash = hashed_password
        existing_user.role = "admin" # Ensure admin role
        existing_user.status = "active"
        db.commit()
        print(f"Password updated successfully! Login with: {EMAIL} / {PASSWORD}")
    else:
        print(f"Creating new admin user: {EMAIL}")
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
