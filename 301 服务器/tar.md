- 打包文件夹

  ```
  tar -cvf xxx.tar xxx/
  ```

- 解包文件夹

  ```
  tar -xf xxx.tar
  ```

  



- 打包后，以`gzip`压缩

  ```
  tar -zcvf  xxx.tar xxx
  ```

- 从文件创建存档

  ```
  tar cf target.tar file1 file2 file3
  ```

- 创建`gzipped`存档

  ```
  tar czf target.tar.gz file1 file2 file3
  ```

- 使用相对路径从目录创建`gzipped `存档

  ```
  tar czf target.tar.gz -C path/to/directory .
  ```

  

- 将一个(压缩的)存档文件解压缩到当前目录

  ```
  tar xf source.tar[.gz|.bz2|.xz]
  ```

- 将存档解压到目标目录中

  ```
  tar xf source.tar -C directory
  ```

- 解压

  ```
  tar zxf  xxx.tgz
  ```

  