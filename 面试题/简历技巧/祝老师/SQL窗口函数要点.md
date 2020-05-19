## 窗口函数

### 1. 介绍

- 窗口函数不像聚合函数，聚合函数将参与计算的行合并成一行输出，而窗口函数是将计算出来的结果带回到原来的行上。

  - 聚合函数：sum / min / avg ... + GROUP BY
  - 窗口函数：sum / min / avg / rank ... + OVER (...)
- 窗口函数只能在SELECT和ORDER BY子句中使用，不能在任何其他地方使用，比如GROUP BY、HAVING和WHERE子句
  - 窗口函数必须和over字句配合使用。
  - over 子句包含 PARTITION BY 和 ORDER BY 两部分，分别用来分组和确定组内输出顺序。
  - PARTITION BY和ORDER BY都是可选的。
- 所有的聚合函数都可以作为窗口函数使用

### 2. 语法

```plsql
<窗口函数> 
OVER ([PARTITION BY <列清单>]                      
ORDER BY <排序用列清单>)
```

### 3. 窗口函数

- row_number()
  -   返回分组后的行号。注意到虽然emp_no为9和11的员工，salary相同，但row_number返回的行号仍然连续。
- rank()
  -   返回分组后的行号，但和row_number不同的是，如果对比值重复时，行号重复且会发生间断。
- dense_rank()
  -   返回分组后的行号，但和row_number和rank函数都不同，当对比值重复时行号重复但不间断。
- percent_rank()
  -   返回当前行的相对排名，计算在分组中的比例(rank-1)/(总记录数-1)，需要对比rank函数理解。
- cume_dist()
  -   返回当前行的相对排名：(前面的行数或与当前行相同的行数)/(总行数)
- ntile(分组数量) 
  - 让所有记录尽可以的均匀分布。
- lag(value any [, offset integer [, default any ]]) 
  -   返回偏移值，offset integer是偏移值，正数时前值，负数时后值，没有取到值时用default代替，默认偏移量为0， 默认值为null
- lead(value any [, offset integer [, default any ]])
  -   返回偏移值，offset integer是偏移值，正数时取后值，负数时取前值，没有取到值时用default代替
- first_value(value any)
  -   返回分组第一个值
- last_value(value any)
  -   返回分组最后一个值
- nth_value(value any, nth integer)
  -   返回分组的第n个值，如果没有则为null

### 4. 成绩例子

```sql
-- example table: score 
-- id  subject  name  score

-- 查询时，要多显示一列subject_avg，为此科目所有人的平均成绩，与每个人的成绩做对比：
select *, 
	round(avg("score") over (partition by "exam_id","s_id"),2) as "student_avg" 
	from "score";

-- 查询时，要多显示一列test_avg，为此次考试所有人的平均成绩，与每个人的成绩做对比：
select *, 
	round(avg("score") over (partition by "exam_id"),2) as "exam_avg" 

-- 取此人该科目成绩班上排第几名
select *, 
	avg("score") over (partition by "subject") as "subject_avg", 
	rank() over (partition by "subject" order by "score" desc) as "subject_rank" 
	from "score";
	
-- 
select *, 
	avg("score") over (partition by "exam_id","s_id")
	from "score";

-- 把学生的成绩与本次考试的平均成绩对比
select *, 
	avg("score") over (partition by "exam_id"),
	rank() over (partition by "exam_id" order by "score" desc)
	from "score";

-- # 列出本次考试每个科目的排名
select *, 
	rank() over (partition by "exam_id","obj_id" order by "score" desc)
	from "score";

-- rank() 最适合用来做排名的功能，它是若两人并列第一，那第三个人就排名第三
-- dense_rank() 跟 rank() 的区别是，若两人并列第一，那第三个人紧随其后排名第二
-- row_number() 则单纯是序号，所以不会出现多个人并列的情况。

-- 提取重复的 OVER 变量
-- 如果在 sql 里写了很多重复的 OVER()，可以提取成一个 window 变量，简化代码。
SELECT *, 
    avg("score") OVER win_frame as "subject_avg_score",
    avg("score") OVER win_frame as "subject_avg_score_2",
    avg("score") OVER win_frame as "subject_avg_score_3"
	FROM "score"  
	window win_frame as (PARTITION BY "subject")
```

