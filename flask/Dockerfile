# Use an official Python image as the base image
FROM python:3.10.9

# Set the working directory
WORKDIR /similarity

# Copy the requirements.txt file to the working directory
COPY . /similarity

# Create a Conda environment with the packages listed in the requirements.txt file
RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

# Set the command to run when the container starts
CMD ["uwsgi", "uwsgi.ini"]