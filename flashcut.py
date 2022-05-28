import cv2
import librosa


class FlashCut():
    def __init__(self, video_filepath=None) -> None:
        self.cap = None
        if video_filepath is not None:
            self.cap = cv2.VideoCapture(video_filepath)

    def __del__(self):
        if self.cap is not None:
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
            frame = self.preprocess_frame(frame, 960, 540)

    def is_flashback_frame(self, frame):
        """
        Returns whether the given `frame` is part of a flashback based on its
        colours.
        """
        pass

    def is_flashback_transition_frame(self, frame):
        """
        Returns whether the given `frame` is part of a transition to a
        flashback based on its colours, brightness, and blur.
        """
        pass

    def preprocess_frame(self, frame, width, height):
        """
        Preprocesses the given `frame` by reducing its dimensions to the given
        `width` and `height`.
        """
        return cv2.resize(frame, (width, height))

    def compute_img_features(self, frame):
        pass

    def compute_audio_features(self, audio):
        pass

    def show_img(self, img):
        """
        Displays the given image until any key is pressed.
        """
        cv2.imshow(winname="Image", mat=img)
        cv2.waitKey(0)
