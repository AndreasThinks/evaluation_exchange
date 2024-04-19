# create_admin.py
import os
import sys
import datetime
from mongoengine import connect
from app.models.user import User
from app.services.auth_service import hash_password

def create_admin():
    db_name = os.environ.get('DB_NAME')
    db_host = os.environ.get('DB_HOST')
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    admin_user = os.environ.get('ADMIN_USER')
    admin_pass = os.environ.get('ADMIN_PASS')

    if not admin_user or not admin_pass:
        print("Admin username or password not provided.")
        sys.exit(1)

    # Connect to MongoDB with authentication
    connect(
        db=db_name,
        host=db_host,
        username=db_username,
        password=db_password,
        authentication_source='admin'
    )

    hashed_pwd = hash_password(admin_pass)
    admin_user_obj = User(
        name=admin_user,
        email=admin_user,
        password=hashed_pwd,
        is_evaluator=False,
        is_sponsor=False,
        is_admin=True,
        org_id='admin',
        created_at=datetime.datetime.now()
    )
    admin_user_obj.save()
    print(f'Admin user {admin_user} created successfully.')

if __name__ == "__main__":
    create_admin()
