import torch
from transformers import BertTokenizer, BertForSequenceClassification
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Настройки
MODEL_PATH = "C:/Users/kit/Desktop/PE/project_root/app/improved_trained_model.pth"
MODEL_NAME = "DeepPavlov/rubert-base-cased"
MAX_LENGTH = 50

# Загрузка необходимых инструментов
stop_words = set(stopwords.words('russian'))
lemmatizer = WordNetLemmatizer()
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

# Предобработка текста
def preprocess_text(text):
    """
    Предобрабатывает текст для подачи в модель.
    :param text: Исходный текст.
    :return: Обработанный текст.
    """
    text = re.sub(r'\d+', '', text)  # Удаление цифр
    text = re.sub(r'[^\w\s]', '', text)  # Удаление пунктуации
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])
    return text.strip()

# Загрузка модели
def load_model(model_path=MODEL_PATH):
    """
    Загружает модель из файла и инициализирует её.
    :param model_path: Путь к файлу сохранённой модели.
    :return: Загруженная модель.
    """
    model = BertForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=3)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Подготовка входных данных
def prepare_inputs(text):
    """
    Преобразует текст в формат, совместимый с моделью.
    :param text: Входной текст.
    :return: Словарь с токенами и масками.
    """
    processed_text = preprocess_text(text)
    encoded = tokenizer.encode_plus(
        processed_text,
        add_special_tokens=True,
        max_length=MAX_LENGTH,
        truncation=True,
        padding='max_length',
        return_attention_mask=True,
        return_tensors="pt"
    )
    return encoded

# Предсказание
def predict(text, model):
    """
    Выполняет предсказание на основе входного текста.
    :param text: Входной текст.
    :param model: Загруженная модель.
    :return: Класс предсказания.
    """
    inputs = prepare_inputs(text)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class