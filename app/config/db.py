# app/config/db.py
import os
from mongoengine import connect

def global_init():
    db_name = os.environ.get('DB_NAME')
    db_host = os.environ.get('DB_HOST')
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    admin_user = os.environ.get('ADMIN_USER')
    admin_pass = os.environ.get('ADMIN_PASS')

    # Connect to MongoDB with optional authentication
    connect(
        db=db_name,
        host=db_host,
        username=db_username,
        password=db_password,
        authentication_source='admin'
    )
