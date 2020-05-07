#### time            | 时间                 
datetime        | 日期和时间           
calendar        | 日历   



#### 1 获取一个月最后一天

```python
import datetime
def last_day_of_month(any_day):
    '''
    获取一个月中的最后一天
    :param any_day:任意日期
    :return: string
    '''
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return  next_month-datetime.timedelta(days=next_month.day)

data= last_day_of_month(datetime.date(2020,2,15))
print(data)  #2020-02-29
```

##### 2 时间拼接

```python
import datetime
now_day = datetime.datetime.now()
query_day=now_day.replace(day=10).date()
min_query_day = str(query_day) + " 00:00:00"
max_query_day = str(query_day) + " 23:59:59"
print(min_query_day,max_query_day)
#2020-03-10 00:00:00 2020-03-10 23:59:59
```

##### 3 时间转化

```
import time

print(datetime.datetime.now())    #2020-03-12 22:45:01.788028
dt = "20160505202854111"
#转换成时间数组
timeArray = time.strptime(dt, "%Y%m%d%H%M%S%f")
print(timeArray)   
#time.struct_time(tm_year=2016, tm_mon=5, tm_mday=5, tm_hour=20, tm_min=28,

#转换成时间戳
timestamp = time.mktime(timeArray)
print(timestamp)   #1462451334.0
```

#####  4 js获取时间

```
<script>
  function gettime() {
    var date = new Date();
    // 获取当前月份
    var nowMonth = date.getMonth() + 1;
    // 获取当前是几号
    var strDate = date.getDate();
    var strHour = date.getDate();
    // 对月份进行处理，1-9月在前面添加一个“0”
    if (nowMonth >= 1 && nowMonth <= 9) {
       nowMonth = "0" + nowMonth;
    }
    // 对日期进行处理，1-9号在前面添加一个“0”
    if (strDate >= 0 && strDate <= 9) {
       strDate = "0" + strDate;
    }
    // 最后拼接字符串，得到一个格式为(yyyy-MM-dd)的日期
    var nowDate = date.getFullYear()  + nowMonth  + strDate
    return nowDate
}
	var newDate = gettime();
    var beforeDate = berforegettime();
    var reg = '^'+newDate+'[0-9]{20}$'
    var r = alipay_no.match(reg);
    if(r == null){
    console.log('匹配失败')
    }else{
    console.log('匹配成功')
}
<script>

```

