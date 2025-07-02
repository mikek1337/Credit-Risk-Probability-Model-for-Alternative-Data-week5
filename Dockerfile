# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies if any (none explicitly needed for this setup, but good practice)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your feature engineering pipeline script and FastAPI application code
COPY data_processed.py .
COPY main.py .

# Create directories for the feature engineering pipeline and MLflow model artifacts.
# These directories will be mounted as volumes by docker-compose, allowing your service
# to access the model files from your host machine.
RUN mkdir -p full_feat_pipeline
RUN mkdir -p mlruns/0/dummy_model_run_id/artifacts/model

# Expose the port that Uvicorn (the ASGI server) will listen on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
# The --host 0.0.0.0 makes the server accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
