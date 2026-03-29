from langchain_community.chat_models import ChatZhipuAI
import os
import dotenv

dotenv.load_dotenv()


os.environ["ZHIPUAI_API_KEY"]=os.getenv("ZHIPUAI_API_KEY")
os.environ["ZHIPUAI_BASE_URL"]=os.getenv("ZHIPUAI_BASE_URL")


#使用环境变量的方式
chat_model = ChatZhipuAI(
    model_name="glm-4",
    api_key = os.environ["ZHIPUAI_API_KEY"],
    base_url = os.environ["ZHIPUAI_BASE_URL"]
    )

#调用模型
response = chat_model.invoke("什么是langchain")

print(response.content)