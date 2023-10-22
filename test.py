import joblib
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer



# Load the trained model using joblib
loaded_model = joblib.load('sentiment_model.pkl')
tokenizer = joblib.load('tokenizer.pkl')

# New text data to test the model
new_text = ""
while new_text !="stop the program":
    new_text = [input("Enter the text you want to analyse: ")]
    # Tokenize and pad the new text data (assuming tokenizer and max_sequence_length are defined as before)
    new_text_sequences = tokenizer.texts_to_sequences(new_text)
    new_text_padded = pad_sequences(new_text_sequences, maxlen=2000)

    # Make predictions using the loaded model
    predictions = loaded_model.predict(new_text_padded)

    # Print the predictions
    if predictions == 0:
         print("Predictions: neutral" )
    if predictions == 1:
         print("Predictions: positive")
    if predictions == 2:
         print("Predictions: negative")