from cv2 import VideoCapture


def capture(path):
    if path == '0':
        return VideoCapture(
            0
        )
    
    else:
        return VideoCapture(
            path
        )
