# MobileNetSSD Caffe-OpenVino-comparison
This project indicates performance differences of using MobileNetSSD with Caffe and OpenVino
```diff
- it does not contain the used video for legal reasons as it is property of Udacity
```
## Caffe vs. OpenVino
*(size, execution-time, CPU-usage)*

#### Video replay without model

- size: **0 KB (no model used)**
- execution-time: **2 minutes 24 seconds**
- CPU-usage (avg of 3 executions): **3.70%**

#### Caffe-Model
- size: **MobileNetSSD_deploy.caffemodel: 23.1 MB, MobileNetSSD_deploy.prototxt: 29 KB**
- execution-time: **3 minute 9 seconds 2:48**
- CPU-usage (avg of 10 executions): **9.97%**

_(Note: Original-Code was retrieved from: [pyimagesearch](https://www.pyimagesearch.com/2017/09/18/real-time-object-detection-with-deep-learning-and-opencv/))_

#### OpenVino
- size: **MobileNetSSD_deploy.bin: 23.1 MB, MobileNetSSD_deploy.xml: 175 KB**
- execution-time (speed):  **4 minutes 22 seconds**
- CPU overhead (avg of 10 executions): **8.14% (-1.83% vs. default Caffe-Model)**

#### Comparison-Conclusion
Only slight improvement was noticed when using the model converted to IR with OpenVino, when it comes to CPU-usage, which decreased by 1.83%. Those results were expected as MobileNet models are already well optimised for speed and size.

### Running instructions
- **Video replay without model:** Use the running instructions mentioned at the end of [simple_video.py](simple_video.py)
- **Caffe-Model:** Use the running instructions mentioned at the end of [detection_caffe.py](detection_caffe.py)

