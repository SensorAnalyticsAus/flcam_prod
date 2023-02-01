import os

urlx = 0 # camid 0 or '' quoted RTSP url
flip = 1   # Flip camera images: 1
portnum = 8989
# rtsp_flag are set below.
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"]="rtsp_transport;tcp\
   |analyzeduration;9000\
   |reorder_queue_size;2500"
# informational message-levels are set below.
#os.environ["OPENCV_FFMPEG_DEBUG"] = "1" 
os.environ["OPENCV_LOG_LEVEL"] = "QUIET"
#os.environ["OPENCV_LOG_LEVEL"] = "VERBOSE"
#os.environ["OPENCV_LOG_LEVEL"] = "ERROR"

