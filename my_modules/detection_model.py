from rfdetr.detr import RFDETRNano, RFDETRSmall, RFDETRMedium, RFDETRLarge 
from rfdetr.util.coco_classes import COCO_CLASSES

def get_model(size:str = 'nano', optimize: bool = False):
    match size:
        case 'nano':
            model = RFDETRNano()
        case 'small':
            model = RFDETRSmall()
        case 'medium':
            model = RFDETRMedium()
        case 'large': 
            model = RFDETRLarge()
    if optimize:
        model.optimize_for_inference()
    return model

def get_model_classes():
    return COCO_CLASSES

def get_classes_of_interest()->list:
    # categories we're interested in - here flying objects
    return [5, 16, 34, 37, 38]

def filter_results(results, classes_of_interest: list, track_objects: bool)->tuple:
    
    class_ids = results.class_id
    xyxys = results.xyxy
    if track_objects:
        tracker_ids = results.tracker_id

    bboxes = []
    tracker_id = []
    
    if track_objects:
        for class_id, xyxy, track_id in zip(class_ids, xyxys, tracker_ids):
            if class_id in classes_of_interest:
                bboxes.append(xyxy)
                tracker_id.append(int(track_id))
    else: 
        for class_id, xyxy in zip(class_ids, xyxys):

            if class_id in classes_of_interest:
                bboxes.append(xyxy)
    
    return bboxes, tracker_id

def get_detections(img, model, tracker, detection_threshold: float, track_objects: bool):
    # get detections with tracking
    results = model.predict(img, threshold=detection_threshold) # get detection results
    if track_objects: 
        results = tracker.update(results) # update with tracker info
    return results

