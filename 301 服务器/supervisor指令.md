##### 启动服务

- ```
  supervisord -c xxxx.conf
  ```

##### 进入客户端操作

- ```
  supervisorctl 
  ```

##### 查看任务状态

- ```
  supervisorctl status
  第一列是服务名；第二列是运行状态，RUNNING表示运行中，FATAL 表示运行失败，STARTING表示正在启动,STOPED表示任务已停止；　第三/四列是进程号,最后是任务已经运行的时间。
  ```

##### 启动任务

- ```
  supervisorctl  start 服务名
  ```

##### 停止任务

- ```
  supervisorctl  stop 服务名
  ```

##### 重启任务

- ```
  supervisorctl restart 服务名
  ```

##### 增加了配置文件,更新

- ```
  supervisorctl update
  ```

#####配置文件默认在 `etc/supervisord.d/`目录下

supervisord.conf 注释是；

```
#配置文件
[program:sparkportal]
command=node www.js
process_name=%(program_name)s ; process_name expr (default %(program_name)s)
numprocs=1                    ; number of processes copies to start (def 1)
directory=/usr/local/sparkportal/bin                ; directory to cwd to before exec (def no cwd)
;umask=022                     ; umask for process (default None)
;priority=999                  ; the relative start priority (default 999)
autostart=true                ; start at supervisord start (default: true)
autorestart=unexpected        ; whether/when to restart (default: unexpected)
startsecs=1                   ; number of secs prog must stay running (def. 1)
startretries=3                ; max # of serial start failures (default 3)
exitcodes=0,2                 ; 'expected' exit codes for process (default 0,2)
stopsignal=QUIT               ; signal used to kill process (default TERM)
stopwaitsecs=10               ; max num secs to wait b4 SIGKILL (default 10)
stopasgroup=false             ; send stop signal to the UNIX process group (default false)
killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=skywell                  ; setuid to this UNIX account to run the program
;redirect_stderr=true          ; redirect proc stderr to stdout (default false)
stdout_logfile=/var/log/sparkportal.log        ; stdout log path, NONE for none; default AUTO
stdout_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
stdout_logfile_backups=1     ; # of stdout logfile backups (default 10)
stdout_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
stdout_events_enabled=false   ; emit events on stdout writes (default false)
stderr_logfile=/var/log/sparkportal.err        ; stderr log path, NONE for none; default AUTO
stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
stderr_logfile_backups=10     ; # of stderr logfile backups (default 10)
stderr_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
stderr_events_enabled=false   ; emit events on stderr writes (default false)
environment=A="1",B="2",HOME="/home/skywell"       ; process environment additions (def no adds),
serverurl=AUTO                ; override serverurl computation (childutils)
```

