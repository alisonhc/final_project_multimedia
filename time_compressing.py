import os
import pytsmod as tsm
import soundfile as sf


desired_sylls = [4, 5.5, 7, 8.5, 10, 11.5]

def calc_compression_factor(original_syll_rate, desired_syll_rate):
    compression_factor = original_syll_rate / desired_syll_rate
    return compression_factor


def create_diff_speed_versions(fpath, dest_path, num_syll):
    x, sr = sf.read(fpath)  # x is ndarray and sr is sampling_rate
    x = x.T
    x_length = x.shape[-1]  # length of the audio sequence x.
    duration_seconds = x_length / sr
    original_syll_rate = num_syll / duration_seconds
    original_clip_num = fpath.split('_')[-1].split('.')[0]
    for i in desired_sylls:
        new_fpath = os.path.join(dest_path, f'clip_{original_clip_num}_{i}_sylls.wav')
        compression_factor = calc_compression_factor(original_syll_rate=original_syll_rate, desired_syll_rate=i)
        print(f"new duration: {compression_factor*duration_seconds}")
        sped_x = tsm.wsola(x, compression_factor)
        sf.write(new_fpath, sped_x, sr)


# if __name__ == '__main__':
#     dest_path_folder = '/data/compressed_candidates'
#     clip_dict = {'clip_2': 35, 'clip_3': 26, 'clip_4': 27, 'clip_5': 39, 'clip_6': 27}
#     for clip_no, num_sylls in clip_dict.items():
#         clip_path = f'//data/candidates/{clip_no}.wav'
#         create_diff_speed_versions(fpath=clip_path, dest_path=dest_path_folder, num_syll=num_sylls)