#!/user/
# -*- coding:utf-8 -*-
import os
import numpy as np
import gzip
import keras
from keras.models import Sequential,Model
from keras.layers import Input,Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D,UpSampling2D
from keras import backend as K
import cv2

def load_data(data_folder):

  files = [
      'train-labels-idx1-ubyte.gz', 'train-images-idx3-ubyte.gz',
      't10k-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz'
  ]

  paths = []
  for fname in files:
    paths.append(os.path.join(data_folder,fname))

  with gzip.open(paths[0], 'rb') as lbpath:
    y_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

  with gzip.open(paths[1], 'rb') as imgpath:
    x_train = np.frombuffer(
        imgpath.read(), np.uint8, offset=16).reshape(len(y_train), 28, 28)

  with gzip.open(paths[2], 'rb') as lbpath:
    y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

  with gzip.open(paths[3], 'rb') as imgpath:
    x_test = np.frombuffer(
        imgpath.read(), np.uint8, offset=16).reshape(len(y_test), 28, 28)

  return (x_train, y_train), (x_test, y_test)

(X_train, y_train), (X_test, y_test) = load_data('C:\soft\pycharm\python\Tf2.0\mnist')

x_train = X_train.astype('float32') / 255
x_test = X_test.astype('float32') / 255
x_train = np.reshape(x_train, (len(x_train),28,28,1))
x_test = np.reshape(x_test, (len(x_test), 28,28,1))

noise_factor = 0.5
x_train_noisy = x_train + noise_factor * np.random.normal(loc = 0.0, scale = 1.0,size = x_train.shape)
x_test_noisy = x_test + noise_factor * np.random.normal(loc = 0.0, scale = 1.0, size = x_test.shape)

x_train_noisy = np.clip(x_train_noisy,0.,1.)
x_test_noisy = np.clip(x_test_noisy,0.,1.)

batch_size = 128
num_classes = 10
epoches = 1

img_rows, img_cols = 28,28
input_shape = (28,28,1)
model = Sequential()
x = Conv2D(32,(3,3),activation = 'relu',padding = 'same',input_shape = input_shape)
model.add(x)
x = MaxPooling2D((2,2),padding = 'same')
model.add(x)
x = Conv2D(32,(3,3),activation = 'relu',padding = 'same')
model.add(x)
encoded = MaxPooling2D((2,2),padding = 'same')
model.add(encoded)

x = Conv2D(32,(3,3),activation = 'relu',padding = 'same')
model.add(x)
x = UpSampling2D((2,2))
model.add(x)
x = Conv2D(32,(3,3),activation = 'relu',padding = 'same')
model.add(x)
x = UpSampling2D((2,2))
model.add(x)
decoded = Conv2D(1,(3,3),activation = 'sigmoid',padding = 'same')
model.add(decoded)
model.compile(optimizer = 'adadelta',loss = 'binary_crossentropy')

model.fit(x_train_noisy,x_train,batch_size = batch_size,
          epochs = epoches,verbose = 1,
          validation_data = (x_test_noisy,x_test))

model.save("encode.model")
model.set_weights("encode.weight")
score = model.evaluate(x_test_noisy,x_test,verbose = 0)

for currentEpoch in range(1,10):
    ii = currentEpoch + 1
    dir = 'path' + str(ii)
    prevdir = 'path' + str(currentEpoch)
    if not os.path.isdir(dir):
        print("mkdir:" +dir)
        os.mkdir()
    model.fit(x_train_noisy,x_train,batch_size = batch_size,
          epochs = epoches,verbose = 1,
          validation_data = (x_test_noisy,x_test))
    model.save(dir+'\\encode.model')
    model.save_weights(dir+'\\encode.weight')
    index = 0
    image1 = x_test_noisy[index]
    image2 = x_test[index]
    result = model.predict(image1.reshape(1,28,28,1))
    result = result.reshape(28,28,1)
    result *= 255
    cv2.imwrite(dir+'\\result001.png',result)
    image1 = image1.astype('float32')
    image2 = image2.astype('float32')
    image1 *= 255
    image2 *= 255
    image1 = image1.reshape(28,28,1)
    image2 = image2.reshape(28,28,1)
    noise = X_test[index] + 0.5*np.random.normal(loc = 0.0,scale = 100.0,size = X_train[index].shape)
    noise = noise.reshape(28,28,1)
    cv2.imwrite(dir+'\\noise001.png',noise)
    cv2.imwrite(dir+'\\clean001.png',image2)
















