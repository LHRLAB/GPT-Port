import requests
# Get yourip: curl ipinfo.io/ip
url = 'http://yourip:2023/'

def GPT(input, model):
    if model == 'gpt-3.5-turbo':
        json={
            'conversation': [
                {"role": "system", "content": ""},
                {"role": "user", "content": input},
                ],
            'model': 'gpt-3.5-turbo',
        }
    elif model == 'gpt-4':
        json={
            'conversation': [
                {"role": "system", "content": ""},
                {"role": "user", "content": input},
                ],
            'model': 'gpt-3.5-turbo',
        }        
    response = requests.post(url+'GPT_conversation', json=json)
    assert response.status_code == 200
    output=response.json()['data']
    return output

output = GPT(input="What is ChatGPT", model='gpt-3.5-turbo')
print(output)
