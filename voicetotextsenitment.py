import time
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.metrics import classification_report,accuracy_score
from nltk.corpus import stopwords
import six.moves.cPickle as pickle
import re
import speech_recognition as sr
# import pyaudio
import traceback
# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
print("loading Voice to Text Sentiment")
# Sample rate is how often values are recorded
sample_rate = 48000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()

# generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)

# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
        print(device_id)
# print(device_id)
def get_vals():
    global pos,neg
    return(pos,neg)

def sample_check():
    with sr.Microphone(device_index=0,sample_rate=sample_rate,chunk_size=chunk_size) as s:
        r.adjust_for_ambient_noise(s)
        print('say some test sentence')
        aud=r.listen(s)
        print('Recognised')
        print('If the recognitiion ended automatically use the current threshold \n else increase the threshold value')

def recog_save():
    with sr.Microphone(device_index=0, sample_rate=sample_rate, chunk_size=chunk_size) as source:
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Recording audio")
        # listens for the user's input
        audio = r.listen(source)
        print("Done ")
        try:
            print("Recognizing")
            text = r.recognize_google(audio)
            print("you said: " + text)
            return (text)
        # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return (None)
        except sr.RequestError as e:
            print("Could not request results from GoogleSpeechRecognitionservice;{0}".format(e))
            return (None)


# from imdbReview import extract_words
def extract_words(sentences):
    result = []
    stop = stopwords.words('english')
    trash_characters = '?.,!:;"$%^&*()#@+/0123456789<>=\\[]_~{}|`'
    trans = str.maketrans(trash_characters, ' '*len(trash_characters))

    for text in sentences:
        text = re.sub(r'[^\x00-\x7F]+',' ', text)
        text = text.replace('<br />', ' ')
        text = text.replace('--', ' ').replace('\'s', '')
        text = text.translate(trans)
        text = ' '.join([w for w in text.split() if w not in stop])

        words = []
        for word in text.split():
            word = word.lstrip('-\'\"').rstrip('-\'\"')
            if len(word)>2 :
                words.append(word.lower())
        text = ' '.join(words)
        result.append(text.strip())
    return result
# Load All Reviews in train and test datasets
f = open('train.pkl', 'rb')
reviews = pickle.load(f)
f.close()

f = open('test.pkl', 'rb')
test = pickle.load(f)
f.close()


# Generate counts from text using a vectorizer.
# There are other vectorizers available, and lots of options you can set.
# This performs our step of computing word counts.
vectorizer = TfidfVectorizer(min_df=5, max_df=0.8,
                            sublinear_tf=True, use_idf=True)
train_features = vectorizer.fit_transform(reviews[0])
test_features = vectorizer.transform(test[0])

# Perform classification with SVM, kernel=linear
classifier_liblinear = svm.LinearSVC()
classifier_liblinear.fit(train_features, reviews[1])
prediction_liblinear = classifier_liblinear.predict(test_features)
# Now we can use the model to predict classifications for our test features.
print(classification_report(test[1], prediction_liblinear))
print("accuracy: {0}".format( accuracy_score(test[1], prediction_liblinear)))
# Compute the error.
#fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
#print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))
pos=0
neg=0
sentence=None
busy=False
def result_of_sentiment_analysis():
    global pos,neg,sentence,busy
    while True:
        try:
            sentences = []
            sentence = recog_save()
            busy=False # just giving a busy here to stop thhe detection eithout getting a google error
            if sentence == "exit":
                print("\033[93mexit program ...\033[0m\n")
                break
            else:
                sentences.append(sentence)
                input_features = vectorizer.transform(extract_words(sentences))
                prediction = classifier_liblinear.predict(input_features)
                if prediction[0] == 1:
                    print("---- \033[92mpositive\033[0m\n")
                    print("I have got here")
                    pos += 1
                    print(f'positive={pos}')
                else:
                    print("---- \033[91mneagtive\033[0m\n")
                    neg += 1
                    print(f'negative={neg}')
        except Exception:
            print('Error occured while Trying to connect to google API')
            traceback.print_exc()
            return

def perform_analysis(string):
    global pos,neg
    sentences = []
    sentences.append(string)
    input_features = vectorizer.transform(extract_words(sentences))
    prediction = classifier_liblinear.predict(input_features)
    if prediction[0] == 1:
        print("---- \033[92mpositive\033[0m\n")
        pos += 1
    else:
        print("---- \033[91mneagtive\033[0m\n")
        neg += 1

def get_Busy():
    global busy
    return busy
# function to send the status of the busy variable to the dbb.py's main thread
# result_of_sentiment_analysis()
# print(f'positive={pos},negative={neg}')
print("Voice to text sentiment model loaded")