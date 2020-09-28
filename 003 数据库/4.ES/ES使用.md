##### 1、API接口约定

ElasticSearch整体使用RESTful规范，基于HTTP协议，并使用json格式的数据进行交互， 除非有特殊规定

主要分四个方面：

- Multiple Indices  多索引
- Date math support in index names 索引名中支持日期
- Common options  通用参数
- URL-based access control 网址访问控制

##### 2、ES术语

- Index 索引 （对比mysql的数据库）
- Type 索引中的数据类型(对比mysql的表)
- Document文档数据(就是ES中一条数据)
- Field字段，文档的属性
- Query DSL查询语法

##### 3、索引

- 创建索引

  接口：http:39.100.114.253:9200/book

  请求方法：PUT

  参数：

  ```
  {
     "settings" : {
        "number_of_shards" : 5,
        "number_of_replicas" : 1
     }
  }
  ```

  - number_of_shards 主分片数量(默认一个索引被分配到5个主分片)
  - number_of_replicas 复制分片的数量(每个主分片都有一个复制分片)

  返回数据：

  ```
  {
      "acknowledged": true,
      "shards_acknowledged": true,
      "index": "book"
  }
  ```

- 查看索引

  接口：http:39.100.114.253:9200/book

  请求方法：GET

  返回：

  ```
  {
      "book": {
          "aliases": {},
          "mappings": {},
          "settings": {
              "index": {
                  "creation_date": "1590130174737",
                  "number_of_shards": "5",
                  "number_of_replicas": "1",
                  "uuid": "9TVMQHy4S_izgOHUCcSC6g",
                  "version": {
                      "created": "5061299"
                  },
                  "provided_name": "book"
              }
          }
      }
  }
  ```

- 删除索引

  接口：http:39.100.114.253:9200/book

  请求方法：DELETE

  返回：

  ```
  {
      "acknowledged": true
  }
  ```

- 获取所有索引

  接口：http:39.100.114.253:9200/_all

  请求方法：GET

##### 4、文档

```
通常，我们可以认为对象(object)和文档(document)是等价相通的。不过，他们还是有所差别：对象(Object)是一个JSON结构体——类似于哈希、hashmap、字典或者关联数组；对象(Object)中还可能包含其他对象(Object)。
在Elasticsearch中，文档(document)这个术语有着特殊含义。它特指最顶层结构或者根对象(root object)序列化成的JSON数据（以唯一ID标识并存储于Elasticsearch中）
```

- 文档元数据

  一个文档不只有数据。它还包含了**元数据(metadata)**——**关于**文档的信息。三个必须的元数据节点是：

  | 节点     | 说明               |
  | -------- | ------------------ |
  | `_index` | 文档存储的地方     |
  | `_type`  | 文档代表的对象的类 |
  | `_id`    | 文档的唯一标识     |

- 添加文档

  格式：`/index1/type1/id`

  自增ID接口： /book/longwang/

  自定义ID接口：/book/longwang/1

  方法：POST

  参数：

  ```
  {
    "name": "蒸蛋",
    "price": 20.5,
    "images": "foods/1.jpg"
  }
  ```

  返回数据

  ```
  {
      "_index": "book",
      "_type": "longwang",
      "_id": "1",
      "_version": 1,
      "result": "created",
      "_shards": {
          "total": 2,
          "successful": 2,
          "failed": 0
      },
      "created": true
  }
  ```

- 查询文档

  格式：`/index/type/id?source=字段1，字段2&pretty`
  - id是添加的id值
  - _source是文档的原数据
  - pretty美化输出

  请求方法：GET

  ```
  http://39.100.114.253/book/longwang/1?_source=name&pretty
  ```

##### 5、搜索

