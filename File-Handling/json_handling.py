import json

# Python dictionary to JSON Serialization
# Python dictionary
data = {"name": "Alice", "age": 30, "city": "New York"}
# Serialize to JSON string
json_string = json.dumps(data)
print(json_string)

# Deserialize JSON string to Python object
# JSON string
json_string = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "state": "NY"}}'
# Deserialize JSON string to Python object
python_obj = json.loads(json_string)
print(python_obj)


# Read and deserialize from file
with open("data.json", "r") as f:
    python_obj = json.load(f)
print(python_obj)