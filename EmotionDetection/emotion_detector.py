
import requests
import json 

def emotion_detector(text_to_analyze: str): 

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": f"{text_to_analyze}" } }
    response = requests.post(url = url, headers = headers, json = input_json)

    status_code = response.status_code

    if status_code == 400: 
        return {"anger" : None, "disgust" : None, "fear" : None, "joy": None, "sadness" : None, "dominant_emotion" : None}
    text_dict = json.loads(response.text)
    return_dict = text_dict["emotionPredictions"][0]["emotion"]

    dominant_emotion = "kvakk"
    dominant_emotion_score = -1

    for k, v in return_dict.items(): 
        if v > dominant_emotion_score: 
            dominant_emotion = k
            dominant_emotion_score = v
    
    return_dict["dominant_emotion"] = dominant_emotion

    return return_dict

