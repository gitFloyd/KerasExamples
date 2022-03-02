# https://keras.io/examples/vision/image_classification_from_scratch/

# Installation errors?
# See: https://github.com/XifengGuo/CapsNet-Keras/issues/25#issuecomment-515690929

# Note the ds_path variable. Point it to your PetImages dataset.

import tensorflow as tf

keras = tf.keras
layers = keras.layers
preprocessing = keras.preprocessing

image_size = (180, 180)
batch_size = 32
ds_path = "D:\Web\Python\datasets\kagglecatsanddogs_3367a\PetImages"

train_ds = preprocessing.image_dataset_from_directory(
	ds_path,
	validation_split=0.2,
	subset='training',
	seed=1337,
	image_size=image_size,
	batch_size=batch_size
)
val_ds = preprocessing.image_dataset_from_directory(
	ds_path,
	validation_split=0.2,
	subset='validation',
	seed=1337,
	image_size=image_size,
	batch_size=batch_size
)

# Visualize nine of the images:
# import matplotlib.pyplot as plt
# 
# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#	 for i in range(9):
#		 ax = plt.subplot(3, 3, i + 1)
#		 plt.imshow(images[i].numpy().astype("uint8"))
#		 plt.title(int(labels[i]))
#		 plt.axis("off")
# plt.show()




# # Use GPU acceleration to rescale the image pixel data from [0,255] to [0,1]
# inputs = keras.Input(shape=image_size)
# x = data_augmentation(inputs)
# x = layers.Rescaling(1./255)(x)

# use buffered prefetching so we can yield data from disk without having I/O becoming blocking:
train_ds = train_ds.prefetch(buffer_size=32)
val_ds = val_ds.prefetch(buffer_size=32)

def make_model(input_shape, num_classes):
	global keras, layers, preprocessing
	data_augmentation = keras.Sequential(
		[
			layers.RandomFlip("horizontal"),
			layers.RandomRotation(0.1),
		]
	)
	inputs = keras.Input(shape=input_shape)
	# Image augmentation block
	x = data_augmentation(inputs)

	# Entry block
	x = layers.Rescaling(1.0 / 255)(x)
	x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
	x = layers.BatchNormalization()(x)
	x = layers.Activation("relu")(x)

	x = layers.Conv2D(64, 3, padding="same")(x)
	x = layers.BatchNormalization()(x)
	x = layers.Activation("relu")(x)

	previous_block_activation = x  # Set aside residual

	for size in [128, 256, 512, 728]:
		x = layers.Activation("relu")(x)
		x = layers.SeparableConv2D(size, 3, padding="same")(x)
		x = layers.BatchNormalization()(x)

		x = layers.Activation("relu")(x)
		x = layers.SeparableConv2D(size, 3, padding="same")(x)
		x = layers.BatchNormalization()(x)

		x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

		# Project residual
		residual = layers.Conv2D(size, 1, strides=2, padding="same")(
			previous_block_activation
		)
		x = layers.add([x, residual])  # Add back residual
		previous_block_activation = x  # Set aside next residual

	x = layers.SeparableConv2D(1024, 3, padding="same")(x)
	x = layers.BatchNormalization()(x)
	x = layers.Activation("relu")(x)

	x = layers.GlobalAveragePooling2D()(x)
	if num_classes == 2:
		activation = "sigmoid"
		units = 1
	else:
		activation = "softmax"
		units = num_classes

	x = layers.Dropout(0.5)(x)
	outputs = layers.Dense(units, activation=activation)(x)
	return keras.Model(inputs, outputs)


model = make_model(input_shape=image_size + (3,), num_classes=2)
keras.utils.plot_model(model, show_shapes=True)

epochs = 1

callbacks = [
	keras.callbacks.ModelCheckpoint("save_at_{epoch}.h5"),
]
model.compile(
	optimizer=keras.optimizers.Adam(1e-3),
	loss="binary_crossentropy",
	metrics=["accuracy"],
)
model.fit(
	train_ds, epochs=epochs, callbacks=callbacks, validation_data=val_ds,
)

img = keras.preprocessing.image.load_img(
	ds_path + "/Cat/6779.jpg", target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
score = predictions[0]
print(
	"This image is %.2f percent cat and %.2f percent dog."
	% (100 * (1 - score), 100 * score)
)