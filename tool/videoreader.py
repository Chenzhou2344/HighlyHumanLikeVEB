import cv2
import time
import base64
from IPython.display import Image, display
# We'll be using the OpenAI DevDay Keynote Recap video. You can review the video here: https://www.youtube.com/watch?v=h02ti0Bl6zk
def process_video(datadir,videos_path, extract_frames_persecond=2,resize_fx=1,resize_fy=1):
    base64Frames = {"gen2": [],"lavie": [],"pika": [],"show1":[],"videocrfater2":[]}
    for key in base64Frames.keys():
        video = cv2.VideoCapture(datadir+videos_path[key])
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = video.get(cv2.CAP_PROP_FPS)
        frames_to_skip = int(fps/extract_frames_persecond)
        curr_frame=0
        # Loop through the video and extract frames at specified sampling rate
        while curr_frame < total_frames - 1:
            video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
            success, frame = video.read()
            if not success:
                break

            frame = cv2.resize(frame, None, fx=resize_fx, fy=resize_fx)

            _, buffer = cv2.imencode(".jpg", frame)
            base64Frames[key].append(base64.b64encode(buffer).decode("utf-8"))
            curr_frame += frames_to_skip
        video.release()
        
    


    return base64Frames

