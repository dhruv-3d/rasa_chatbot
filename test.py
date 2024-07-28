import requests

data = {
  "sender": "test_user",
  "message": "Tell me about AMTICs."
}

response = requests.post('http://localhost:5005/webhooks/rest/webhook', json=data)
print(response.status_code)
print(response.json()[0]['text'])