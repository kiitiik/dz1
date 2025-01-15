import pytest
from transformers import BertForSequenceClassification

from app.model import preprocess_text as preprocess_data, predict
from app.app import app
import torch
from fastapi.testclient import TestClient


model_path = "improved_trained_model.pth"
# Инициализируйте модель с правильной архитектурой
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-cased', num_labels=3)
state_dict = torch.load(model_path, map_location=torch.device('cpu'))
model.load_state_dict(state_dict)
model.eval()


def test_preprocess_data():
    input_data = "у пациента головная боль"
    expected_output = "пациента головная боль"  # Скорректируйте ожидаемый результат, если нужно
    assert preprocess_data(input_data) == expected_output

def test_predict():
    input_data = "пациент головная боль"
    result = predict(input_data, model)  # Передаём загруженную модель
    assert isinstance(result, int)  # Если результат - индекс класса
    assert result in [0, 1, 2]  # Классы модели: 0, 1, 2

def test_integration_pipeline():
    input_data = "у пациента головная боль"
    processed_data = preprocess_data(input_data)
    result = predict(processed_data, model)
    assert result in [0, 1, 2]  # Классы модели: 0, 1, 2

def test_regression():
    input_data = "у пациента кашель"
    expected_output = 1  # Например, класс "лёгкое"
    result = predict(preprocess_data(input_data), model)
    assert result == expected_output

client = TestClient(app)

def test_api_predict():
    response = client.post("/predict/", json={"text": "кашель и насморк"})
    assert response.status_code == 200
    result = response.json()
    assert "predicted_label" in result  # Скорректировано для текущего ответа
    assert result["predicted_label"] in ["лёгкое", "серьёзное", "неопределено"]