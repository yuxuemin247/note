数据库中的每一个语句必须在事务中运行,即使事务仅仅包括一个语句

大多数的数据库都有`AUTOCOMMIT`设置,

- 装饰器

```
@transaction.atomic  # 开启事务，当方法执行完以后，自动提交事务
def xxx(request):
	with connection.cursor() as cursor:
		cursor.excute("xxxxx")
		cursor.excute("xxxxx")
直接加在视图函数上,里面不管是ORM,mysql都会起作用 ..,出现异常全部回滚
```

- with 用法

```
from django.db import transaction
def viewfunc(request):
	obj1.save()
    # with内部的这些代码会在一个事务中执行
    with transaction():
	    obj2.delete()
	    obj3.save()
```

-   使用with还语句可以限定事务的具体作用范围

  ```
  from django.db import transaction
  def viewfunc(request):
  	obj1.save()
      # with内部的这些代码会在一个事务中执行
      with transaction():
  	    obj2.delete()
  		save_id = transaction.savepoint()  # 创建保存点,记录当前的状态
  	    obj3.save()
  	    try:
  	    	obj4.save()
  	    except Exception:
  	    	transaction.savepoint_rollback(save_id)   # 如果obj4操作失败，可以回滚到保存点obj2.save()以后。,即使obj4失败，obj2.save()还可以继续提交
  	   
  		transaction.savepoint_commit(save_id)   # 这条语句可以控制提交从保存点到当前状态的所有数据库事务操作
  ```


django默认下

```
def xxx(request):
	with connection.cursor() as cursor:
    	cursor.execute(  )                      
        cursor.execute()
下面失败不会影响下面的
```

