import requests

# URL JSON-файла
url = "http://localhost:8085/data.json"

# Выполнение HTTP-запроса и получение содержимого файла
response = requests.get(url)
data = response.json()

# Функция для поиска значения "value" по "id"
def find_value_by_id(data, target_id):
    if isinstance(data, dict):
        if "id" in data and str(data["id"]) == target_id:
            return data.get("Value")
        for key, value in data.items():
            result = find_value_by_id(value, target_id)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_value_by_id(item, target_id)
            if result is not None:
                return result

# Использование функции для поиска значения для "id": 60
target_id = "60"
value = find_value_by_id(data, target_id)

# Проверка результата
if value is not None:
    print(f"Значение для 'id': {target_id} равно {value}")
else:
    print(f"Значение для 'id': {target_id} не найдено.")
