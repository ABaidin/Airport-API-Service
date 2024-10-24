# Airport API Service

This API service manages flights, airplanes, crew, and tickets for an airport management system.

## Features:
- Create, Read, Update, Delete (CRUD) operations for flights, routes, airplanes, and tickets.
- Validation to ensure proper seat/row selection.
- Swagger documentation at `/api/docs/`.

## Installation and Setup

### 1. Local Development

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd airport-api
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
3. Create and configure a PostgreSQL database:

    ```bash
    createdb airportdb
4. Run migrations:

    ```bash
    python manage.py migrate
5. Load sample data:

    ```bash
    python manage.py loaddata sample_data.json
6. Start the development server:

    ```bash
    python manage.py runserver
### 2. Using Docker
1. Build the Docker image and start the containers:

    ```bash
    docker-compose up --build
2. Open the API at http://localhost:8000/api/.