### 5. 商品例子

```plsql
-- 样例数据表
DROP TABLE IF EXISTS "public"."products";
CREATE TABLE "public"."products" (
    "id" varchar(10) COLLATE "default",
    "name" text COLLATE "default",
    "price" numeric,
    "uid" varchar(14) COLLATE "default",
    "type" varchar(100) COLLATE "default"
)WITH (OIDS=FALSE);

-- 准备数据
INSERT INTO "public"."products" VALUES ('0006', 'iPhone X', '9600', null, '电器');
INSERT INTO "public"."products" VALUES ('0012', '电视', '3299', '4', '电器');
INSERT INTO "public"."products" VALUES ('0004', '辣条', '5.6', '4', '零食');
INSERT INTO "public"."products" VALUES ('0007', '薯条', '7.5', '1', '零食');
INSERT INTO "public"."products" VALUES ('0009', '方便面', '3.5', '1', '零食');
INSERT INTO "public"."products" VALUES ('0005', '铅笔', '7', '4', '文具');
INSERT INTO "public"."products" VALUES ('0014', '作业本', '1', null, '文具');
INSERT INTO "public"."products" VALUES ('0001', '鞋子', '27', '2', '衣物');
INSERT INTO "public"."products" VALUES ('0002', '外套', '110.9', '3', '衣物');
INSERT INTO "public"."products" VALUES ('0013', '围巾', '93', '5', '衣物');
INSERT INTO "public"."products" VALUES ('0008', '香皂', '17.5', '2', '日用品');
INSERT INTO "public"."products" VALUES ('0010', '水杯', '27', '3', '日用品');
INSERT INTO "public"."products" VALUES ('0015', '洗发露', '36', '1', '日用品');
INSERT INTO "public"."products" VALUES ('0011', '毛巾', '15', '1', '日用品');
INSERT INTO "public"."products" VALUES ('0003', '手表', '1237.55', '5', '电器');
INSERT INTO "public"."products" VALUES ('0016', '绘图笔', '15', null, '文具');
INSERT INTO "public"."products" VALUES ('0017', '汽水', '3.5', null, '零食');

-- 给查询出来的数据添加一列序号
select 
	type, name, price, 
	row_number() over 
		(order by price asc) 
		as idx 
	from products ;

-- 在类别(type)内按照价格(price) 升序排列(就是在类别内做排序)
-- 分组排序
select type,name,price,
	row_number() over(PARTITION by type order by price asc) as idx 
	from products ;

-- 在类别(type)内按照价格(price) 升序排列，如何将零食和汽水并列？
SELECT type,name,price,rank() over(partition by type order by price asc) from products;

-- 在类别(type)内按照价格(price) 升序排列，如何将零食和汽水并列？并保持序号不重不少
SELECT type,name,price,dense_rank() over(partition by type order by price asc) from products;

-- 限制序号在0到1之间排序呢？
SELECT type,name,price,percent_rank() over(partition by type order by price asc) from products;

--　限制序号在0~1之间相对排名，
SELECT type,name,price,cume_dist() over(partition by type order by price asc) from products;

-- 限制最大序号为指定数字序号 ntile(val1) 实现
SELECT type,name,price,ntile(2) over(partition by type order by price asc) from products;

-- 在子分类排序的情况下取偏移值：获取到排序数据的每一项的偏移值(向下偏移) , lag(val1,val2,val3) 函数实现
-- 函数lag(val1,val2,val3) 中的三个参数分别为
-- (输出的上一条记录的字段,偏移值,无偏移值的默认值)；
-- 以上这里的偏移值为1，偏移字段为id，无偏移默认值为空('')
SELECT id,type,name,price,lag(id,1,'') over(partition by type order by price asc) as topid from products;

-- 获取分类子项排序中的第一条记录的某个字段的值， first_value(val1) 实现
SELECT id,type,name,price,first_value(name) over(partition by type order by price asc) from products;

-- 向下取分类排序中的最后一条记录的某个字段, last_value(val1)实现
-- 当取分类在最后一条记录的时候 自然排序下不可以在over() 使用排序字段，
-- 不然取得的值为相对于当前记录的值，故这里按价格(price) 升序的时候指定 
-- 排序字段 -> range between unbounded preceding and unbounded following
SELECT id,type,name,price,last_value(name) over(partition by type order by price range between unbounded preceding and unbounded following) from products; 
-- order by type asc ;-- ,price asc;

-- 取得排序字段项目中指定序号记录的某个字段值
SELECT id,type,name,price,nth_value(name,2) OVER(partition by type order by price range between unbounded preceding and unbounded following ) from products;

-- 计算移动平均值
-- 指定框架（汇总范围): 指定框架，将汇总对象限定为了“最靠近的3行”。
-- ROWS 和 PRECEDING 关键字，将框架指定为“截止到之前 ~ 行”，
-- 因此“ROWS 2 PRECEDING" 这样的统计方法称为移动平均
-- PRECEDING 之前
-- FOLLOWING 之后
select "id", "name", "price",
  avg("price") over (
		order by "id" rows 2 preceding) as moving_avg
		from products;

-- 用相邻的上下行计算平均值
SELECT "id", "name", "price",
	AVG ("price") OVER (
		ORDER BY "id" ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
	) AS moving_avg
FROM "products";

-- 窗口函数+聚合函数
select 
    id,type,name,price,
sum(price) over (partition by type) 类别金额合计,
(sum(price) over (order by type))/sum(price) over() 类别总额占所有品类商品百分比,
round(price/(sum(price) over (partition by type rows between unbounded preceding and unbounded following)),3) 子除类别百分比,
rank() over (partition by type order by price desc) 排名,
sum(price) over() 金额总计
from products ORDER BY type,price asc;

-- 为使语句有更好的可读性，窗口条件可以放在from后面 
select 
    id,type,name,price,
    sum(price) over w1 类别金额合计,
    (sum(price) over (order by type))/sum(price) over() 类别总额占所有品类商品百分比,
    round(price/(sum(price) over w2),3) 子除类别百分比,
    rank() over w3 排名,
    sum(price) over() 金额总计
from 
    products 
WINDOW 
    w1 as (partition by type),
    w2 as (partition by type rows between unbounded preceding and unbounded following),
    w3 as (partition by type order by price desc)
ORDER BY 
    type,price asc;
```

