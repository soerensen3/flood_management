from faker import Faker
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine
import psycopg2
import geoalchemy2
from shapely.geometry import Point

fake = Faker('de_DE')
engine = create_engine('postgresql://docker:docker@localhost:5432/gis')


def create_rows_faker(num=1):
    output = [{
        "vorname": fake.first_name(),
        "nachname": fake.last_name(),
        "geometry": Point(fake.coordinate(7.1, 0.05), fake.coordinate(50.73, 0.05)),
    } for x in range(num)]
    return output


df = pd.DataFrame(create_rows_faker(50))
df.index.name = 'id'

gdf = gpd.GeoDataFrame(df, crs="EPSG:4326")

with engine.connect() as conn:
    gdf.to_postgis('fieldworker', conn, if_exists='replace', index=True)

# 7.1, 50.73
