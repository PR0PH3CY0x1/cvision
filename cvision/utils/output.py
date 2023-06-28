from cv2 import COLOR_BGR2GRAY

from cv2 import destroyAllWindows, waitKey
from cv2 import cvtColor, rectangle, imshow


def read_capture(capture, classifier):
    while True:
        try:
            ret, frame = capture.read(

            )

            gray = cvtColor(
                frame, 
                COLOR_BGR2GRAY
            )

            cars = classifier.detectMultiScale(
                gray,
                1.1,
                1
            )

            for ( x, y, w, h ) in cars:
                rectangle(
                    frame,
                    ( x, y ),
                    ( x + w, y + h ),
                    ( 51, 225, 51 ),
                    2
                )

            imshow(
                'cvision_output',
                frame
            )

            if waitKey(33) == 27:
                break
        
        except:
            break

    destroyAllWindows()
