from rfdetr import RFDETRNano
from rfdetr.util.coco_classes import COCO_CLASSES

def get_model(optimize: bool = False):
    model = RFDETRNano()
    if optimize:
        model.optimize_for_inference()
    return model

def get_model_classes():
    return COCO_CLASSES
