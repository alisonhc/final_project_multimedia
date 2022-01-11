import random

all_combos = []

clip_ids = [1, 2, 3, 4, 5, 6]
speeds = [4, 5.5, 7, 8.5, 10, 11.5]

# for i in range(len(speeds)):
#     lst = []
#     for j in range(len(clip_ids)):
#         lst.append((speeds[i], clip_ids[j]))
#     all_combos.append(lst)
# print(all_combos)

ALL_POSSIBLE_PAIRS = [[(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)],
                      [(5.5, 1), (5.5, 2), (5.5, 3), (5.5, 4), (5.5, 5), (5.5, 6)],
                      [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)],
                      [(8.5, 1), (8.5, 2), (8.5, 3), (8.5, 4), (8.5, 5), (8.5, 6)],
                      [(10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6)],
                      [(11.5, 1), (11.5, 2), (11.5, 3), (11.5, 4), (11.5, 5), (11.5, 6)]]


def get_clips_for_a_participant():
    selected_pairs = []
    for i in range(len(ALL_POSSIBLE_PAIRS)):
        speed_pairs = ALL_POSSIBLE_PAIRS[i]
        pair_ind = random.choice(range(len(speed_pairs)))
        selected_pairs.append(speed_pairs[pair_ind])
        if i < len(ALL_POSSIBLE_PAIRS) - 1:
            for lst in ALL_POSSIBLE_PAIRS:
                lst.pop(pair_ind)
    random.shuffle(selected_pairs)
    return selected_pairs

# print(list(itertools.product(speeds, clip_ids)))
print(get_clips_for_a_participant())