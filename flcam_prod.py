#!/usr/bin/python

from flcam_config import urlx,flip,portnum
from flask import Flask, render_template, Response
from waitress import serve
import cv2, time, sys

app = Flask('FLCAM_PROD_SRV')

camera = cv2.VideoCapture(urlx)  
if camera is None or not camera.isOpened():
    print('Unable to open video source: ',rtsp_url)
    sys.exit("Video source failed to open...exiting") 

def gen_frames():  
    while True:
        #print(time.time())
        success, frame = camera.read()
        if not success:
            break
        else:
            if flip == 1: frame=cv2.rotate(frame, cv2.ROTATE_180)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/')
def index():
    return """
<body>
<div class="container">
    <div class="row">
        <div class="col-lg-8  offset-lg-2">
            <h3 class="mt-5">FlCam is Live Streaming</h3>
            <img src="/video_feed" width="50%">
        </div>
    </div>
</div>
</body>        
    """
serve(app, host="0.0.0.0", port=portnum)
