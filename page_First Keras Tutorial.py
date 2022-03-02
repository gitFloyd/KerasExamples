# Follow the tutorial and get the dataset from
# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
#

import numpy as np
import keras as ks
models = ks.models
layers = ks.layers

# A value such as 5 will allow the code to take much less time to execute.
epochs = 5

# Again, smaller numbers make the code execute faster.
batch_size = 5

dataset = np.loadtxt("D:\Web\Python\datasets\pima-indians-diabetes.data.txt", delimiter=',')

X = dataset[:,0:8]
y = dataset[:,8]

model = models.Sequential()
model.add(layers.Dense(12, input_dim=8, activation='relu'))
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])



model.fit(X, y, epochs=epochs, batch_size=batch_size)
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))