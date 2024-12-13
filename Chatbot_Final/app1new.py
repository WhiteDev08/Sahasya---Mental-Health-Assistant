import nltk
# Ensure 'punkt' tokenizer is downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Downloading NLTK punkt tokenizer...")
    nltk.download('punkt')
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import random
import json
import pickle
import numpy as np
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
#Disable GPU
import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')

# Set base directory for loading files relative to app1new.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Load resources using relative paths
try:
    intents = json.loads(open(os.path.join(base_dir, 'intents.json')).read())
    words = pickle.load(open(os.path.join(base_dir, 'updated_wordsv6.pkl'), 'rb'))
    classes = pickle.load(open(os.path.join(base_dir, 'updated_classesv6.pkl'), 'rb'))
    model = load_model(os.path.join(base_dir, 'chatbot_model.h5'))
    
    # Compile the loaded model to avoid warnings
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
except FileNotFoundError as e:
    print(f"File not found: {e}")
    raise

# Chatbot Functions
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.75
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]
    return return_list

def get_response(intents_list, intents_json):
    if not intents_list or float(intents_list[0]['probability']) < 0.75:
        # Return a fallback response if no intent has sufficient confidence
        for i in intents_json['intents']:
            if i['tag'] == "fallback":
                return random.choice(i['responses'])
    
    # Otherwise, return a response based on the predicted intent
    tag = intents_list[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "I'm here to listen, but I didn't understand that."

def chatbot_response(user_message):
    ints = predict_class(user_message)
    return get_response(ints, intents)


print("Length of words array:", len(words))
