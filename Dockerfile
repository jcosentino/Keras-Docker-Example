FROM ubuntu:latest
MAINTAINER John Cosentino "john.s.cosentino@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential hdf5-tools
COPY . ~/Projects/kerasAssg
WORKDIR ~/Projects/kerasAssg
EXPOSE 5000
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["kerasFlask.py"]
