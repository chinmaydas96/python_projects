import re
import urllib
import json
zipcode=raw_input("enter your city name or zip code: ")
def get_weather(zipcode):
    end_point = "http://api.worldweatheronline.com/free/v1/weather.ashx?" 
    query = "key=a37fae643df77aa83d88abbc9e8e96194ab242d4&q=" + str(zipcode) + "&num_of_days=0&format=json"
    url = end_point +  query
    json_data = urllib.urlopen(url).read()
    data = json.loads(json_data)
    current_weather = data['data']['current_condition'][0]
    return current_weather


def print_weather(data):
    print """
    Weather : %s 
    Temperatue : %s Celsius
    Wind : %s Kmph %s 
    Humidity : %s 
    Precipitation : %s MM
    """ % (data['weatherDesc'][0]['value'], data['temp_C'], data['windspeedKmph'], data['winddir16Point'], data['humidity'], data['precipMM'])


def main():
    print "\nGetting weather information for your location..."
    data = get_weather(zipcode)
    print_weather(data)


if __name__ == "__main__":
    main()