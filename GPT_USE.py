import openai
openai.api_key="your openai api key"

def ask_conversation(conversation,model="gpt-3.5-turbo"):
    got_result = False
    num = 0
    while not got_result:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=conversation,
                temperature=0
            )
            answer = response['choices'][0]['message']['content']
            return answer
        except Exception as e:
            if num >= 3:
                got_result = True
            print(e)
            return False






