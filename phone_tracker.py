import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Replace 'number' with the actual phone number you want to lookup
number = "+2783798290"  # Replace with your phone number

pepnumber = phonenumbers.parse(number, "US")

location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Get carrier information
service_pro = phonenumbers.parse(number, "US")
print(carrier.name_for_number(service_pro, "en"))

# OpenCageGeocode setup
key = 'f9719fffa03f4d5eb1304ff5a581f14a'
geocoder = OpenCageGeocode(key)

query = " ".join(location.split())
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

# location html file will be created which will store the location
myMap.save("location_test.html")
