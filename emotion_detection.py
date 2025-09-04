import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str):
    payload = {"raw_document": {"text": text_to_analyze}}
    resp = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    # возвращаем ровно text из ответа
    return data["emotionPredictions"][0]["emotionMentions"][0]["text"]

