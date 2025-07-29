#https://medium.com/@hesam.alavi1380/argparse-example-script-f767a3f89a93
from my_modules import cv2_utils, detection_model, parser_utils
import cv2
    
args_dict = parser_utils.get_parser_args()

DEVICE = args_dict["input"]
MODEL_SIZE = args_dict["size"]
DETECTION_THRESHOLD = args_dict["threshold"]

vid_cap = cv2_utils.get_vid_cap(device=DEVICE)
model = detection_model.get_model(size=MODEL_SIZE, optimize=True)
classes_of_interest = detection_model.get_classes_of_interest()

while True:
    ret, frame = cv2_utils.grab_frame(vid_cap=vid_cap)

    pil_frame = cv2_utils.convert_to_PIL(frame=frame)
    results = model.predict(pil_frame, threshold=DETECTION_THRESHOLD)
    bboxes = detection_model.filter_results(results=results,
                                            classes_of_interest=classes_of_interest)

    frame = cv2_utils.plot_bboxes(frame=frame, bboxes=bboxes)
    cv2_utils.show_frame(frame=frame, 
                    window_name="frame", 
                    scale=.5)
    k = cv2.waitKey(1)
    if k == 27:
        break
    

cv2_utils.clear_memory(vid_cap=vid_cap)
