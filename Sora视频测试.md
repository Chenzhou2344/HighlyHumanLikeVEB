# Sora视频测试

选取一致性中的Video-text Consistency，动态指标中的Motion Effects，静态中的Aesthetic Quality

生成参数分辨率720P,比例16:9,时长5s；
（因为成本限制没有采用1080P为更客观评估因此静态指标没有选择Imaging Quality）

### 评估结果

| VG Model      | Aesthetic Quality | Motion Effects | Video-text Consistency |
| ------------- | ----------------- | -------------- | ---------------------- |
| Sora          | 4.6               |                |    4.47                |
| CogVideoX     | 4                 |                |    4.57                |
| Kling         | 3.933             |                |    4.13                |
| Gen3          | 4.567             |                |    4.27                |
| videocrafter2 | 3.9               |                |    4.10                |
| pika          | 3.8               |                |    3.67                |
| show1         | 3.267             |                |    4.27                |
| lavie         | 2.867             |                |    3.87                |