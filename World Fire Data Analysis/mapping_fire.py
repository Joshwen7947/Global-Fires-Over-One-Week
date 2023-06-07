import csv  
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#
with open("data/world_fires_7_day.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    
    # 0 - latitide
    # 1 - longitude
    longitudes, latitudes = [],[]
    for row in reader:
        try:
            latitude = float(row[0])
            longitude = float(row[1])
        except ValueError:
            print("Some Error")
        else:
            longitudes.append(longitude)
            latitudes.append(latitude)
            
data = [Scattergeo(lon=longitudes, lat=latitudes)]
design = Layout(title="World Fires Over 7 Days")
fig = {"data":data,"layout":design}
offline.plot(fig, filename="fires.html")
