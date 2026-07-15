## What
- Initialized the base Backend project structure and configured .gitignore to exclude redundant/environment files (venv, __pycache__).
- Authored a comprehensive guide for local environment setup and execution in README.md.
- Successfully implemented the GET /api/health API endpoint to return system status.
- Configured the PULL_REQUEST_TEMPLATE.md file to standardize future development workflows.
- Initialized and exported the Postman Collection for automated API testing.

## Why
- A standardized project structure and clear documentation are essential for team members and Mentors to easily set up and run the project locally.
- Implementing the /api/health endpoint serves as a baseline sanity check, ensuring the server can listen to and handle requests properly before migrating to larger frameworks (FastAPI/Django).

## How
- Utilized Python's native http.server and json libraries to spin up a lightweight HTTP Server on port 8000 without any external dependencies.
- Developed the HealthCheckHandler class (extending BaseHTTPRequestHandler) to capture GET requests and return a 200 OK status code with application/json headers.
- Maintained a standard Git Flow workflow: Created the feature/setup-backend-api branch from main, followed Conventional Commits guidelines, and fully resolved merge conflicts locally before opening this PR.