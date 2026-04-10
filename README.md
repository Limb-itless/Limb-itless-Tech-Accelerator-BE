# Welcome to Limb-itless Project

## Team members

- Siphamandla Malaza
- Jessica Harrison
- Reuben Ellis
- Nkanyiso Shabane

## Branching Strategy

This project follows Trunk-Based Development.

All work is based on a single primary branch (main), which is always kept in a deployable state. Changes are developed in short-lived branches created from main and merged back frequently through pull requests.

This approach promotes:
- Continuous integration and fast feedback
- Reduced merge conflicts
- Smaller, incremental changes

To maintain stability, all changes merged into main must pass automated checks and code review before integration.

## Running Application
1) Ensure you have installed and activated the virtual environment: 

    In main directory run commands: 
   - python -m venv venv
   - macOS/Linux: `source venv/bin/activate`
   - Windows (Command Prompt): `venv\Scripts\activate`
   - Windows (PowerShell): `venv\Scripts\Activate.ps1`

2) Install the requirements found in requirements.txt

    In main directory run command:
   - pip install -r requirements.txt

3) Start application:

    In main directory run command:
    - fastapi run (for production server)
    - fastapi dev (for dev server)

## Access API
1) To access the interactive API documentation, 
go to http://127.0.0.1:8000/docs. 
   - FastAPI automatically generates this documentation using Swagger UI.
2) You can also access alternative API documentation at http://127.0.0.1:8000/redoc, 
which uses ReDoc.
