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
    non_fb_frames = []

    # Track progression
    fb_idx = 0
    frame_num = 0
    in_flashback = False

    cap = cv2.VideoCapture(video_filepath)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fb_frame_tups = sec_tups_to_frame_num_tups(fb_timestamps, fps)

    while True:
        (retval, frame) = cap.read()
        if not retval:  # Breaks at the end of a video file
            break

        # Start tracking a flashback scene if we encounter one
        if frame_num == fb_frame_tups[fb_idx][0]:
            in_flashback = True

        # Stop tracking a flashback scene when a timestamp denotes it
        if frame_num == fb_frame_tups[fb_idx][1]:
            in_flashback = False
            fb_idx += 1

        # Save frames according to whether we're in a flashback or not
        if in_flashback:
            fb_frames.append(frame)
        else:
            non_fb_frames.append(frame)

        frame_num += 1

    return (np.array(non_fb_frames), np.array(fb_frames))


def seconds_to_frame_num(secs, fps, n_extra_frames=0):
    """
    Converts the given number of `seconds` to a frame number by using a
    given number of frames per second.
    """
    n_extra = n_extra_frames + fps//2  # Get the middle frame within a second
    return secs*fps + n_extra_frames


def sec_tups_to_frame_num_tups(sec_tups, fps, n_extra=0):
    """
    Converts a given list of tuples containing two integers denoting seconds
    to a list of tuples containing two integers denoting frame numbers
    according to a given number of frames per second.
    """
    return [
        (seconds_to_frame_num(sec0, fps, n_extra),
         seconds_to_frame_num(sec1, fps, n_extra))
        for (sec0, sec1) in sec_tups
    ]
