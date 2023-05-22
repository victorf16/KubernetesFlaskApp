# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /.

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=fideliza.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["flask", "run"]
