# Define the base image.
FROM python:3.7
# Copy files into image.
COPY ./requirements.txt . 
# Execute a command on an intermediate container.
RUN pip3 install -r requirements.txt
# Copy files into image.
COPY . . 
# Selects the port that the container listens on.
EXPOSE 5000
# Define the main process for the container to run on start-up.
ENTRYPOINT ["gunicorn", "--workers=4", "--bind=0.0.0.0:5002", "app:app"]
