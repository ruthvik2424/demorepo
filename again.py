import librosa
import numpy as np
from keras.models import Sequential, model_from_json
from fastapi import FastAPI

app = FastAPI()

# Define the function to extract features from an audio file
def extract_features(audio_path):
    signal, sr = librosa.load(audio_path, sr=44100)
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=20)
    features = np.mean(mfcc_features, axis=1) # Calculate the mean of each MFCC coefficient
    return features

# Load the model architecture from a file
json_file = open('stutter_detection_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

# Create the model from the loaded architecture
loaded_model = model_from_json(loaded_model_json)

# Load the saved model weights into the model
loaded_model.load_weights("stutter_detection_modela.h5")

@app.post('/process')
async def process_audio(audio_data: dict):
    # Get the Base64-encoded audio data from the request body
    base64_audio = audio_data['audioData']
    # TODO: Convert the Base64 audio data to a file and save it locally

    # Extract features from the audio file to be predicted
    audio_file = r'E:\\\Telegram\\\Stutter9.mp3'

    features = extract_features(audio_file)

    # Predict the class probability of the audio file
    probabilities = loaded_model.predict(np.array([features]))
    predicted_class = round(probabilities[0][0])

    # Return the predicted result
    if predicted_class == 0:
        return {"result": "The audio file is normal", "probability": float(1 - probabilities[0][0])}
    else:
        return {"result": "The audio file contains stuttering", "probability": float(probabilities[0][0])}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
