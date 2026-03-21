from zhipuai import ZhipuAI 
import os
from dotenv import load_dotenv,find_dotenv

_=load_dotenv(find_dotenv())
client = ZhipuAI(api_key=os.getenv("ZHIPUAI_API_KEY"))
def get_completion(prompt, model="glm-4"):
    response = client.chat.completions.create(  # 新的调用方式
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    
    return response.choices[0].message.content  # 访问方式略有变化


def get_completion_from_messages(messages, model="glm-4", temperature=0):
    response = client.chat.completions.create(  # 新的调用方式
        model=model,
        messages=messages,
        temperature=temperature
    )
    
    return response.choices[0].message.content  # 访问方式略有变化
