from cv2 import CascadeClassifier


def classifier(path):
    return CascadeClassifier(
        path
    )
