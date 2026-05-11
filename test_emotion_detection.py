from EmotionDetection.emotion_detector import emotion_detector
import pytest 


def make_dict(string): 
    return_dict = {}
    for l in string.split("\n"): 
        maybe_line = l.split(":")
        if len(maybe_line) > 1: 
            key, val = maybe_line[0].strip(), maybe_line[1].strip()
            return_dict[key] = val
    return return_dict

def test_output(): 

    string = emotion_detector("I am glad this happened")
    s_dict = make_dict(string)
    print(s_dict)
    assert s_dict["'dominant_emotion'"] == "'joy'"


    string = emotion_detector("I am really mad about this")
    s_dict = make_dict(string)
    assert s_dict["'dominant_emotion'"] == "'anger'"

    
    string = emotion_detector("I feel disgusted hearing about this")
    s_dict = make_dict(string)
    assert s_dict["'dominant_emotion'"] == "'disgust'"

    string = emotion_detector("I am so sad about this")
    s_dict = make_dict(string)
    assert s_dict["'dominant_emotion'"] == "'sadness'"

    string = emotion_detector("I am really afraid that this will happen")
    s_dict = make_dict(string)
    assert s_dict["'dominant_emotion'"] == "'fear'"


