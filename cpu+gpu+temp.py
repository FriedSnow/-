import requests

# URL JSON-файла
url = "http://localhost:8085/data.json"

# Выполнение HTTP-запроса и получение содержимого файла
response = requests.get(url)
data = response.json()

# Функция для поиска значения "Value" по "id"
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

# target_id1 - id той части json'a где в Value лежит температура CPU
# target_id2 - то же самое но с GPU

target_id1 = "60"
target_id2 = "92"

cputemp = find_value_by_id(data, target_id1)
gputemp = find_value_by_id(data, target_id2)

# Проверка результата
if cputemp is not None:
    print(f"CPU: {cputemp}, GPU: {gputemp}")
else:
    print("404")
