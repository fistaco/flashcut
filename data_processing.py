from tokenize import String
from typing import Tuple
import cv2
import numpy as np


def divide_frames(video_filepath, fb_timestamps):
    """
    Iterates over all frames from the video file corresponding to the given
    `video_filepath`, detects flashback frames using the given `fb_timestamps`,
    and returns a tuple containing the respective lists of regular frames and
    flashback frames.

    Arguments:
        `video_filepath`: A string denoting the filepath to a video file.
        `fb_timestamps`: A list of tuples where each tuple contains two
            integers that define a flashback's boundaries. Each integer defines
            the number of seconds elapsed from the start of the video.

    Returns:
        A tuple in which the first item is a list containing regular frames and
        the second item is a list containing flashback frames.
    """
    fb_frames = []

    # Track flashback progression
    fb_idx = 0

    # TODO:
    # - Convert given frame timestamps to frame numbers
    # - Use frame numbers to track and extract flashback frames

    cap = cv2.VideoCapture(video_filepath)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    while True:
        (retval, frame) = cap.read()
