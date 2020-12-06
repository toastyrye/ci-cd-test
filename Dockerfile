FROM python:3.8

ADD "/src/hello_world.py" .

# RUN pip install

CMD [ "python", "./hello_world.py"]
