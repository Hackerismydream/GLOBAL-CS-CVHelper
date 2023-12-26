"""
定义了多个Pydantic模型类，每个类对应数据库中的一个表格或关联关系。

UniversityBase、ProBase、ConBase和ApplicationNoteBase定义了基本的字段。

UniversityCreate、ProCreate、ConCreate和ApplicationNoteCreate用于在创建新记录时使用，继承自基本模型并无需额外字段。

University、Pro、Con和ApplicationNote是与数据库中记录对应的模型，在基本模型的基础上添加了id字段，并使用orm_mode = True配置项启用了ORM模式，使其可以直接与SQLAlchemy模型交互。

UniversityWithPros、UniversityWithCons和UniversityWithApplicationNotes是扩展模型，用于在获取University记录时包含其关联的Pro、Con和ApplicationNote数据。
"""
from pydantic import BaseModel
from typing import List

class UniversityBase(BaseModel):
    name: str
    duration: str
    language: str
    degree_type: str
    internship_required: str
    thesis_required: str
    scholarship: str
    other_info: str

class UniversityCreate(UniversityBase):
    pass

class University(UniversityBase):
    id: int

    class Config:
        orm_mode = True

class ProBase(BaseModel):
    pro: str

class ProCreate(ProBase):
    pass

class Pro(ProBase):
    id: int
    university_id: int

    class Config:
        orm_mode = True

class ConBase(BaseModel):
    con: str

class ConCreate(ConBase):
    pass

class Con(ConBase):
    id: int
    university_id: int

    class Config:
        orm_mode = True

class ApplicationNoteBase(BaseModel):
    note: str

class ApplicationNoteCreate(ApplicationNoteBase):
    pass

class ApplicationNote(ApplicationNoteBase):
    id: int
    university_id: int

    class Config:
        orm_mode = True

class UniversityWithPros(University):
    pros: List[Pro] = []

class UniversityWithCons(University):
    cons: List[Con] = []

class UniversityWithApplicationNotes(University):
    application_notes: List[ApplicationNote] = []