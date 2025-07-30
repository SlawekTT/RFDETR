from trackers import SORTTracker

def initialize_tracker(lost_track_buffer: int=100):
    tracker = SORTTracker(lost_track_buffer=lost_track_buffer)
    return tracker