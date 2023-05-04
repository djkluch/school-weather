import json, requests

#web address builder
class Weatherapi:
  def __init__(self,city,url,data):
    self.city = city
    self.url = url
    self.data = data
    
#set up the website call with inputed city.
  def city_get(self):
    print("What city would you like the tempature for?") 
    print("You can use the name or zip. Or 'Q' to quit")
    name = input()
    #tests for number then sets to lower
    #may not need test for number though
    try:
      name == name.int()
    except:
      self.city = name
    else:
      self.city = name.lower
    return self

  def url_make(self):
    #set basic url info
    base_url='https://api.openweathermap.org/data/2.5/weather'
    appid='dc9e99edbb4e1104a16a1ecde4f5f3d6'
    #combines to full website
    cityurl=f'{base_url}?q={self.city}&units=imperial&APPID={appid}'
    self.url = cityurl
    #sends back full url
    return self
      
  def data_get(self):
    #get the requests from the website
    response = requests.get(self.url)
    new_data = response.json()
    self.data = new_data
    return self

    
#if you need to print the url.
  def print_url(self):
    print(self.url)
    print()

  #show the json data from the website
  def print_raw(self):
    data = json.dumps(self.data,indent=2)
    print(data)
    print()

  #show the temp for the user
  def temp_print(self):
    temp = self.data['main']['temp']
    temp_max = self.data['main']['temp_max']
    print(f'The current temp is : {temp}')
    print(f'The max temp is: {temp_max}')
    print()  

  def tester(self): 
    test = self.data
    try:
      #if an error shows up on the website it will show what you get
     test = test["main"]
    except:
      print('The website has returned an error: ', self.data['message'])
      print()
      main()
    else:
      print("Thank you!\n")
#end of class


#pick a number no text, could be used else where
def num_pick1_5():
  goto = ''
  while goto != '1' and goto != '2' and goto !='3' and goto !='4' and goto !='5':
    goto = input()
    print()
  return goto


def main():
#sets the urlinput
  urlinput = Weatherapi("","","0")
  active = True
  #get city then build info
  urlinput.city_get()
  print()
  test = urlinput.city
  if test == "q":
    print('Thank you, have a great day.')
    quit(main)
  else:
    urlinput.url_make()
    urlinput.data_get()
    urlinput.tester()
  #see what they want.
    while active:
      print('If you would like the temp press 1, the URL link press 2,')
      print('3 for the raw data, to pick a new city press 4,')
      print('or to quit press 5')
      goto = num_pick1_5()
      if goto == '1':
        #calls temp
          urlinput.temp_print()
      elif goto == '2':
        #call url
         urlinput.print_url()
      elif goto == '3':
        #call data returned from a valid pull
        urlinput.print_raw()
      elif goto == '4':
        #start over with new city
         print()
         main()
      elif goto == '5':
        #close
        print('Thank you, have a great day.')
        break


main()
