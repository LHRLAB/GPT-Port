# GPT-Port
GPT-Port: a Flask-based Tool for GPT Port Building with External Jump Server.

## Step 1: Install Dependencies
```
pip install -r requirements.txt
```
## Step 2: Build GPT-Port
### 2.1 Change OpenAI API Key
Change "```your openai api key```" in ```openai.api_key="your openai api key"``` to your openai api key in the 4th line of "GPT_USE.py".
### 2.2 Build GPT-Port
You can build GPT-Port in External Jump Server which can access to openai service.
```
nohup python main.py &
```
After successful start, remember the Process Id [PID] for end the service by kill [PID]  later.
### 2.3 Check Public IP Address
You need to check what your public IP address [PublicIP] is in case you want to use GPT-Port service on other servers later.
```
curl ipinfo.io/ip
```
## Step 3: Use GPT-Port
You can use your GPT service on your internal servers that have access to your Flask-based GPT-Port but not to the OpenAI service with "use_route.py".
### 3.1 Change Public IP
Change "```yourip```" in ```url = 'http://yourip:2023/'``` to your Public IP ([PublicIP] in Step 2.3) in the 3th line of "use_route.py".
### 3.2 Use GPT-Port Service
You can use the function "GPT" in "use_route.py" to get the equivalent OpenAI api service by simply entering the "input" and "model" name. 

For example:

ChatGPT Service: 
```output = GPT(input="What is ChatGPT", model='gpt-3.5-turbo')``` 

GPT4 Service: 
```output = GPT(input="What is ChatGPT", model='gpt-4')``` 


