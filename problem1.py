# Problem 1: Salary Conversion
# David Khowanto
# I think this problem doesn't need oop for testing

## Import Libraries
import json
import requests
from collections import defaultdict, Counter

## Returns list of JSON from url / API
def getJsonListFromApi(url):
  return json.loads(requests.get(url).text)

## Main logic for salary conversion
def salaryInversion(json_file, json_url):
  # Get data from JSON file
  f = open(json_file)
  data_file = json.load(f)['array']
  f.close()

  # Get data from JSON url
  data_url = getJsonListFromApi(json_url)

  # Join fetched data from url with JSON file
  temp_dict = defaultdict(dict)
  for item in data_file + data_url:
      temp_dict[item['id']].update(item)

  # convert defaultdict to list
  res = list(temp_dict.values())

  # fetch USD to IDR value
  IDR_to_USD = getJsonListFromApi("https://free.currconv.com/api/v7/convert?q=USD_IDR&compact=ultra&apiKey=7ee2137263fa8f4c0d82")["USD_IDR"]

  # add 'salaryInUSD' field
  # remove 'company' and 'website' field
  for d in res:
      d['salaryInUSD'] = d['salaryInIDR'] / IDR_to_USD
      d.pop('website', None)
      d.pop('company', None)

  # Print final data
  return(res)

## test expected fields in endpoint
def testEndpointOutput(endpoint): 
  # Output from the endpoint should be: id, name, username, email, address, phone, salary in IDR, and salary in USD
  expected_output = ['id', 'name', 'username', 'email','address', 'phone', 'salaryInIDR', 'salaryInUSD']
  # Output final JSON Data
  print("Output:", json.dumps(endpoint, indent=4))
  # assert JSON keys
  for elmt in endpoint:
    try:
      assert Counter(expected_output) == Counter(list(elmt.keys()))
    except:
      print("id", elmt["id"], "don't have one or more field")
    else:
      print("test with id", elmt["id"], "succeed")

## Run the test
testEndpointOutput(salaryInversion('JSON Files/salary_data.json', "http://jsonplaceholder.typicode.com/users"))
