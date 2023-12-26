"""
用SQLAlchemy库来定义数据库表的结构和关系。它定义了三个表：University、Pro和Con，以及一个名为ApplicationNote的表。

University表表示申请的项目，包含了以下列：
id：主键，用于唯一标识每个项目。
name：大学名称。
duration：课程持续时间。
language：教授语言。
degree_type：学位类型。
internship_required：是否需要实习。
thesis_required：是否需要论文。
scholarship：奖学金信息。
other_info：其他信息。
pros：与该大学相关的优点列表。
cons：与该大学相关的缺点列表。
application_notes：与该大学相关的申请注意事项列表。

Pro表表示大学的优点，包含了以下列：
id：主键，用于唯一标识每个优点。
university_id：外键，与University表中的id列相关联，表示该优点所属的项目。
pro：优点的描述。

Con表表示大学的缺点，包含了以下列：
id：主键，用于唯一标识每个缺点。
university_id：外键，与University表中的id列相关联，表示该缺点所属的项目。
con：缺点的描述。

ApplicationNote表表示大学的申请注意事项，包含了以下列：
id：主键，用于唯一标识每个申请注意事项。
university_id：外键，与University表中的id列相关联，表示该申请注意事项所
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from model.db_config import Base

class University(Base):
    __tablename__ = 'universities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    duration = Column(String(50))
    language = Column(String(50))
    degree_type = Column(String(50))
    internship_required = Column(String(50))
    thesis_required = Column(String(50))
    scholarship = Column(String(255))
    other_info = Column(Text)
    pros = relationship('Pro', backref='university')
    cons = relationship('Con', backref='university')
    application_notes = relationship('ApplicationNote', backref='university')

class Pro(Base):
    __tablename__ = 'pros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    university_id = Column(Integer, ForeignKey('universities.id'))
    pro = Column(String(255))

class Con(Base):
    __tablename__ = 'cons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    university_id = Column(Integer, ForeignKey('universities.id'))
    con = Column(String(255))

class ApplicationNote(Base):
    __tablename__ = 'applicationnotes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    university_id = Column(Integer, ForeignKey('universities.id'))
    note = Column(Text)