# Client Details API - Backend

A FastAPI backend for managing client details with SQL Server database integration.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI web server
- **SQLAlchemy** - Python SQL toolkit and ORM
- **pyodbc** - Python ODBC database connector

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- SQL Server (local or remote instance)
- Virtual environment (recommended)

## Installation

### 1. Navigate to the backend directory:
```bash
cd backend
```

### 2. Create a virtual environment (recommended):
```bash
python -m venv .venv
```

In case permission issue use below.
cmd - rmdir /s /q .venv 
powershell - Remove-Item -Recurse -Force .venv

### 3. Activate the virtual environment:

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

### Database Setup

1. Update your SQL Server connection string in `database.py` if needed
2. Run the SQL setup script to initialize the database:
```bash
sqlcmd -S <server_name> -U <username> -P <password> -i sqlserver_setup.sql
```

Or manually execute the queries in `sqlserver_setup.sql` using SQL Server Management Studio.

### Environment Variables

Create a `.env` file in the backend directory if needed for configuration:
```
DATABASE_URL=mssql+pyodbc://user:password@server/database?driver=ODBC+Driver+17+for+SQL+Server
```

## Running the Development Server

Start the FastAPI development server:
```bash
python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Available Endpoints

The API provides endpoints for managing client details. Visit the Swagger UI to explore all available endpoints and test them interactively.

## Project Structure

- `main.py` - FastAPI application and route definitions
- `models.py` - SQLAlchemy data models
- `database.py` - Database configuration and session management
- `sqlserver_setup.sql` - SQL Server database initialization script
- `requirements.txt` - Python dependencies

## Development

### Auto-reload

The `--reload` flag enables auto-reload on file changes during development. Remove this flag for production.

### CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:5173`
- `http://127.0.0.1:5173`

Update the CORS configuration in `main.py` if your frontend runs on a different port.

## Troubleshooting

### Virtual Environment Issues

If the virtual environment doesn't activate, try:
```bash
python -m venv .venv --upgrade
```

### Database Connection Errors

- Verify SQL Server is running
- Check connection string in `database.py`
- Ensure pyodbc and ODBC drivers are properly installed

### Port Already in Use

If port 8000 is in use, specify a different port:
```bash
python -m uvicorn main:app --reload --port 8001
```
