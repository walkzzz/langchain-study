import os
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

# 获取环境变量示例
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_base_url = os.getenv("OPENAI_BASE_URL")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# 打印部分环境变量值（出于安全考虑，实际项目中不要打印API密钥）
print(f"OPENAI_BASE_URL: {openai_base_url}")
print(f"OLLAMA_BASE_URL: {os.getenv('OLLAMA_BASE_URL')}")

# 检查是否成功加载环境变量
if openai_api_key:
    print("OpenAI API Key 已加载")
else:
    print("未找到 OpenAI API Key")