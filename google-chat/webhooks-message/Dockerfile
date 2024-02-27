# Description: Dockerfile for the webhooks-message application
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the source code
COPY ./src /app/src

# Install the dependencies
RUN python -m venv ./src/venv
RUN . ./src/venv/bin/activate
RUN pip install -r ./src/requirements.txt

# Install Nginx package
RUN apt-get update
RUN apt-get install -y nginx

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

