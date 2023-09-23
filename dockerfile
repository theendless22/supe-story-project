#why only run this as a script when we can complicate it further by dockerizing it. 

FROM python:latest

LABEL owner="theendless"

WORKDIR /supe-project/src
COPY ./main.py /supe-project/src/

CMD [ "python", "./main.py"]

#Clone this repo and from within this folder, run: docker run <name> 