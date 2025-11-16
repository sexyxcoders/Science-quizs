# Use official Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy bot source code
COPY . .

# Expose port if needed (optional)
# EXPOSE 8443

# Run bot
CMD ["python", "main.py"]