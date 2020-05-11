`cmd`下执行指令

- 从视频中提取音频  

  ```
  ffmpeg -i test.mp4 -f mp3 -vn test.mp3
  ```

- 视频截取

  ```
  ffmpeg -ss 00:00:25 -i test.mp4 -acodec copy -vcodec copy -t 00:02:20 test1.mp4
  ```

- 从视频中提取无声视频

  ```
  ffmpeg -i test.mp4 -vcodec copy -an test2.mp4
  ```

- 合并视频和音频

  ```
  ffmpeg -i test.mp3 -i test3.mp4 test4.mp4
  ```

  