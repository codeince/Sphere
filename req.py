import requests

response = requests.post('http://localhost:8000/api/generate_answer', params={'question': 'Привет'})



print(response.url)