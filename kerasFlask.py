from flask import Flask, request
import numpy as np
import h5py
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import sys
from kerasAssg import createSinglePrediction

app = Flask(__name__)

def createPredictions():
	if len(sys.argv) <= 1:
		return 'Not enough command line args!'
	predictions = []
	FULL_HTML = []
	for x in range(1, len(sys.argv)):
		image = sys.argv[x]
		pred = createSinglePrediction(image)
		predictions.append(
			'<tr><td>{}</td></tr>'.format(pred)
			)
	predictions = '<table>\n{}\n</table>'.format('\n'.join(predictions))
	FULL_HTML.append(predictions)
	return "<html>\n{}\n</html>".format('\n'.join(FULL_HTML))

@app.route('/', methods=['GET', 'POST'])
def index():
	if(request.method == 'POST'):
		return createPredictions()
	else:
		return createPredictions()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
