"""
Contains openCV functions
"""

import cv2
import numpy as np

from PIL import Image

def get_vid_cap(device: str):
    return cv2.VideoCapture(device)

def grab_frame(vid_cap: cv2.VideoCapture) -> tuple:
    ret, frame = vid_cap.read()
    return ret, frame

def show_frame(frame: np.ndarray, 
               window_name: str, 
               scale:float=0.25):
    frame = cv2.resize(frame, 
                       dsize=None, 
                       fx=scale, 
                       fy=scale)
    cv2.imshow(window_name, 
               frame)

def clear_memory(vid_cap: cv2.VideoCapture):
    cv2.destroyAllWindows()
    vid_cap.release()

def video_streaming(vid_cap: cv2.VideoCapture, 
                    delay: int=30, 
                    scale: float=0.25, 
                    window_name: str ="frame"):
    while True:
        ret, frame = grab_frame(vid_cap=vid_cap)
        assert(ret)
        show_frame(frame=frame, 
                   window_name=window_name,
                   scale=scale)
        k= cv2.waitKey(delay=delay)
        if k == 27:
            break

def convert_to_PIL(frame: np.ndarray):
    return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def plot_bboxes(frame: np.ndarray, bboxes: list):
    for bbox in bboxes:
        pt1 = (int(bbox[0]), int(bbox[1]))
        pt2 = (int(bbox[2]), int(bbox[3]))
        frame = cv2.rectangle(img=frame,
                              pt1=pt1,
                              pt2=pt2,
                              color=(0, 255, 0),
                              thickness=1)
    return frame

