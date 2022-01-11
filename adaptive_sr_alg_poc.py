import os
import time
import pytsmod as tsm
import soundfile as sf
import time_compressing as tc
import speech_rate_detection as srd

THRESH = 7


def get_max_percent_to_compress_given_thresh(rate):
    return tc.calc_compression_factor(rate, THRESH)


def compress_up_to_time_left(seg_frames, dur, time_left):
    compress_percent = dur / time_left
    return tsm.wsola(seg_frames, compress_percent)


def process_late_speech_seg(seg_fpath: str, deadline):
    r_info = srd.speech_rate(seg_fpath)
    num_sylls, dur = r_info['nsyll'], r_info['dur(s)']
    rate = num_sylls / dur
    max_to_compress = get_max_percent_to_compress_given_thresh(rate)
    time_left = deadline - time.time()
    x, sr = sf.read(seg_fpath)  # x is ndarray and sr is sampling_rate
    x = x.T
    if dur*max_to_compress <= time_left:
        sped_seg = compress_up_to_time_left(x, dur, time_left)
        return sped_seg, False  # delayed = False
    else:
        sped_seg = tsm.wsola(x, dur, max_to_compress)
        return sped_seg, True  # delayed = True



