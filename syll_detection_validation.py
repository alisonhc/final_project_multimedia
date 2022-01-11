import os.path

import speech_rate_detection as srd

candidate_fpath = 'data/candidates'
speeds = [4, 5.5, 7, 8.5, 10, 11.5]
clip_nums = [1, 2, 3, 4, 5, 6]
actual_nums = [31,
               35,
               26,
               27,
               39,
               27]

# num_abs_acc = 0
all_errors = 0

for i in range(6):
    clip_num = clip_nums[i]
    #for j in range(6):
    #speed = speeds[j]
    fpath = os.path.join(candidate_fpath, f'clip_{clip_num}.wav')
    sr_info = srd.speech_rate(fpath)
    num_sylls = sr_info['nsyll']
    dur = sr_info['dur(s)']
    est_rate = num_sylls / dur
    actual_rate = actual_nums[i] / dur
    print(actual_rate, est_rate)
    print(abs(actual_rate - est_rate))
    all_errors += abs(actual_rate - est_rate)
    # print(f'{clip_num}_{speed}: \n est_speed: {est_speed}\n actual speed: {speed}\n'
    #           f'absolute error: {abs(speed-est_speed)}')
        #err = abs(speed-est_speed)
        #all_errors += err
        # if err == 0:
        #     num_abs_acc += 1

print(f"MAE: {all_errors/36}")
# print(f"Abs acc: {num_abs_acc/36}")