import requests

headers = {
    "Content-Type": "application/json",
}

data = {
    'inputs': 'Write a 500 word essay of Kyoto',
    'parameters': {
        'max_new_tokens': 2000,
    },
}

response = requests.post('http://127.0.0.1:8080/generate', headers=headers, json=data)
print(response.json())
# {'generated_text': '\n\nDeep Learning is a subset of Machine Learning that is concerned with the development of algorithms that can'}