"""
定义了对数据库的增删改查操作
"""
from sqlalchemy.orm import Session, joinedload
from . import models, schemas

def get_university(db: Session, university_id: int):
    """
    根据id查询项目信息
    :param db:  数据库会话
    :param university_id:  项目id
    :return:  项目信息
    """
    return db.query(models.University).filter(models.University.id == university_id).first()

def get_universities(db: Session):
    """
    查询所有项目信息
    :param db:  数据库会话
    :return:  所有项目信息
    """
    return db.query(models.University).all()

def get_university_with_pros(db: Session, university_id: int):
    """
    根据id查询项目信息，并且查询项目的优点
    :param db:  数据库会话
    :param university_id:  项目id
    :return:  项目信息
    """
    return db.query(models.University).filter(models.University.id == university_id).\
        options(joinedload(models.University.pros)).first()

def get_universities_by_name(db: Session, name: str):
    """
    根据项目名称查询项目信息
    :param db:  数据库会话
    :param name:  项目名称
    :return:  项目信息
    """
    return db.query(models.University).filter(models.University.name == name).all()
# 同样的方式可以查询Pros、Cons和ApplicationNote记录的函数