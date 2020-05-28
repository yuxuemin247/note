一、models

```
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()
engine = create_engine(
    "postgresql://postgres:password@39.100.114.253:54321/test1",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

class Users(Base):
    __tablename__ = 'users'  # 数据库表名称
    id = Column(Integer, primary_key=True)  # id 主键
    name = Column(String(32), index=True, nullable=False)  # name列，索引，不可为空
    age = Column(Integer)
    email = Column(String(32), unique=True)
    #datetime.datetime.now不能加括号，加了括号，以后永远是当前时间
    ctime = Column(DateTime, default=datetime.datetime.now)
    extra = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'), #联合唯一
        Index('ix_id_name', 'name', 'email'), #索引
    )

class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    # hobby指的是tablename而不是类名
    hobby_id = Column(Integer, ForeignKey("hobby.id"))
    #加一个字段,该字段不会再数据库中生成
    # 跟数据库无关，不会新增字段，只用于快速链表操作
    # 类名，backref用于反向查询
    hobby = relationship('Hobby', backref='pers')


#orm不能创建数据库,只能创建表
def init_db():
    """
    根据类创建数据库表
    """
    Base.metadata.create_all(engine)

def drop_db():
    """
    根据类删除数据库表
    """

    Base.metadata.drop_all(engine)
    
#多对多
class Boy2Girl(Base):
    __tablename__ = 'boy2girl'
    id = Column(Integer, primary_key=True, autoincrement=True)
    girl_id = Column(Integer, ForeignKey('girl.id'))
    boy_id = Column(Integer, ForeignKey('boy.id'))
    

class Girl(Base):
    __tablename__ = 'girl'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Boy(Base):
    __tablename__ = 'boy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    # 与生成表结构无关，仅用于查询方便,放在哪个单表中都可以
    girls = relationship('Girl', secondary='boy2girl', backref='boys')

if __name__ == '__main__':
    #drop_db()
    init_db()
```

二、增删改查

```
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Person,Hobby
engine = create_engine(
    "postgresql://postgres:password@39.100.114.253:54321/test1",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
Connection = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个Connection
con = Connection()
```

```
#增
#单表新增数据
obj1 = Users(name="lqz")
con.add添加数据
con.add(obj1)

con.add_all([
	Users(name="lqzee"),
    Users(name="egon"),
])
# 提交事务,	关闭session，其实是将连接放回连接池
con.commit()
```

```
#修
ret=con.query(Users).filter(Users.id > 3).update({"name" : "lqz"})

con.query(Users).filter(Users.id > 3).update({Users.name: Users.name + "099"}, synchronize_session=False)
con.query(Users).filter(Users.id > 0).update({"age": Users.age + 1}, synchronize_session="evaluate")
con.commit()
```

```
#删除
ret=con.query(Users).filter(Users.id>2).delete()
#filter内传的是条件
ret=con.query(Users).filter(Users.id==5).delete()
con.commit()
```

```
#查
ret=con.query(Users).order_by(Users.name.desc(),Users.age.asc()).all()
# Users.name.label('newname') 重命名
ret=con.query(Users.name.label('newname')).all()

#一对多关系的查询
p=con.query(Person).filter_by(name='lqz').first()
print(p)
print(p.hobby.caption)

h=con.query(Hobby).filter_by(caption='人妖').first()
print(h.pers)
for p in h.pers:
    print(p.name)

ret=con.query(Hobby,Person).filter(Hobby.id==Person.hobby_id).all()
#其他范围
Users.id.in_([1,3,4])
Users.id.between(1, 3)
~Users.id.in_([1,3,4]
```

- 线程安全

  ```
  engine = create_engine(
      "postgresql://postgres:password@39.100.114.253:54321/test1",
      max_overflow=0,  # 超过连接池大小外最多创建的连接
      pool_size=5,  # 连接池大小
      pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
      pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
  )
  Session = sessionmaker(bind=engine)
  #scoped_session类并没有继承Session,但是却又它的所有方法
  session = scoped_session(Session)
  
  
  session.add(obj1)
  # 提交事务
  session.commit()
  # 关闭session
  session.close()
  ```

  