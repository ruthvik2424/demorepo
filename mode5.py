import librosa
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

# define the function to extract features from an audio file
def extract_features(audio_path):
    signal, sr = librosa.load(audio_path, sr=44100)
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=20)
    features = np.mean(mfcc_features, axis=1) # calculate the mean of each MFCC coefficient
    return features

# define the function to create the machine learning model
def create_model():
    model = Sequential()
    model.add(Dense(64, input_dim=20, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# load the dataset and extract features from all audio files
normal_files = ['Normal1.mp3', 'Normal2.mp3', 'Normal3.mp3', 'Normal4.mp3','Normal5.mp3']
stutter_files = ['Stutter1.mp3', 'Stutter2.mp3', 'Stutter3.mp3', 'Stutter4.mp3','Stutter5.mp3']
X = []
y = []
for file in normal_files:
    X.append(extract_features(file))
    y.append(0)
for file in stutter_files:
    X.append(extract_features(file))
    y.append(1)
X = np.array(X)
y = np.array(y)

# create and train the machine learning model
model = create_model()
model.fit(X, y, epochs=100, batch_size=32)

# save the model to a file
model.save("stutter_detection_modela.h5")

# save the model architecture to a file
model_json = model.to_json()
with open("stutter_detection_model.json", "w") as json_file:
    json_file.write(model_json)
