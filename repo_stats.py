import pandas as pd
from os import system
from datetime import datetime
import plotly.express as px


def git_shortlog_to_df(flags="-ns") -> pd.DataFrame:
    system(f"git shortlog HEAD {flags} > temp.txt")
    with open("temp.txt", "r") as output:
        lines = output.readlines()
    system('rm -rf temp.txt')

    cleaned_lines = []
    while lines:
        line = lines.pop()
        line = line.strip()
        line = line.split("\t")
        line[0] = int(line[0])  # convert commit count to an int
        cleaned_lines.append(line)

    columns = ["number of commits", "user"]
    df = pd.DataFrame(cleaned_lines, columns=columns)
    return df

if __name__ == "__main__":
    df = git_shortlog_to_df()
    # plot the long (tidy) dataframe
    fig = px.bar(df, x="user", y="number of commits", title=f"code commits per dev as of {datetime.utcnow().date()}", barmode='stack')
    fig.update_layout(xaxis_title='user', yaxis=dict(tickformat="commits", ))
    fig.write_image("stats.png")
