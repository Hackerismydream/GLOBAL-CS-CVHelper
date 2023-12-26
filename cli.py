"""
提供一个命令行接口，用于将PDF简历文件转换为JSON格式，以及根据简历内容生成面试问题，并根据简历文件内容生成留学推荐项目。

该脚本提供了三个命令：
- `json`：将给定的PDF简历文件转换为JSON格式。
- `q`：根据给定的PDF简历文件的内容生成面试问题。
- `g`：根据给定的PDF简历文件的内容生成CS留学推荐项目。
"""

import typer
from rich import print as pprint
from rich.progress import Progress, SpinnerColumn, TextColumn
from application.interview import InterviewQuestionMaker
from application.parser import ResumeJsonParser

app = typer.Typer()

json_parser: ResumeJsonParser = ResumeJsonParser()
question_maker: InterviewQuestionMaker = InterviewQuestionMaker()


@app.command()
def json(file_path: str):
    """
    将PDF简历文件转换为JSON格式。

    Args：
        file_path（str）：PDF简历文件的路径。
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        pprint(json_parser.pdf2json(file_path))


@app.command("q")
def question(file_path: str):
    """
    根据PDF简历文件的内容生成面试问题。

    Args：
        file_path（str）：PDF简历文件的路径。
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        pprint(question_maker.create_questions(file_path))

@app.command("g")
def global_make(file_path: str):
    """
    根据PDF简历文件的内容生成CS留学推荐项目。

    Args：
        file_path（str）：PDF简历文件的路径。
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        pprint(question_maker.make_global(file_path))

if __name__ == "__main__":
    app()
