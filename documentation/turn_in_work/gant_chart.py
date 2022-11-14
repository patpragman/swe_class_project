import plotly.express as px
import pandas as pd
import plotly.io as pio

df = pd.DataFrame([
    dict(Task="Sprint 1 - Refactoring / Housekeeping", Start='2023-01-16', Finish='2023-01-31'),
    dict(Task="Sprint 2 - 3 - Relational Database Migration", Start='2023-02-01', Finish='2023-02-28'),
    dict(Task="Sprint 4 - Move to Permanent Hosting", Start='2023-03-01', Finish='2023-03-15'),
    dict(Task="Sprint 5 - Image, Sound, and Video Feature", Start='2023-03-16', Finish='2023-03-31'),
    dict(Task="Sprint 6 - Front-End Support for Images, Sounds, and Video", Start='2023-04-01', Finish='2023-04-15'),
    dict(Task="Sprint 7 - Card Sharing Functionality", Start='2023-04-15', Finish='2023-04-22'),
    dict(Task="Sprint 7.5 - Budgeted Refactoring Time", Start='2023-04-22', Finish='2023-04-30'),
    dict(Task="Sprint 8 - Data Product Construction", Start='2023-05-01', Finish='2023-05-15'),
    dict(Task="Sprint 9 - Maintenance / Cleaning / Documentation", Start='2023-05-15', Finish='2023-05-30'),
    dict(Task="Total Time", Start='2023-01-16', Finish='2023-05-30'),
])


fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up

with open("gant.html", "w") as write_file:
    write_file.write(fig.to_html())

pio.write_image(fig, "gant.png")