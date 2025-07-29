#https://medium.com/@hesam.alavi1380/argparse-example-script-f767a3f89a93
from my_modules import cv2_utils, model_builder, parser_utils

    
args_dict = parser_utils.get_parser_args()

device = args_dict["input"]
print(device)

vid_cap = cv2_utils.get_vid_cap(device=device)
print(vid_cap)
