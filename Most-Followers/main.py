import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('dataset.xlsx')

def create_top5_bar_chart(df, platform_column, platform_name, color, file_name):
    top_entities = df.nlargest(5, platform_column).fillna(0)

    entities = top_entities['Name (English)']
    followers = top_entities[platform_column]
    index = np.arange(len(entities))

    plt.figure(figsize=(10, 6))
    plt.bar(index, followers, color=color, label=f'{platform_name} Followers')

    plt.xlabel('Entities', fontsize=12)
    plt.ylabel('Number of Followers', fontsize=12)
    plt.title(f'Top 5 Entities with Most Followers on {platform_name}', fontsize=14)
    plt.xticks(index, entities, rotation=45, ha='right')
    plt.legend()

    plt.tight_layout()
    plt.savefig(file_name)

platforms = {
    'Twitter': ('X (Twitter) Follower #', 'skyblue'),
    'Facebook': ('Facebook Follower #', 'tomato'),
    'Instagram': ('Instagram Follower #', 'mediumseagreen'),
    'Threads': ('Threads Follower #', 'gold'),
    'YouTube': ('YouTube Subscriber #', 'purple'),
    'TikTok': ('TikTok Subscriber #', 'pink')
}

for platform, (column, color) in platforms.items():
    create_top5_bar_chart(df, column, platform, color, f'top5_{platform.lower()}.png')
