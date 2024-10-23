import cv2
import os
import time
import base64
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# We'll be using the OpenAI DevDay Keynote Recap video. You can review the video here: https://www.youtube.com/watch?v=h02ti0Bl6zk
def process_video(datadir,videos_path, extract_frames_persecond=2,resize_fx=1,resize_fy=1):
    base64Frames = {"cogvideox5b": [],"kling": [],"gen3": [],"lavie": [],"pika": [],"show1":[],"videocrafter2":[]}
    for key in base64Frames.keys():
        video = cv2.VideoCapture(os.path.join(datadir,videos_path[key]))

        if not video.isOpened():
            print(f"Error: Cannot open video file {datadir+videos_path[key]}")
            continue

        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = video.get(cv2.CAP_PROP_FPS)
        if key == "gen3":
            frames_to_skip = int(2*fps/extract_frames_persecond)
        else:
            frames_to_skip = int(fps/extract_frames_persecond)
    
        curr_frame=1
        end_frame = total_frames - 1
        # Loop through the video and extract frames at specified sampling rate
        while curr_frame < total_frames - 1:
            video.set(cv2.CAP_PROP_POS_FRAMES, curr_frame)
            success, frame = video.read()
            if not success:
                break

            frame = cv2.resize(frame, None, fx=resize_fx, fy=resize_fy)

            _, buffer = cv2.imencode(".jpg", frame)
            base64Frames[key].append(base64.b64encode(buffer).decode("utf-8"))
            curr_frame += frames_to_skip

        video.set(cv2.CAP_PROP_POS_FRAMES, end_frame)
        success, frame = video.read()
        if not success:
            break

        frame = cv2.resize(frame, None, fx=resize_fx, fy=resize_fy)

        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames[key].append(base64.b64encode(buffer).decode("utf-8"))

        
        video.release()
        
    


    return base64Frames


def display_base64_images(base64Frames, cols=7):
    for key, frames in base64Frames.items():
        print(f"Displaying images for {key}:")
        num_images = len(frames)
        rows = (num_images + cols - 1) // cols  # 计算行数
        fig, axes = plt.subplots(rows, cols, figsize=(15, 3 * rows))
        axes = axes.flatten()  # 将 axes 转换为一维数组，方便索引

        for i, b64_string in enumerate(frames):
            # 解码 Base64 字符串
            img_data = base64.b64decode(b64_string)
            # 将字节数据转换为 BytesIO 对象
            img_buffer = BytesIO(img_data)
            # 使用 PIL 打开图像
            img = Image.open(img_buffer)
            # 将 PIL 图像转换为 NumPy 数组
            img_np = np.array(img)
            # 显示图像
            axes[i].imshow(img_np)
            axes[i].set_title(f"{key} - Frame {i}")
            axes[i].axis('off')  # 隐藏坐标轴

        # 隐藏多余的子图
        for j in range(i + 1, len(axes)):
            axes[j].axis('off')

        plt.tight_layout()
        plt.show()