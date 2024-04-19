# Define default action in case no arguments are provided
.PHONY: start-local-db
start-local-db: up create-admin

# Spin up the services (including the database)
.PHONY: up
up:
	@echo "Starting the services..."
	docker-compose up

# Create an admin user
.PHONY: create-admin
create-admin:
	@echo "Creating an admin user..."
	@python create_admin_user.py

# Stop the services
.PHONY: down
down:
	@echo "Stopping the services..."
	docker-compose down

# You may want to ensure that the ADMIN_USER and ADMIN_PASS environment variables are exported or provided
.PHONY: start-api
start-api:
	uvicorn app.main:app --reload

