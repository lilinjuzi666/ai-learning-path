import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv(".env")


llm=ChatOpenAI(
    openai_api_key=os.getenv("API_KEY"),
    base_url="https://pen.bigmodel.cn/api/paas/v4/",
    model="glm_4"
)

response=llm.invoke("你好，请用一句话介绍一下你自己")

print(response.content)