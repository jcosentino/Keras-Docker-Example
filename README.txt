[KERAS] ASSIGNMENT
Completed by John Cosentino john.s.cosentino@gmail.com
Offered by [redacted]

I built the app on a fully up-to-date version of Ubuntu 18.04 (x86_64)
I used the Flask web framework and Docker to build this app.

In this folder you will find:
1. cats_dogs_model.hdf5 -> Keras model
2. Dockerfile -> The Dockerfile that can be used to run this app
2. instructions.txt -> Alex's instructions for me
3. README.txt -> this file
4. requirements.txt -> is used by the Dockerfile to install the necessary pip modules
5. screenshot.png -> A screenshot of the app in use
6. kerasAssg.py -> this is the python file that runs the Keras prediction simulation. You do not run this directly; it is run by the Flask app
7. kerasFlask.py -> You may run this app
	7a) You can run this using the command:
		python kerasFlask.py
		This will simply render an error message on a webpage. This is because you are meant to run a command with image files as apart of the argument
	7b) The following command is desirable:
		python kerasFlask.py images/*.jpg
		This will run the predictions on all of the images inside of the images/ folder
8. images/ -> This contains a series of dog and cat images to be used by kerasAssg.py

I built the docker image with the following command:
docker build -t kerasAssg .

I ran the image using the following command:
docker run -d -p 5001:5000 kerasAssg python kerasFlask.py images/*.jpg

Issues:
1. The app is a little slow in displaying the Keras predictions to the webpage. The Keras model seems to take longer to finish than the app does to load, so initially, it appears as though the app fails. You must wait briefly.
2. The GUI is not refined by any means.
3. The Docker image does seem to understand directories as parameters in the command. Therefore, one must run the python kerasFlask.py images/*.jpg as apart of the docker execution command. A restructuring of the code, or an alternative command to the Docker file must be introduced.