Flask CI/CD Pipeline with GitHub Actions and Docker
Overview
This document provides a detailed description of the Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Flask web application. The pipeline automates the process of building, testing, and deploying the application using GitHub Actions and Docker.

Project Structure
The project consists of the following components:

.github/: Contains the GitHub Actions workflow configuration.
templates/: Stores HTML templates used by the Flask application (if applicable).
.pytest_cache/: Stores temporary test cache files.
pycache/: Contains compiled Python files.
app.py: The main Flask application file.
test_app.py: Contains unit tests for the application using Pytest.
requirements.txt: Lists the required dependencies for the project.
Dockerfile: Defines the instructions to build a Docker image for the application.
README.md: Provides documentation for the project.

Setup Instructions
Installing Dependencies
To install the required dependencies, run the following command:

pip install -r requirements.txt


Running the Flask Application
To start the Flask application locally, execute:

python app.py
Once the application is running, it can be accessed at http://localhost:5050/.


Running Unit Tests
To verify the functionality of the application using Pytest, run:

pytest test_app.py


Docker Setup
Building the Docker Image
To build a Docker image for the application, use:

docker build -t flask-app .

Running the Docker Container
To run the application inside a Docker container, execute:

docker run -p 5050:5050 flask-app

GitHub Actions Workflow
The GitHub Actions workflow automates the CI/CD process and is stored in the .github/workflows/ directory. The workflow includes the following steps:

Running unit tests using Pytest.
Building a Docker image.


Contributors
[Mahmoud Saber]
February,22 2025