### 6. 入职查询

```sql
-- 表结构
DROP TABLE IF EXISTS "public"."enroll";
CREATE TABLE "public"."enroll" (
  "id" int4 NOT NULL,
  "date" date,
  "month" varchar(255) COLLATE "pg_catalog"."default"
);

-- 数据
INSERT INTO "public"."enroll" VALUES (1, '2019-07-01', '201907');
INSERT INTO "public"."enroll" VALUES (2, '2019-09-11', '201909');
INSERT INTO "public"."enroll" VALUES (3, '2019-07-24', '201907');
INSERT INTO "public"."enroll" VALUES (4, '2019-08-14', '201908');
INSERT INTO "public"."enroll" VALUES (5, '2019-09-12', '201909');
INSERT INTO "public"."enroll" VALUES (6, '2019-09-12', '201909');
INSERT INTO "public"."enroll" VALUES (7, '2019-09-20', '201909');
INSERT INTO "public"."enroll" VALUES (8, '2019-09-07', '201909');

ALTER TABLE "public"."enroll" ADD CONSTRAINT "enroll_pkey" PRIMARY KEY ("id");

-- 查出每个月最后入职的3个人
select * from (
  SELECT "id", "date", 
  	row_number() over(
      partition by (month) order by "date" desc
    ) as last_enroll 
  from enroll
) as new_enroll 
where last_enroll < 4;
```

