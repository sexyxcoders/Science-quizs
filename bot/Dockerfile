# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot folder
COPY . .

# Set environment variables (can also use .env file)
ENV PYTHONUNBUFFERED=1

# Start bot
CMD ["python", "main.py"]
