import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

speeds = [4, 5.5, 7, 8.5, 10, 11.5]


def create_heatmap(participant_list, vmax, plot_data, plot_name):
    heatmap_df = pd.DataFrame(plot_data, columns=speeds, index=participant_list)
    plt.subplots(figsize=(9, 7))
    ax = sns.heatmap(heatmap_df,
                          cmap="PuRd",
                          vmin=0, vmax=vmax, annot=True, yticklabels=5)
    ax.set_xlabel("\nSpeed in syll/sec")
    ax.set_ylabel("\nParticipant")
    ax.set_title(plot_name)
    plt.show()


def create_correlation_scatterplot(title, xlabel, ylabel, x_df, y_df):
    colors = ['silver', 'lightgreen', 'lightblue', 'plum', 'gold', 'red']
    fig = plt.figure()
    ax = fig.subplots()

    for c, speed in zip(colors, speeds):
        x_col = x_df[str(speed)]
        y_col = y_df[str(speed)]

        ax.scatter(x_col, y_col, c=c, marker='o')

    ax.grid(linestyle=':', linewidth=2, alpha=0.2)
    ax.set_xlabel(f'\n{xlabel}')
    ax.set_ylabel(f'\n{ylabel}')
    ax.set_title(f'\n{title}')
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.legend(speeds)

    plt.show()

if __name__ == '__main__':
    #Plotting transcription grades
    plot_name = "Transcription grade for each speed per participant"
    transcription_file = "data/transcription_grade_floats.csv"
    df = pd.read_csv(transcription_file)
    participant_list = [i for i in range(0, 30)]
    val_cols = df.loc[:, df.columns!='Participant']
    val_cols = val_cols.to_numpy()
    #print(val_cols)
    create_heatmap(participant_list=participant_list, vmax=1, plot_data=val_cols, plot_name=plot_name)

    # Plotting quality scores
    # plot_name = "Intelligibility score for each speed per participant"
    # int_file = "data/intelligibility_for_csv.csv"
    # df = pd.read_csv(int_file)
    # val_cols = df.to_numpy()
    # #print(val_cols)
    # create_heatmap(participant_list=participant_list, vmax=5, plot_data=val_cols, plot_name=plot_name)
    # transcription_df = pd.read_csv(transcription_file)
    # Scatter plot quality vs. intelligibility
    # quality_file = 'data/quality_for_csv.csv'
    # int_df = pd.read_csv(int_file)
    # quality_df = pd.read_csv(quality_file)
    # create_correlation_scatterplot(title="Intelligibility Scores vs. Transcription Grades", ylabel="Intelligibility Score",
    #                                xlabel="Transcription Grade", y_df=int_df, x_df=transcription_df)