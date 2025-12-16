from dotenv import load_dotenv, find_dotenv
import os

# Load env vars FIRST, before importing app.database
load_dotenv(find_dotenv())

print(f"Debug: Connecting to {os.getenv('DB_HOST')}...")

from app.database import engine, Base
from app.employees.models import *
from app.attendance.models import *
from app.leaves.models import *
from app.salary.models import *
from app.tasks.models import *

print("Creating tables in the database...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
