import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

def get_lat_lon(region):
    region_coords = {
        "Anglosphere": (53.0, -0.8),
        "China": (35.8617, 104.1954),
        "Afghanistan": (33.9391, 67.7100),
        "Yunnan": (24.4753, 101.3431),
        "Switzerland": (46.8182, 8.2275),
        "Austria": (47.5162, 14.5501),
        "Indonesia": (-0.7893, 113.9213),
        "UAE": (23.4241, 53.8478),
        "EU": (50.8503, 4.3517),
        "France": (46.2276, 2.2137),
        "African Union": (9.1450, 40.4897),
        "Cyprus": (35.1264, 33.4299),
        "Lesotho": (-29.6100, 28.2336),
        "Iran": (32.4279, 53.6880),
        "Serbia": (44.0165, 21.0059),
        "Saudi Arabia": (23.8859, 45.0792),
        "Burundi": (-3.3731, 29.9189),
        "Cameroon": (7.3697, 12.3547),
        "Dem. Rep. of Congo": (-4.0383, 21.7587),
        "Chad": (15.4542, 18.7322),
        "Italy": (41.8719, 12.5674),
        "USA": (37.0902, -95.7129),
        "Bulgaria": (42.7339, 25.4858),
        "Trinidad and Tobago": (10.6918, -61.2225),
        "Japan": (36.2048, 138.2529),
        "Egypt": (26.8206, 30.8025),
        "Poland": (51.9194, 19.1451),
        "Suriname": (3.9193, -56.0278),
        "South Korea": (35.9078, 127.7669),
        "Pakistan": (30.3753, 69.3451),
        "UK": (55.3781, -3.4360),
        "Qatar": (25.3548, 51.1839),
        "Shanghai": (31.2304, 121.4737),
        "MENA": (34.8021, 38.9968),  # Middle East and North Africa
        "Jiangxi": (27.0875, 114.9042),
        "Beijing": (39.9042, 116.4074),
        "Hong Kong": (22.3193, 114.1694),
        "la Francophonie": (48.8566, 2.3522),  # Represented by Paris, France
        "Russia": (61.5240, 105.3188),
        "Kenya": (-0.0236, 37.9062),
        "Finland": (61.9241, 25.7482),
        "Tanzania": (-6.3690, 34.8888),
        "Spain": (40.4637, -3.7492),
        "Somalia": (5.1521, 46.1996),
        "India": (20.5937, 78.9629),
        "Maldives": (3.2028, 73.2207),
        "Zimbabwe": (-19.0154, 29.1549),
        "Nigeria": (9.0820, 8.6753),
        "Colombia": (4.5709, -74.2973),
        "Netherlands": (52.1326, 5.2913),
        "Ukraine": (48.3794, 31.1656),
        "Fujian": (26.4837, 117.9249),
        "ASEAN": (1.3521, 103.8198),  # Represented by Singapore
        "Belgium": (50.5039, 4.4699),
        "South Africa": (-30.5595, 22.9375),
        "UN": (40.7489, -73.9680),  # Represented by New York City, USA
        "Samoa": (-13.7590, -172.1046),
        "New Zealand": (-40.9006, 174.8860),
        "Germany": (51.1657, 10.4515),
        "Canada": (56.1304, -106.3468),
        "Kazakhstan": (48.0196, 66.9237),
        "Türkiye": (38.9637, 35.2433),
        "Australia": (-25.2744, 133.7751),
        "Greece": (39.0742, 21.8243),
        "South Sudan": (6.8769, 31.3069),
        "Ethiopia": (9.1450, 40.4897),
        "Chile": (-35.6751, -71.5430),
        "Dominican Republic": (18.7357, -70.1627),
        "Algeria": (28.0339, 1.6596),
        "Angola": (-11.2027, 17.8739),
        "Antigua and Barbuda": (17.0608, -61.7964),
        "Argentina": (-38.4161, -63.6167),
        "Malawi": (-13.2543, 34.3015),
        "Albania": (41.1533, 20.1683),
        "Bahrain": (26.0667, 50.5577),
        "Rep. of Congo": (-0.2280, 15.8277),
        "Croatia": (45.1, 15.2),
        "Eritrea": (15.1794, 39.7823),
        "Grenada": (12.1165, -61.6790),
        "Ghana": (7.9465, -1.0232),
        "Mauritania": (21.0079, -10.9408),
        "Rwanda": (-1.9403, 29.8739),
        "Ireland": (53.4129, -8.2439),
        "Kuwait": (29.3117, 47.4818),
        "Malta": (35.9375, 14.3754),
        "Philippines": (12.8797, 121.7740),
        "Namibia": (-22.9576, 18.4904),
        "Peru": (-9.1900, -75.0152),
        "Portugal": (39.3999, -8.2245),
        "Sri Lanka": (7.8731, 80.7718),
        "Slovakia": (48.6690, 19.6990),
        "Slovenia": (46.1512, 14.9955),
        "Denmark": (56.2639, 9.5018),
        "Lebanon": (33.8547, 35.8623),
        "Iraq": (33.2232, 43.6793),
        "Mali": (17.5707, -3.9962),
        "Guinea": (9.9456, -9.6966),
        "Senegal": (14.4974, -14.4524),
        "Djibouti": (11.8251, 42.5903),
        "Morocco": (31.7917, -7.0926),
        "Gambia": (13.4432, -15.3101),
        "Fiji": (-17.7134, 178.0650),
        "Papua New Guinea": (-6.3149, 143.9555),
        "Uganda": (1.3733, 32.2903),
        "Thailand": (15.8700, 100.9925),
        "Jordan": (30.5852, 36.2384),
        "Hungary": (47.1625, 19.5033),
        "Montenegro": (42.7087, 19.3744),
        "Yemen": (15.5527, 48.5164),
        "Estonia": (58.5953, 25.0136),
        "Liberia": (6.4281, -9.4295),
        "Sudan": (15.5007, 32.5599),
        "Hubei": (30.9756, 112.2707),
        "Brazil": (-14.2350, -51.9253),
        "Mongolia": (46.8625, 103.8467),
        "Botswana": (-22.3285, 24.6849),
        "Xinjiang": (41.1129, 85.2401),
        "Ecuador": (-1.8312, -78.1834),
        "El Salvador": (13.7942, -88.8965),
        "Uruguay": (-32.5228, -55.7658),
        "Tonga": (-21.1789, -175.1982),
        "Cuba": (21.5218, -77.7812),
        "Equatorial Guinea": (1.6508, 10.2679),
        "Mexico": (23.6345, -102.5528),
        "Panama": (8.5380, -80.7821),
        "Venezuela": (6.4238, -66.5897),
        "Guangxi": (23.7248, 108.8076),
        "Henan": (34.2904, 113.3824),
        "Iceland": (64.9631, -19.0208),
        "São Tomé and Príncipe": (0.1864, 6.6131),
        "Hunan": (27.6253, 111.8569),
        "Jiangsu": (32.0603, 118.7969),
        "Chongqing": (29.4316, 106.9123),
        "Lithuania": (55.1694, 23.8813),
        "Zhejiang": (29.1416, 119.7889),
        "Jilin": (43.8378, 126.5494),
        "Hispanophone": (40.4637, -3.7492),  # Represented by Spain as a central location
        "Mauritius": (-20.3484, 57.5522),
        "Costa Rica": (9.7489, -83.7534),
        "Myanmar": (21.9162, 95.9560),
        "Lusophone": (-14.2350, -51.9253),  # Represented by Brazil as a central location
        "Nepal": (28.3949, 84.1240),
        "Czech Rep.": (49.8175, 15.4730),
        "Hainan": (19.5664, 109.9497),
        "Shaanxi": (35.1917, 108.8701),
        "Israel": (31.0461, 34.8516),
        "Sichuan": (30.2638, 102.8055),
        "East African Community": (-6.3690, 34.8888),  # Represented by Tanzania as a central location
        "Guangdong": (23.3790, 113.7633),
        "Tibet": (29.6469, 91.1172),
        "Shandong": (36.6683, 117.0204),
        "Bolivia": (-16.2902, -63.5887),
        "Norway": (60.4720, 8.4689),
        "Barbados": (13.1939, -59.5432),
        "Belarus": (53.7098, 27.9534),
        "Laos": (19.8563, 102.4955),
        "Kyrgyzstan": (41.2044, 74.7661),
        "Latvia": (56.8796, 24.6032),
        "Anhui": (31.8612, 117.2841),
        "Heilongjiang": (47.8610, 127.7615),
        "Gansu": (37.8107, 101.0587),
        "Taiwan": (23.6978, 120.9605),
        "Shanxi": (37.5777, 112.2922),
        "Vietnam": (14.0583, 108.2772),
        "Malaysia": (4.2105, 101.9758),
        "Romania": (45.9432, 24.9668),
        "Bangladesh": (23.6850, 90.3563),
        "Cambodia": (11.5564, 104.9282),
        "Guyana": (4.8604, -58.9302),
        "North Macedonia": (41.6086, 21.7453),
        "Sierra Leone": (8.4606, -11.7799),
        "Singapore": (1.3521, 103.8198),
    }
    return region_coords.get(region, (None, None))


