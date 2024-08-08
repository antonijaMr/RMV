import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Učitavanje CIFAR-10 dataseta
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalizacija slika
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# One-hot encoding oznaka
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Kreiranje modela
model = Sequential()

# Prvi konvolucioni sloj
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D((2, 2)))

# Drugi konvolucioni sloj
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

# Treći konvolucioni sloj
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

# Pretvaranje u 1D
model.add(Flatten())

# Fully connected sloj
model.add(Dense(512, activation='relu'))

# Izlazni sloj
model.add(Dense(10, activation='softmax'))

# Kompilacija modela
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Treniranje modela
history = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_test, y_test))

# Grafikon tačnosti i gubitka
plt.figure(figsize=(12, 4))

# Tačnost treniranja
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Gubitak treniranja
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.show()

