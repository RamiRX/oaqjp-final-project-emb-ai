from emotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetection(unittest.TestCase):
    def Test_Emotion_Detection(self):
        #one
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        #two
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')
        #three
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')
        #four
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')
        #five
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')
unittest.main()       

        