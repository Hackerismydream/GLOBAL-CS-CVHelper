"""
定义了一些数据库连接的配置
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 数据库连接配置
SQLALCHEMY_DATABASE_URI = (
    "mysql+pymysql://root:123456@localhost/global_u?charset=utf8mb4"
    #                用户:密码@服务器/数据库?参数
)

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 声明基类
Base = declarative_base()