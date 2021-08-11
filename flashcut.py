import cv2
import librosa


class FlashCut():
    def __init__(self, video_filepath) -> None:
        self.cap = cv2.VideoCapture(video_filepath)

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def run(self):
        """
        Iterates over the video data contained in `self.cap` and returns a list
        of tuples, each of which represents a time windows that contains a
        flashback.
        """
        while True:
            (retval, frame) = self.cap.read()

            # Preprocess image
            frame = cv2.resize(frame, (960, 540))

    def preprocess_frame(self, frame, width, height):
        """
        Preprocesses the given `frame` by reducing its dimensions to
        """

    def compute_img_features(self, frame):
        pass

    def compute_audio_features(self, audio):
        pass

    def show_img(self, img):
        """
        Displays the given image until any key is pressed.
        """
        cv2.imshow(img)
        cv2.waitKey(0)
