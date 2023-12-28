# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /WeatherAppAPI
WORKDIR /WeatherAppAPI

# Copy the entire project directory into the container at /WeatherAppAPI
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements

# Install specific versions of Flask and Werkzeug
RUN pip install flask==2.0.2 werkzeug==2.0.2

# Set environment variables
ENV FLASK_APP=Server.py
ENV FLASK_RUN_HOST=127.0.0.1
ENV FLASK_RUN_PORT=8000

# Install necessary packages
RUN pip install uvicorn

# Run the FastAPI application with uvicorn
CMD ["uvicorn", "Server:app", "--host", "127.0.0.1", "--port", "8000"]
