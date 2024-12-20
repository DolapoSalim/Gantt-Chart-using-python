import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime, timedelta

#The part breaks the project/research into detailed phases/sections

sections = [
    #insert all the sections of the project and specify the start and end time
    {"name": "Literature Review", "start": datetime(2024, 11, 1), "end": datetime(2025, 1, 15)},
    {"name": "Proposal Finalization", "start": datetime(2025, 1, 16), "end": datetime(2025, 1, 31)},
    {"name": "Field Surveys Preparation/Desk Validations", "start": datetime(2025, 2, 1), "end": datetime(2025, 3, 15)},
    {"name": "Field Surveys/Model Worflow Design", "start": datetime(2025, 3, 16), "end": datetime(2025, 9, 30)},
    {"name": "Preliminary Data Analysis/Image allocation", "start": datetime(2025, 10, 1), "end": datetime(2025, 12, 31)},
    {"name": "Image Annotation", "start": datetime(2025, 6, 1), "end": datetime(2025, 9, 30)},
    {"name": "Dataset Expansion & Validation", "start": datetime(2025, 10, 1), "end": datetime(2026, 6, 30)},
    {"name": "Model Development (Baseline Models)", "start": datetime(2026, 4, 1), "end": datetime(2026, 9, 30)},
    {"name": "Advanced AI Model Training", "start": datetime(2026, 10, 1), "end": datetime(2027, 6, 30)},
    {"name": "Data Integration & Network Modeling", "start": datetime(2026, 7, 1), "end": datetime(2027, 3, 31)},
    {"name": "Resilience & Stability Analysis", "start": datetime(2027, 4, 1), "end": datetime(2027, 12, 31)},
    {"name": "Thesis Writing (Initial Draft)", "start": datetime(2027, 1, 1), "end": datetime(2027, 6, 30)},
    {"name": "Thesis Writing (Final Draft)", "start": datetime(2027, 7, 1), "end": datetime(2028, 3, 31)},
    {"name": "Publications & Dissemination", "start": datetime(2027, 4, 1), "end": datetime(2028, 6, 30)},
]

#This code makes the plot reverse in order #sections.reverse()

#Plot the chart using matplot
#Set all the features
fig, ax = plt.subplots(figsize=(12, 8)) #Adjust the width and height to your preferences
y_ticks = []
y_labels = []
for i, sections in enumerate(sections):
    start = date2num(sections['start'])
    end = date2num(sections['end'])
    ax.barh(i, end - start, left=start, color='skyblue', edgecolor='black') #Set the color features
    y_ticks.append(i)
    y_labels.append(sections['name'])

#Add some features to confugure the chart
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_labels)
ax.set_xlabel("Timeline")
ax.set_title("PhD Research Gantt Chart")
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Formatting x-axis with dates
ax.xaxis_date()
fig.autofmt_xdate()

plt.tight_layout()
plt.show()