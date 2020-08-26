- 连接数据库

  ```
   psql -U 用户名   --db 数据库名
  ```

- pg强行删库

  ```
  SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE datname='skynet' AND pid<>pg_backend_pid();
  drop database skynet;
  ```

- 执行sql

  ```
  psql -U 用户名 -d 数据库名  -a -f init.sql
  ```

- 显示数据库

  /usr/bin/psql -c "\l"





