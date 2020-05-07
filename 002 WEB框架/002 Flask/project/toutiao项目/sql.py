#使用原生的Sql
#使用engine, engine使用connectionpooling连接数据库，然后通过Dialect执行语句
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:123456@182.92.7.134:3306/zhoujian')
result = engine.execute('select *  from blog_tag')
# with engine.begin() as conn:
#     conn.execute('insert into blog_tag (name)  values ("qqqq")')
print(result.fetchall())