- 空搜索

  接口：/_search

  请求方法： GET

  返回数据

  ```
  {
    "took": 71,              #整个搜索请求花费的毫秒数
    "timed_out": false,      #查询超时与否
    "_shards": {
      "total": 5,            #_shards节点告诉我们参与查询的分片数（`total`字段），
      "successful": 5,       #有多少是成功的（`successful`字段）
      "skipped": 0,          #有多少的是失败的（`failed`字段）
      "failed": 0
    },
    "hits": {
      "total": 4,
      "max_score": 1.0,    #指的是所有文档匹配查询中`_score`的最大值，最匹配的。
      "hits": [
        {
          "_index": "book",
          "_type": "longwang",
          "_id": "2",
          "_score": 1.0,
          "_source": {
            "name": "鸭子",
            "price": 12.5,
            "images": "foods/3.jpg"
          }
        },
        {
          "_index": "book",
          "_type": "longwang",
          "_id": "4",
          "_score": 1.0,
          "_source": {
            "name": "激荡",
            "price": 12.5,
            "images": "foods/3.jpg"
          }
  ```

  ```
   响应中最重要的部分是hits，它包含了total字段来表示匹配到的文档总数，hits数组还包含了匹配到的前10条数据。
  
  hits数组中的每个结果都包含_index、_type和文档的_id字段，被加入到_source字段中这意味着在搜索结果中我们将可以直接使用全部文档。这不像其他搜索引擎只返回文档ID，需要你单独去获取文档。
  
  每个节点都有一个_score字段，这是相关性得分(relevance score)，它衡量了文档与查询的匹配程度。默认的，返回的结果中关联性最大的文档排在首位；这意味着，它是按照_score降序排列的。这种情况下，我们没有指定任何查询，所以所有文档的相关性是一样的，因此所有结果的_score都是取得一个中间值1
  
  max_score指的是所有文档匹配查询中_score的最大值。
  
  took   告诉我们整个搜索请求花费的毫秒数。
  
  _shards节点告诉我们参与查询的分片数（total字段），有多少是成功的（successful字段），有多少的是失败的（failed字段）。通常我们不希望分片失败，不过这个有可能发生。如果我们遭受一些重大的故障导致主分片和复制分片都故障，那这个分片的数据将无法响应给搜索请求。这种情况下，Elasticsearch将报告分片failed，但仍将继续返回剩余分片上的结果。
  
  time_out值告诉我们查询超时与否。一般的，搜索请求不会超时。如果响应速度比完整的结果更重要，你可以定义timeout参数为10或者10ms（10毫秒），或者1s（1秒）
  GET /_search?timeout=10ms
  Elasticsearch将返回在请求超时前收集到的结果。
  ```

- 多索引和多类型(几种常见的)

  - `/index/_search `
  - `inedx1,index2/_search`
  - `/a*,b*/_search`  #使用*通配符
  -  `/index1/type1/_search `  在指定的索引和文档中搜索
  - ` /index1,index2/type1,type2/_search`
  - ` /_all/type1,type2/_search`

- 查询字符串

  在ES中被称之为结构化查询语句(DSL)

  - 查询字符串方式，将参数拼接到 url中

    ```
    GET /_all/text/_search?q=name:蒸
    GET /_all/text/_search?q=name:蒸+name:john+price:1.5
    ```

    "+"`前缀表示语句匹配条件必须被满足。类似的"-"前缀表示条件必须不被满足。所有条件如果没有+或-表示是可选的——匹配越多，相关的文档就越多。

    ```
    全文搜索
    GET /_search?q=蒸
    ```

  - json格式的请求体

- 分页

  ES中，接受from和size参数。

  你想每页显示5个结果，页码从1到3，那请求如下：

  ```
  GET /_search?size=5
  GET /_search?size=5&from=5
  GET /_search?size=5&from=10
  ```

##### 6、ES性能

ELasticsearch为每个field都建立了一个倒排索引。
它使用了多种压缩技术(FST)，尽可能将索引数据从硬盘放到内存
对每一个field字段建立一个term dictionary,并且对item本身又做了一层索引，term _index