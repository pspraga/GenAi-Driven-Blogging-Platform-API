# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files to disc and to not buffer output
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create and set the working directory for the Django app
WORKDIR /GENAI

# Install dependencies
COPY requirements.txt /GENAI/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY . /GENAI/

# Expose port 8000 (the default Django port)
EXPOSE 8083

# Start the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8083"]
