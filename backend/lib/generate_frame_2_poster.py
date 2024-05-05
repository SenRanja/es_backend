# coding=utf-8

import cv2
import random

def generate_poster(video_source, frame_name):
    # 打开视频文件
    videoCapture = cv2.VideoCapture(video_source)
    # 获取视频的总帧数
    total_frames = int(videoCapture.get(cv2.CAP_PROP_FRAME_COUNT))
    # 生成一个随机帧索引
    random_frame_index = random.randint(0, total_frames - 1)
    # 将视频的帧设置到随机选择的索引位置
    videoCapture.set(cv2.CAP_PROP_POS_FRAMES, random_frame_index)
    # 读取随机帧
    success, frame = videoCapture.read()

    # 如果成功读取了帧，则保存帧
    if success:
        address = frame_name
        cv2.imwrite(address, frame)
