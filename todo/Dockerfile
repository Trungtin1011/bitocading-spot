# Base image
FROM python:alpine3.20

# Maintainer metadata
LABEL maintainer="trungtin" maintainer_contact="trungtinth1011@gmail.com"

# Run every next command wih this user
USER root

# Create work directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . /app

# Install dependencies
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port
EXPOSE 8080

# Starting application
ENTRYPOINT ["python3", "main.py"]
