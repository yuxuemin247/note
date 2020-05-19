- 查看crontab服务状态：service crond status
- 手动启动crontab服务：service crond start 

- 使用1：直接分配

  - 终端输入   crontab -e                      #可以crontab -u root -e 指定用户是root

  - 在出来的可编辑文件编写

    ```
    如：每分钟执行一次任务，将时间输出到/home/mydatetest
    0 * * * * date >> /home/mydatetest
    ```

