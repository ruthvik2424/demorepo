import os.path
import librosa
import numpy as np
from keras.models import Sequential, model_from_json
from flask import Flask, request
import base64
import tempfile

app = Flask(__name__)

# check if the model file exists
model_file = 'stutter_detection_modela.h5'
if not os.path.isfile(model_file):
    raise Exception("Model file does not exist")

# load the model architecture from a file
json_file = open('stutter_detection_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

# create the model from the loaded architecture
loaded_model = model_from_json(loaded_model_json)

# load the saved model weights into the model
loaded_model.load_weights(model_file)

# compile the model
loaded_model.compile(optimizer='adam', loss='binary_crossentropy')


@app.route('/process', methods=['POST'])
def post():
    # Get the Base64-encoded audio data from the request body
    data = request.json
    base64Audio = data['audioData']

    # Decode the Base64-encoded audio data
    audioBytes = base64.b64decode(base64Audio)

    # Save the audio data as a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as audio_file:
        audio_file.write(audioBytes)
        audio_path = audio_file.name

    # Process the audio data as needed
    def extract_features(audio_path):
        signal, sr = librosa.load(audio_path, sr=44100)
        mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=20)
        # calculate the mean of each MFCC coefficient
        features = np.mean(mfcc_features, axis=1)
        return features

    # extract features from the audio file to be predicted
    features = extract_features(audio_path)

    # predict the class probability of the audio file
    probabilities = loaded_model.predict(np.array([features]))
    predicted_class = round(probabilities[0][0])

    # calculate the accuracy of the prediction
    test_X = np.array([features])
    test_y = np.array([1])  # provide the true label of the audio file
    evaluation_result = loaded_model.evaluate(test_X, test_y)
    loss = evaluation_result
    accuracy = evaluation_result
    # its Working

    # Return the results as a JSON response
    result = {
        'message': 'Audio data received and processed',
        'predicted_class': int(predicted_class),
        'probability': float(probabilities[0][0]),
        'accuracy': float(accuracy)
    }
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
