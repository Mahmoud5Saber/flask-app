# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port (adjust based on your Flask app)
EXPOSE 5050

# Define environment variable
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0","--port=5050"]
