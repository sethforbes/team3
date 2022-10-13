# start with our base image
FROM python:3.9

# create a folder in the container called code, and set this as the current directory
WORKDIR /code

# copy the requirements file into the code folder
COPY ./requirements.txt /code/requirements.txt

# install the requirements with pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# the app folder into the code/app directory in the container
COPY ./app /code/app


# run the app -- the webapp is in the app folder, called main.py3-3
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
