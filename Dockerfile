FROM python:3.7

# Set the working directory
WORKDIR /app

# Copy the Flask app code to the container
COPY model_deployment.py .

# Copy the time series forest model to the container
COPY time_series_forest_model.joblib .

# Install the required packages
RUN pip install flask==2.2.3 pandas==1.3.4 pyts==0.12.0 joblib==1.1.0

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask app
CMD ["python", "model_deployment.py"]