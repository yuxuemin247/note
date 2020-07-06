##### 1、启动rabbitmq节点

```
rabbitmq-server
```

##### 2、rabbitmq配置工具

可以管理用户，集群配置，权限设置，队列备份策略等

- 查看节点运行状态

  ```
  rabbitmqctl status
  ```

- 停止节点的应用

  ```
  rabbitmqctl stop_app
  ```

- 启动节点的应用

  ```
  rabbitmqctl start_app
  ```

-  把节点加入到集群

  ```
  rabbitmqctl join_cluster <clusterbode> [--disc--ram]
  ```

- 查看集群状态

  ```
  rabbitmqctl cluster_status
  ```

- 摘除节点，忘记节点，失败状态

  ```
  rabbitmqctl forget_cluster_node [--offline]
  ```

- 移除所有数据

  ```
  rabbitmqctl reset  移除所有数据，要在rabbitmqctl stop_app之后使用
  ```

- 设置queue备份策略

  格式如 set_policy [-p <vhostpath>] <name> <pattern>  <definition> [<priority>]

  ```
  rabbitmqctl set_policy ha-exactly-two ".*" '{"ha-mode":"exactly","ha-params":2}'
  ```

##### 3、 rabbitmq-plugins扩展插件

- 开启/关闭web管理功能

  ```
   rabbitmq-plugins enable/disable rabbitmq-management    #http://ip:15672
  ```

  