df = pd.read_excel('dataset.xlsx')

df['X (Twitter) Follower #'] = pd.to_numeric(df['X (Twitter) Follower #'], errors='coerce')
df['Facebook Follower #'] = pd.to_numeric(df['Facebook Follower #'], errors='coerce')
df['Instagram Follower #'] = pd.to_numeric(df['Instagram Follower #'], errors='coerce')
df.fillna(0, inplace=True)

df['lat'], df['lon'] = zip(*df['Region of Focus'].apply(get_lat_lon))

df = df.dropna(subset=['lat', 'lon'])

plt.figure(figsize=(15, 7.5))

m = Basemap(projection='robin', lon_0=0, resolution='c')

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray', lake_color='aqua')

m.drawmapboundary(fill_color='aqua')
m.drawmeridians(np.arange(-180, 180, 30), labels=[True,False,False,True])
m.drawparallels(np.arange(-90, 90, 30))

df['marker_size'] = (df['X (Twitter) Follower #'] + df['Facebook Follower #'] + df['Instagram Follower #']) / 10000
df['marker_size'] = df['marker_size'].apply(lambda x: max(x, 5))

for _, row in df.iterrows():
    x, y = m(row['lon'], row['lat'])
    m.scatter(x, y, s=row['marker_size'], alpha=0.7, edgecolor='black', linewidth=0.5)

plt.title('Social Media Presence Map of Entities')

plt.savefig("social_media_presence_map2.png")