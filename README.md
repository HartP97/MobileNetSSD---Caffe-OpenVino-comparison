# MobileNetSSD Caffe-OpenVino-comparison
This project indicates performance differences of using MobileNetSSD with Caffe and OpenVino
```diff
- it does not contain the used video for legal reasons as it is property of Udacity
```
## Caffe vs. OpenVino
*(size, execution-time, CPU-usage)*

#### Video reply without model

- size: **0 KB (no model used)**
- execution-time: **2 minutes 24 seconds**
- CPU-usage (avg of 3 executions): **3.70%**

#### Caffe-Model
- size: **MobileNetSSD_deploy.caffemodel: 23.1 MB, MobileNetSSD_deploy.prototxt: 29 KB**
- execution-time: **3 minute 9 seconds 2:48**
- CPU-usage (avg of 10 executions): **9.97%**
