# w01-backend-health-api

## Local Setup Guide
To run the server in your local environment, follow these steps:

Step 1: Ensure that Python 3 is installed on your machine.

Step 2: Open Git Bash or Terminal at the project's root directory and activate the virtual environment:
- For Windows (Git Bash / CMD): .\venv\Scripts\activate
- For macOS / Linux: source venv/bin/activate

Step 3: Launch the Backend server using the following command: python server.py

## API Endpoint Information
Once the server is running successfully, the local endpoint will be ready to handle requests:
- URL: http://localhost:8000/api/health
- Method: GET
- Standard Response: 200 OK with the following JSON body format:

{
  "status": "OK",
  "message": "Backend server is running smoothly"
}

## Testing Workflow with Postman
All test cases for API verification have been pre-configured in the project:
- Environment Variables: Utilizes the {{baseUrl}} variable. Make sure you have configured its value to http://localhost:8000 in your Postman Local environment.
- Storage Path: The Collection folder is named Intern Training. You can quickly import it into Postman from the following path: docs/postman/Intern Training.postman_collection.json