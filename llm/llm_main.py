import json

from config.log import get_logger
from config.config import Config
from llm.llm import LLM


logger = get_logger()


def sys_prompt(context, question):
    return f"""You are a helpful AI assistant. Use the following pieces of
      context to answer the question at the end. If you don't know the answer, 
      just say you don't know. DO NOT try to make up an answer. If the question 
      is not related to the context, politely respond that you are tuned to only 
      answer questions that are related to the context.  {context}  
      Question: {question} Helpful answer:"""


def chat_response(query):

    config_obj = Config()

    llm_chat = LLM(config_obj.config['BASE_URL'])
    result = llm_chat.chat(query, config_obj.config['LLM_MODEL'])
    data = json.loads(result)['response']

    logger.info(f"response: {data['content']}.")
    return data


def parsed_chat(chat_result):
    # 提取 content 信息
    content = chat_result['content']

    # 分割 <think> 内容和回答部分
    think_content = content.split('</think>')[0].replace('<think>', '').strip()
    response_content = content.split('</think>')[1].strip()

    # # 去掉多余的标记（```json 和 ```）
    # json_content = response_content.strip('```json\n').strip('```').strip()

    # # 解析为 Python 对象（列表）
    # parsed_data = json.loads(json_content)

    return think_content, response_content


def format_response(chat_result):

    think_content, response_content = parsed_chat(chat_result)

    # 将提取的信息存储为 JSON 格式
    output_json = {
        'think_content': think_content,
        'response_content': response_content
    }

    return output_json


# 使用示例
if __name__ == "__main__":
    chat_result = chat_response(query="你是谁？")
    output_json = format_response(chat_result)
    print(output_json['response_content'])
