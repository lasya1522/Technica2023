import geopy as gp
from geopy.geocoders import Nominatim
import pandas as pd
import matplotlib.pyplot as plt
from geopy.extra.rate_limiter import RateLimiter

loc = Nominatim(user_agent="Geopy Library")

# entering the location name(testing)
getLoc = loc.geocode("3854 Stadium Drive College Park Maryland")

# printing latitude and longitude
print("Latitude = ", getLoc.latitude)
print("Longitude = ", getLoc.longitude)

df = pd.read_csv('crime_data.csv')
df.drop(columns=["Unnamed: 0"], inplace=True)
df = df.replace(to_replace=r"AM", value="", regex=True)
df = df.replace(to_replace=r"PM", value="", regex=True)
df = df.replace(to_replace=r"Blk ", value="", regex=True)
df["Time_of_Incident"] = df["Time_of_Incident"].apply(pd.to_datetime, errors="coerce")
df["Time_of_report"] = df["Time_of_report"].apply(pd.to_datetime, errors="coerce")
df["Time_of_Incident"] = df["Time_of_Incident"].apply(pd.to_datetime, errors="coerce", utc=True)
df = df.dropna()

df['month_year'] = df['Time_of_Incident'].dt.to_period('M')

loc = Nominatim(user_agent="Geopy Library")

geocode = RateLimiter(loc.geocode, min_delay_seconds=5)

df["lat_lon"] = df["Location"].apply(lambda x: loc.geocode(x))
df.to_csv("location_data.csv")