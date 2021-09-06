import phonenumbers
import folium

from myNumber import number

from phonenumbers import geocoder
key = '1791780aa37f41b8afbe7846eed7b018'

samNumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(samNumber, 'en')
print(yourlocation)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourlocation)
result = geocoder.geocode(query)
print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)
myMap = folium.Map(location=[lat,lng], zoom_start = 9)

folium.Marker([lat, lng], popup = yourlocation).add_to((myMap))

##save map in html file

myMap.save('mylocation.html')

