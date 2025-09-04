import requests

URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze: str):
    """
    Вызывает Watson NLP EmotionPredict и возвращает поле 'text'
    из ответа (как требует задание). Если поля нет, вернёт весь JSON.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        raise ValueError("text_to_analyze must be a non-empty string")

    payload = {"raw_document": {"text": text_to_analyze}}
    try:
        resp = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
    except requests.RequestException as e:
        raise RuntimeError(f"Network error: {e}") from e

    if resp.status_code != 200:
        raise RuntimeError(f"Service error: HTTP {resp.status_code}: {resp.text}")

    data = resp.json()
    return data.get("text", data)  # по требованию задания вернуть атрибут 'text'
