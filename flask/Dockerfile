# Use an official Python image as the base image
FROM python:3.10.9

RUN mkdir /app
WORKDIR /app
ADD . /app
COPY requirements.txt /
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["uwsgi","uwsgi.ini"]
# # Set the working directory
# WORKDIR /similarity

# # Copy the requirements.txt file to the working directory
# COPY . /similarity

# # Create a Conda environment with the packages listed in the requirements.txt file
# RUN python -m pip install --upgrade pip

# RUN pip install -r requirements.txt

# # Set the command to run when the container starts
# CMD ["uwsgi", "uwsgi.ini"]