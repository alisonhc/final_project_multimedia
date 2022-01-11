import statistics
import pandas as pd

fname = 'data/transcription_grades.csv'

new_dict = {}
transcription_df = pd.read_csv(fname)
speeds = [4, 5.5, 7, 8.5, 10, 11.5]
for speed in speeds:
    grades = transcription_df[f"Speed {speed}"]
    the_sum = 0
    #print(len(grades))
    grade_list = []
    for grade in grades:
        #print(grade)
        if grade != '0':
            split_grade = grade.split('/')
            grade_list.append(int(split_grade[0]) / int(split_grade[1]))
        else:
            grade_list.append(0)
    #print(speed, statistics.median(grade_list))
    new_dict[f"Speed {speed}"] = grade_list
    assert len(grades) == len(grade_list)
    av = sum(grade_list) / len(grades)
    print(speed, av)

# new_df = pd.DataFrame.from_dict(new_dict)
# new_df.to_csv('data/transcription_grade_floats.csv')