7.  ### 例子

    1.  CASE 语句分区间查成绩：

        ```sql
        create table course(
            cid char(5) not null,
            cname char(20),
            tid char(5)
            ) engine=innodb  default charset=utf8;
        
        create table sc(
            sid varchar(10) default null,
            cid varchar(20) default null,
            score int(10) default null
            ) engine=innodb  default charset=utf8;
        
        create table student(
            sid varchar(10) not null,
            sname varchar(20) default null,
            sage datetime default '1980-10-12',
            ssex varchar(10) default null,
            primary key(sid)
            ) engine=innodb  default charset=utf8;
        
        create table teacher(
            tid int(10) default null,
            tname varchar(10) default null
            ) engine=innodb  default charset=utf8;
        
        
        insert into course values
        (001, '企业管理', 3),
        (002, '马克思', 3),
        (003, 'UML', 2),
        (004, '数据库', 1),
        (005, '英语', 1);
        
        insert into student values
        (1001,'张三丰','1980-10-12', '男'),
        (1002,'张无忌','1980-10-12', '男'),
        (1003,'李逵','1980-10-12', '女'),
        (1004,'里元宝','1980-10-12', '女'),
        (1005,'历史名','1980-10-12', '男'),
        (1006,'赵六','1980-10-12', '男'),
        (1007,'天气','1980-10-12', '女');
        
        insert into teacher values
        (1,'李老师'),
        (2,'和一身'),
        (3,'叶萍');
        
        insert into sc values
        (1,001,80),
        (1,002,60),
        (1,003,75),
        (2,001,85),
        (2,002,70),
        (3,004,100),
        (3,001,90),
        (3,002,55),
        (4,002,65),
        (4,003,60);
        
        -- 要求：
        -- 查出结果：
        -- 数量，0_60，60_70，70_80，80_90，90_100，科目id
        
        -- 答案
        select count(1) as number,
        sum(case when score > 0 and score < 60 then 1 else 0 end) as 0_60,
        sum(case when score >=60 and score < 70 then 1 else 0 end) as 60_70,
        sum(case when score >=70 and score < 80 then 1 else 0 end) as 70_80,
    sum(case when score >=80 and score < 90 then 1 else 0 end) as 80_90,
        sum(case when score >=90 and score <=100 then 1 else 0 end) as 90_100,
    cid  from sc group by cid;
        ```

        
    
    2.  找出歌手最新的两首曲子
    
        ```sql
        CREATE TABLE "Music"(
          "id" int4 NOT NULL ,
          "name" char(20),
          "year" char(6),
          "singer_id" int4,
          PRIMARY KEY ("id")
        );
        
        INSERT INTO "Music" VALUES (1,'七里香','2003',1),(2,'吻别','2000',2),(3,'如果爱','2001',2),(4,'菊花台','2005',1),(5,'龙卷风','2000',1),(6,'一路上有你','1993',2),(7,'一千个伤心的理由','1995',2),(8,'说好不哭','2019',1);
        
        
        CREATE TABLE Singer(
          "id" int4 NOT NULL,
          "name" char(20) DEFAULT NULL,
          PRIMARY KEY ("id")
        );
        
        
        INSERT INTO Singer VALUES (1,'周杰伦'),(2,'张学友')
        
        -- 找出歌手最新的两首曲子
        select r.singer_id, r.year, r.name, s.name 
        	from (
        		select *, 
            		row_number() over (partition by singer_id order by year desc) 
            	from "Music") as r 
            left join singer s on s.id = r.singer_id
            where row_number <3;
        ```
