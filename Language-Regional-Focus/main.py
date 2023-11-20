import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('dataset.xlsx')

def create_pie_chart_with_threshold(data, title, file_name, threshold=0.02):
    fig, ax = plt.subplots()
    labels = [label if pct > threshold else '' for label, pct in zip(data.index, data.values / data.sum())]
    wedges, texts, autotexts = ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
    for text, label in zip(autotexts, labels):
        text.set_visible(bool(label))
    ax.axis('equal')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(file_name)

language_counts = df['Language'].value_counts()
region_counts = df['Region of Focus'].value_counts()

create_pie_chart_with_threshold(language_counts, 'Language Distribution of Entities', 'language_distribution_threshold.png')
create_pie_chart_with_threshold(region_counts, 'Regional Focus of Entities', 'regional_focus_threshold.png')
