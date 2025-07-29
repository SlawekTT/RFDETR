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

def filter_results(results, classes_of_interest: list)->list:
    
    class_ids = results.class_id
    xyxys = results.xyxy

    bboxes = []

    for class_id, xyxy in zip(class_ids, xyxys):

        if class_id in classes_of_interest:
            bboxes.append(xyxy)
    
    return bboxes

