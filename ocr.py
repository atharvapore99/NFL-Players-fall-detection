import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split


train_data=pd.read_csv("train.csv")
test_data=pd.read_csv("test.csv")



#data preprocessing

y=train_data["label"]
X=train_data.drop(["label"], axis=1)

X_test=test_data

#splitting data
X_train, X_val, y_train, y_val=train_test_split(X, y, test_size=0.2, random_state=42)

#normalising the data
X_train=X_train/255
X_val=X_val/255
X_test=X_test/255

#One hot encoding
y_train=to_categorical(y_train)
y_val=to_categorical(y_val)

#reshaping data
X_train=X_train.values.reshape((-1, 28, 28))
X_val=X_val.values.reshape((-1, 28, 28))
X_test=X_test.values.reshape((-1, 28, 28))



#creating the neural network model
model=Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(256, activation="relu"))
model.add(Dense(128, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.summary()



#fitting the model
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=100, batch_size=100, validation_split=0.3, verbose=1)