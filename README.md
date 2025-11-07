# Incident API Service

Микросервис для учёта инцидентов

# Установить зависимости
pip install -r requirements.txt

# Запустить сервер
uvicorn app.main:app --reload

# Эндпоинты
POST /incidents/ - создать инцидент

GET /incidents/?status=open - получить инциденты с фильтром

PATCH /incidents/{id} - обновить статус инцидента

# Пример

POST /incidents/ {"description": "Самокат не в сети", "source": "operator"}
GET /incidents/?status=open
PATCH /incidents/1 {"status": "in_progress"}
