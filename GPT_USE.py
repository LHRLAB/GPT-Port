from time import sleep
from log.Logging import *
import openai
openai.api_key="your openai api key"
log = Logger('test','use').getlog()

#GPT_3.5和GPT_4
def ask(prompt,askText,model="gpt-3.5-turbo",pre_use=None,pre_assistant=None):
    #prompt
    conversation = [{'role': 'system', 'content': prompt}]
    #上下文或few-shot
    if pre_use!=None and pre_assistant!=None:
        conversation.append({"role": "user", "content": pre_use})
        conversation.append({"role": "assistant", "content": pre_assistant})
    conversation.append({"role": "user", "content": askText})

    got_result = False
    num=0
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
            log.info(model+'use_error:')
            log.error(str(e))
            sleep(3)
            return False

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
            log.info(model+'use_error:')
            log.error(str(e))
            sleep(3)
            return False
def text_davinci3_5(prompt,engine="text-davinci-003",max_tokens=2500):
    got_result = False
    num=0
    while not got_result:
        try:
            num+=1
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                max_tokens=max_tokens,
                # n=1,#生成文本的数量
                stop=None,#生成文本的停止条件
                temperature=0.0
            )
            # 提取响应中的文本并添加到增强的句子列表中
            enhanced_text = response.choices[0].text.strip()
            return enhanced_text
        except Exception as e:
            if num>=3:
                got_result = True
            print(e)
            log.info(engine+'use_error:')
            log.error(str(e))
            sleep(3)
            return False

def text_3(prompt,engine='text-curie-001',max_tokens=1900):#3的最长token少些
    return text_davinci3_5(prompt,engine=engine,max_tokens=max_tokens)

def exam():
    question="""In how many ways can the letters of the word "PROBLEC" be rearranged to make 7 letter words such that none of the letters repeat?"""
    prompt="""# Write Python Code to solve the following questions. Store your result as a variable named 'ans'."""
    # print(ask(askText=question,prompt=prompt))

    # print(text_davinci3_5(prompt+question))
    print(text_3(prompt+question,engine='text-curie-001'))
    print("next:")
    print(text_3(prompt+question,engine='text-ada-001'))





