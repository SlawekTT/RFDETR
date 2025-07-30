#https://medium.com/@hesam.alavi1380/argparse-example-script-f767a3f89a93
from my_modules import cv2_utils, detection_model, parser_utils, tracker_utils
import cv2
import numpy as np

# DEFINE CONSTANT VALUES
DEVICE, MODEL_SIZE, DETECTION_THRESHOLD = parser_utils.get_cli_params()
DEVICE = parser_utils.device_to_int(DEVICE=DEVICE)

VID_CAP = cv2_utils.get_vid_cap(device=DEVICE) # get video capture object
MODEL = detection_model.get_model(size=MODEL_SIZE, optimize=True) # initialize detection model
TRACKER = tracker_utils.initialize_tracker(lost_track_buffer=100) # initialize tracker
CLASSES_OF_INTEREST = detection_model.get_classes_of_interest() # define classes of interest (flying stuff)

while True: # main loop
    ret, frame = cv2_utils.grab_frame(vid_cap=VID_CAP) # grab a frame
    # if no more frame are available
    if not ret:
        print('Stream ended !!!')
        cv2.waitKey(0) # wait for keypressed
        break

    pil_frame = cv2_utils.convert_to_PIL(frame=frame) # convert frame to PIL image - RFDETR works better this way
    results = detection_model.get_detections(img=pil_frame,
                                             model=MODEL,
                                             tracker=TRACKER,
                                             detection_threshold=DETECTION_THRESHOLD,
                                             track_objects=True)
    # get boxes for objects in classes of interest
    bboxes, track_id = detection_model.filter_results(results=results,
                                            classes_of_interest=CLASSES_OF_INTEREST,
                                            track_objects=True)
    frame = cv2_utils.plot_bboxes(frame=frame, 
                                  bboxes=bboxes,
                                  tracker_id=track_id,
                                  track_objects=True) # plot bboxes
    frame = cv2_utils.draw_angle_ruler(img=frame)

    # show frame on screen
    cv2_utils.show_frame(frame=frame, 
                    window_name="frame", 
                    scale=.5)
    k = cv2.waitKey(1) # wait 1 ms
    if k == 27: # if <esc> then brake
        break
    

cv2_utils.clear_memory(vid_cap=VID_CAP) # release vid_cap and kill window


