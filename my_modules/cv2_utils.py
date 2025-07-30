# https://www.color-hex.com/color-palettes/popular.php
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

def plot_bboxes(frame: np.ndarray, 
                bboxes: list, 
                track_objects: bool,
                tracker_id: list=[]):
    if track_objects: 
        assert len(bboxes) == len(tracker_id), "Number of BBoxes and track IDs does NOT match !!!"
        palette = create_palette() # get palette
        for bbox, track_id in zip(bboxes, tracker_id):
            color_index: int = track_id % len(palette)
            box_color = palette[color_index]
            pt1 = (int(bbox[0]), int(bbox[1]))
            pt2 = (int(bbox[2]), int(bbox[3]))
            frame = cv2.rectangle(img=frame,
                    pt1=pt1,
                    pt2=pt2,
                    color=box_color,
                    thickness=2)
            bbox_x_center: int = int(pt1[0] + (pt2[0]-pt1[0])/2)
            radius = int(0.01 * frame.shape[1])
            marker_height = int(0.9 * frame.shape[0] - radius)
            frame = cv2.circle(img=frame, 
                               center=(bbox_x_center, marker_height), 
                               radius=int(0.7* radius), 
                               color=(0, 255, 0), 
                               thickness=-1)

        
    else:
        for bbox in bboxes:
            pt1 = (int(bbox[0]), int(bbox[1]))
            pt2 = (int(bbox[2]), int(bbox[3]))
            frame = cv2.rectangle(img=frame,
                                pt1=pt1,
                                pt2=pt2,
                                color=(255, 0, 255),
                                thickness=2)
    return frame

def create_palette():
    bgr_palette: list = [
        # GRYFFINDOR
        (1, 0, 116),
        (1, 0, 174),
        (48, 186, 238),
        (37, 166, 211),
        (0, 0, 0),
        # SLYTHERIN
        (42, 71, 26),
        (61, 98, 42),
        (93, 93, 93),
        (170, 170, 170),
        #RAVENCLAW
        (64, 26, 14),
        (91, 47, 34),
        (45, 107, 148),
        #HUFFLEPUFF
        (57, 185, 236),
        (94, 199, 240),
        (85, 98, 114),
        (41, 46, 55),
        # SUMMERTIME 3
        (79, 190, 255),
        (219, 210, 107),
        (181, 167, 14),
        (125, 69, 12),
        (42, 112, 232),
        # METRO UI COLORS
        (65, 17, 209),
        (89, 177, 0),
        (219, 174, 0),
        (53, 119, 243),
        (37, 196, 255),
        # PURPLE
        (255, 187, 239),
        (255, 150, 216),
        (236, 41, 190),
        (128, 0, 128),
        (102, 0, 102)]
    return bgr_palette

def draw_angle_ruler(img: np.ndarray, camera_angle: float=90.):
    # draw azimuthal angle ruler
    horiz_len: int = img.shape[1] # get number of pixels - horizontal resolution
    d_alpha: float = camera_angle / horiz_len # get angle degrees per one pixel
    landmark_pixels = np.array([0.1, 0.3, 0.5, 0.7, 0.9]) * horiz_len # get columns at 10%, 30% ... of horizontal resolution
    landmark_angles = (np.array([0.1, 0.3, 0.5, 0.7, 0.9]) * camera_angle) - 0.5 * camera_angle
    
    ruler_height = int(0.9 * img.shape[0]) # height 
    # draw main ruler
    pt1: tuple = (int(landmark_pixels[0]), ruler_height)
    pt2: tuple = (int(landmark_pixels[-1]), ruler_height)
    img = cv2.line(img=img, 
                   pt1=pt1, 
                   pt2=pt2, 
                   color=(0, 255, 0), 
                   thickness=3)

    # draw line markers
    marker_height:int = int(0.03 * img.shape[0])
    for marker in landmark_pixels:
        pt1 = (int(marker), ruler_height)
        pt2 = (int(marker), (ruler_height + marker_height))
        img = cv2.line(img=img,
                       pt1=pt1,
                       pt2=pt2,
                       color=(0, 255, 0), 
                       thickness=3)
    
    # write angle values

    for angle, pixel in zip(landmark_angles, landmark_pixels):
        angle_str = f'{angle:.2f}'
        org = (int(pixel), (ruler_height + 2 * marker_height))
        cv2.putText(img=img,
                    text=angle_str,
                    org=org,
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=(0, 255, 0),
                    thickness=2)
    return img