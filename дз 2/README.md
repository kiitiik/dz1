# API для классификации текста

Этот проект предоставляет API для классификации текста на основе модели BERT.

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/kiitiik/dz1
   cd your-repo
ссылка для установки модели https://disk.yandex.ru/d/7NB7HSP7lK0cFA
##Установите зависимости:
pip install -r requirements.txt
##Запустите сервер:
uvicorn app:app --reload
Пример запроса к API:


curl -X POST "http://127.0.0.1:8000/predict/" -H "Content-Type: application/json" -d '{"text": "у пациента головная боль"}'

Ответ:

{
    "text": "у пациента головная боль",
    "predicted_label": "лёгкое"
}
