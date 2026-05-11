
import requests
import json 



def emotion_detector(text_to_analyze: str): 

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": f"{text_to_analyze}" } }
    response = requests.post(url = url, headers = headers, json = input_json)

    text_dict = json.loads(response.text)
    
    emotions =  text_dict["emotionPredictions"][0]["emotion"]

    dominant_emotion = ""
    dominant_emotion_score = 0 

    for k, v in emotions.items(): 
        if v > dominant_emotion_score: 
            dominant_emotion = k 
            dominant_emotion_score = v 

    return_str = "{\n"

    for k, v in sorted(emotions.items()): 

        return_str += f"'{k}' : {v}\n"
    
    return_str += f"'dominant_emotion' : '{dominant_emotion}'\n"
    return_str += "}"

    
    return return_str 



