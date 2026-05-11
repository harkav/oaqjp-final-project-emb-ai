from EmotionDetection.emotion_detector import emotion_detector
import unittest 

class TestOutput(unittest.TestCase):

    def test_output(self): 

        s_dict = emotion_detector("I am glad this happened")
        assert s_dict["dominant_emotion"] == "joy"

        s_dict = emotion_detector("I am really mad about this")
        assert s_dict["dominant_emotion"] == "anger"
        
        s_dict = emotion_detector("I feel disgusted hearing about this")
        assert s_dict["dominant_emotion"] == "disgust"

        s_dict = emotion_detector("I am so sad about this")
        assert s_dict["dominant_emotion"] == "sadness"

        s_dict = emotion_detector("I am really afraid that this will happen")
        assert s_dict["dominant_emotion"] == "fear"

if __name__ == "__main__": 
    unittest.main()