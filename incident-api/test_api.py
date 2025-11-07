**test_api.py**
```python
import requests
import json

BASE_URL = "http://localhost:8000"

# Создание инцидента
incident_data = {
    "description": "Самокат №123 не в сети",
    "source": "operator"
}

response = requests.post(f"{BASE_URL}/incidents/", json=incident_data)
print("Создан инцидент:", response.json())

# Получение списка
response = requests.get(f"{BASE_URL}/incidents/")
print("Все инциденты:", response.json())

# Обновление статуса
if response.json():
    incident_id = response.json()[0]["id"]
    update_data = {"status": "in_progress"}
    response = requests.patch(f"{BASE_URL}/incidents/{incident_id}", json=update_data)
    print("Обновленный инцидент:", response.json())
