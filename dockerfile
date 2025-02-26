# Use Python 3.10 (NOT 3.12)
FROM python:3.10

# Install system dependencies required to build aiohttp
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    build-essential

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Start the bot
CMD ["python", "telebot.py"]
