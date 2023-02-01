# FlCam
Python code for live streaming PiCam or any plug-and-play usb webcam on the Internet. IP camera with RTSP can be live streamed without exposing camera's username and password or requiring any 3rd party viewers e.g. VLC.

## Getting Started

### Prerequisites
* raspberry pi zero w or better
* PiCam or webcam
* python 3


Install (or upgrade those already installed).
```
pip install numpy
pip install opencv-python 
pip install flask
pip install waitress

```

### flcam_config

Edit the `flcam_config.py` file according to your configuration


## Running the code

`./flcam_prod.py`

Then open `http://flcam_prod_host_computers_ip:8989` to view camera's live stream.