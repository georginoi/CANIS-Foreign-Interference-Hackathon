import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel('dataset.xlsx')

parent_entity_agg = df.groupby('Parent entity (English)')[['X (Twitter) Follower #',
                                                          'Facebook Follower #',
                                                          'Instagram Follower #',
                                                          'Threads Follower #',
                                                          'YouTube Subscriber #',
                                                          'TikTok Subscriber #']].sum()

parent_entity_agg['Total Followers'] = parent_entity_agg.sum(axis=1)

sorted_parent_entities = parent_entity_agg.sort_values('Total Followers', ascending=False)

top_n = 5
top_parent_entities = sorted_parent_entities.head(top_n)

melted_data = top_parent_entities.reset_index().melt(id_vars='Parent entity (English)',
                                                     var_name='Platform',
                                                     value_name='Followers')

melted_data = melted_data[melted_data['Platform'] != 'Total Followers']

plt.figure(figsize=(15, 10))
sns.barplot(x='Followers', y='Parent entity (English)', hue='Platform', data=melted_data)

plt.title('Top Parent Entities and Their Collective Social Media Influence', fontsize=16)
plt.xlabel('Total Followers', fontsize=12)
plt.ylabel('Parent Entity', fontsize=12)
plt.xscale('log')
plt.legend(title='Social Media Platform')
plt.tight_layout()

plt.savefig('total_followers.png')
