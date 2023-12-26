from typing import List

from fastapi import FastAPI, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from application.interview import InterviewQuestionMaker
from application.utils import OpenAIConfig
from model import schemas, crud
from model.db_config import SessionLocal, engine

question_maker = InterviewQuestionMaker(config=OpenAIConfig(temperature=0.7))

app = FastAPI()
# 配置CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源的跨域请求
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有HTTP头部
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/global/")
async def recommend_project(file: UploadFile):
    """
    通过HTTP POST上传的pdf给出推荐的项目json。

    Args:
        file (UploadFile): The uploaded text file.

    Returns:
        str: The generated interview questions.
    """
    respon = question_maker.make_global(file.file)
    # respon = {
    #     "推荐院校": ["ETH MSCS", "Cambridge ACS", "Cambridge MLMI"],
    #     "推荐理由": [
    #         "您的本科专业为计算机科学，GPA优秀，具有较多的科研经历和实习经历，语言成绩也很出色，适合申请ETH MSCS项目。",
    #         "您的本科专业为计算机科学，GPA优秀，具有较多的科研经历和实习经历，语言成绩也很出色，适合申请Cambridge ACS项目。",
    #         "您的本科专业为计算机科学，GPA优秀，具有较多的科研经历和实习经历，语言成绩也很出色，适合申请Cambridge MLMI项目。"]
    # }
    recommended_programs = respon['推荐院校']
    recommended_resons = respon['推荐理由']
    recommend_project = {}

    db = SessionLocal()
    # 从DB中获取推荐项目的详细信息
    for i in range(len(recommended_programs)):
        university = crud.get_universities_by_name(db, recommended_programs[i])
        info = {}
        for item in university:
            info.update({'项目介绍': {'项目时长': item.duration, '授课语言': item.language, '学位类型': item.degree_type,
                                 '是否强制实习': item.internship_required, '毕业是否需要论文': item.thesis_required,
                                 '奖学金': item.scholarship, '其他信息': item.other_info}})
            pros = []
            cons = []
            for pro in item.pros:
                pros.append(pro.pro)
            for con in item.cons:
                cons.append(con.con)
            info.update({'项目优劣势': {'Pros': pros, 'Cons': cons}})
            notes = []
            for note in item.application_notes:
                notes.append(note.note)
            info.update({'注意事项': {'网申注意事项': notes, '其他注意事项': ['无']}})

        recommend_project.update({recommended_programs[i]: info})

    recommended = {}
    recommended.update({'推荐院校': recommend_project})
    recommended.update({'推荐理由': recommended_resons})


    return recommended

@app.get("/universities/id/{university_id}", response_model=schemas.University)
def get_university(university_id: int, db: Session = Depends(get_db)):
    return crud.get_university(db, university_id)


@app.get("/universities/name/{name}", response_model=List[schemas.University])
def get_universities_by_name(name: str, db: Session = Depends(get_db)):
    return crud.get_universities_by_name(db, name)

@app.post("/questions/")
async def create_questions(file: UploadFile):
    """
    翻译：
    通过HTTP POST上传的文本文件创建面试问题。

    Args:
        file (UploadFile): The uploaded text file.

    Returns:
        str: The generated interview questions.
    """
    answers = question_maker.create_questions(file.file)
    return answers