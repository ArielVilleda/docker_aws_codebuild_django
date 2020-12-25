FROM python:3.8.3-slim-buster

# Initialize and Prepare
WORKDIR /data/web

# Copying the requirements.txt file first
COPY /website/requirements.txt /data/web/
# Install python requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copying the others files to avoid reinstallation
# of dependecies if other files changes
COPY /website /data/web/

# Exposing the django wsgi port
EXPOSE 8000 

# Default command to start server, changes when running
# container in prod enviroment see .../start_server.sh file
RUN chmod +x start_server.sh
CMD ./start_server.sh