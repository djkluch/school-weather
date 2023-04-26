import json, requests

#web address builder
class Weatherapi:
  def __init__(self,city,url,data):
    self.city = city
    self.url = url
    self.data = data
    
#set up the website call with inputed city.
  def city_get(self):
    name = input("What city would you like the tempature for?")
    self.city = name
    #set basic url info
    base_url='https://api.openweathermap.org/data/2.5/weather'
    appid='dc9e99edbb4e1104a16a1ecde4f5f3d6'
    #combine
    cityurl=f'{base_url}?q={self.city}&units=imperial&APPID={appid}'
    self.url = cityurl
    #sends back city and url
    return self
    
#if you need to print the city and url.
  def print_url(self):
    print(self.url)
    print(self.city)
    print(self.data)
    
  def url_get(self):
     
    #webcall = self.url
    response = requests.get(self.url)
    new_data = response.json()
    return new_data

  def tester(self): 
    test = self.data
   # print(unformated_date)
    try:
     test = test["main"]
    except:
      print("not valid")
    else:
      temp=self.data["main"]["temp"]
    temp_max = self.data["main"]["temp_max"]
    print(f'The current temp is : {temp}')
    print(f'The max temp is: {temp_max}')
  


def main():
#sets the urlinput
  urlinput = Weatherapi("","","0")
#set up a loop here now.
  urlinput.city_get()
 # urlinput.print_url()
#get the data unformated
  infodata = urlinput.url_get()
  urlinput.print_url()
  print(infodata)



main()