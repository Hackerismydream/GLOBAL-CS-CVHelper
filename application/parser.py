"""
A module to parse resume PDF files and convert them into JSON format using GPT-3.

This module provides a ResumeJsonParser class that can be used to convert
resume PDF files into JSON format. The conversion is performed using the GPT-3
language model provided by the OpenAI API.
"""
import re
import PyPDF2
from application.prompts import PARSER_PROMPT
from application.utils import OpenAIConfig, query_ai


class ResumeJsonParser:
    """解析简历PDF文件并使用GPT-3将其转换为JSON格式的类。"""
    def __init__(self, config: OpenAIConfig = OpenAIConfig(), prompt: str = PARSER_PROMPT):
        """
        初始化ResumeJsonParser并指定配置。
        Args:
            config (OpenAIConfig): OpenAI API配置。
            prompt (str): GPT-3的自定义提示。
        """
        self.config = config
        self.prompt = prompt

    def pdf2json(self, pdf_path: str):
        """
        把PDF简历文件转换成JSON格式。

        Args:
            pdf_path (str): PDF简历文件的路径。

        Returns:
            dict: 简历的JSON表示。
        """
        pdf_str = self.pdf2str(pdf_path)
        json_data = self.__str2json(pdf_str)
        return json_data

    def __str2json(self, pdf_str: str):
        """
        将简历字符串使用GPT-3转换为JSON表示。

        Args：
            pdf_str（str）：简历字符串。

        Returns：
            dict：简历的JSON表示。
        """
        prompt = self.__complete_prompt(pdf_str)
        return query_ai(self.config, prompt)

    def __complete_prompt(self, pdf_str: str) -> str:
        """
        通过将简历字符串附加到初始提示来创建完整提示。
        Args：
            pdf_str（str）：简历字符串。
        Returns：
            str：完整提示。
        """
        return self.prompt + pdf_str

    def pdf2str(self, pdf_path: str) -> str:
        """
        将PDF文件转换为纯文本字符串。

        Args：
            pdf_path（str）：PDF文件的路径。

        Returns：
            str：表示PDF内容的纯文本字符串。
        """
        with open(pdf_path, "rb") as pdf_file:
            pdf = PyPDF2.PdfReader(pdf_file)
            pages = [self.__format_pdf(p.extract_text()) for p in pdf.pages]
            return "\n\n".join(pages)

    def __format_pdf(self, pdf_str: str) -> str:
        """
        通过应用模式替换来清理和格式化PDF文本字符串。

        Args：
            pdf_str（str）：原始PDF文本字符串。

        Returns：
            str：清理和格式化的PDF文本字符串。
        """
        pattern_replacements = {
            r'\s[,.]': ',',
            r'[\n]+': '\n',
            r'[\s]+': ' ',
            r'http[s]?(://)?': ''
        }

        for pattern, replacement in pattern_replacements.items():
            pdf_str = re.sub(pattern, replacement, pdf_str)

        return pdf_str
