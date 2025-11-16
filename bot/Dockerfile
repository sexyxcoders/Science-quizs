# Dockerfile for the bot
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy bot source code
COPY bot ./bot
COPY main.py .

# Set the default command
CMD ["python", "main.py"]