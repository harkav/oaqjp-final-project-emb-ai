from flask import Flask 
from EmotionDetection.emotion_detector import emotion_detector

app = Flask.app() 




if __name__ == "__main__": 
    app.run() 
