"""
用于管理OpenAI API配置参数的模块。

该模块提供了一个数据类OpenAIConfig，用于存储和管理用于向OpenAI API发出请求所需的配置参数。
OpenAIConfig数据类可用于组织和传递这些参数与API交互的其他类或函数。
"""
import json
import os
from dataclasses import dataclass
import openai

openai.api_key = "ak-TAANh61fQLhLSr7Ea7TvsLLXxh6KRE3htF5Jf16jkb2Au3jx"
openai.api_base = "https://api.nextapi.fun"


@dataclass
class OpenAIConfig:
    """
    用于存储OpenAI API配置参数的数据类。

    Attributes：
        model (str)：要使用的OpenAI模型，默认为“gpt-3.5-turbo”。
        temperature (float)：模型的采样温度，默认为0.0。
        max_tokens (int)：模型响应中的最大令牌数，默认为1000。
        top_p (float)：核心采样参数，控制模型响应的随机性，默认为1。
        frequency_penalty (float)：令牌频率的惩罚，默认为0。
        presence_penalty (float)：令牌存在的惩罚，默认为0。
    """
    model: str = "gpt-3.5-turbo"
    # model: str = "gpt-4-1106-preview"
    temperature: float = 0.0
    max_tokens: int = 2000
    top_p: float = 1
    frequency_penalty: float = 0
    presence_penalty: float = 0


def query_ai(config: OpenAIConfig, prompt: str):
    """
    使用提供的配置和提示查询OpenAI API。

    Args：
        config（OpenAIConfig）：OpenAI API请求的配置参数。
        prompt（str）：要发送到API的提示。

    Returns：
        dict：来自API的解析JSON响应。
        str：如果发生异常，则为错误消息。

    Raises：
        openai.APIError：与OpenAI API相关的异常。
        json.JSONDecodeError：与JSON解码相关的异常。
    """
    try:
        response = openai.ChatCompletion.create(
            model=config.model,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            top_p=config.top_p,
            frequency_penalty=config.frequency_penalty,
            presence_penalty=config.presence_penalty,
            messages=[{"role": "user", "content": prompt}],
        )

        response_str = response.choices[0].message.content.strip()
        print(response_str)
        return json.loads(response_str)

    except openai.APIError as api_exc:
        # Handle exceptions related to the OpenAI API
        return f"API Error: {api_exc}"
    except json.JSONDecodeError as json_exc:
        # Handle exceptions related to JSON decoding
        return f"JSON Decode Error: {json_exc}"
