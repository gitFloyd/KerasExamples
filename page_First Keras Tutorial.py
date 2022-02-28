# Follow the tutorial and get the dataset from
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
#

import simpleUtility as su
import numpy as np
import keras as ks
models = ks.models
layers = ks.layers

dataset = np.loadtxt("D:\Web\Python\datasets\pima-indians-diabetes.data.txt", delimiter=',')

X = dataset[:,0:8]
y = dataset[:,8]

model = models.Sequential()
model.add(layers.Dense(12, input_dim=8, activation='relu'))
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Enclose our output in <main>...</main>
# which gives a bit of additional css
# formatting which is specified in test.css
with su.TextWrapper('main'):
	# The functions fit() and evaluate() leak output to stdout
	# The with statement allows us to wrap that content
	# in a hidden div.
	with su.Pre():
		model.fit(X, y, epochs=5, batch_size=5)
		_, accuracy = model.evaluate(X, y)
	su.printbr('Accuracy: %.2f' % (accuracy*100))