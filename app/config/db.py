# app/config/db.py
import os
from mongoengine import connect

def global_init():
    # Retrieve environment variables or define default value for local development
    db_name = os.getenv('DB_NAME', 'evaluation_exchange')
    db_host = os.getenv('DB_HOST', 'mongodb://localhost:27017/evaluation_exchange')
    
    # Optionally, retrieve authentication details if needed
    db_username = os.getenv('DB_USERNAME', 'admin')
    db_password = os.getenv('DB_PASSWORD', 'password')

    # Connect to MongoDB with optional authentication
    connect(
        db_name,
        host=db_host,
        username=db_username,
        password=db_password,
        authentication_source='admin'  # Use appropriate auth source if required
    )
