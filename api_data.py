import requests

url = "http://universities.hipolabs.com/search?country=Kenya"
response = requests.get(url)
data = response.json()

# Filter universities with 'Technology' in their name
tech_universities = [uni for uni in data if "Technology" in uni["name"]]

for uni in tech_universities:
    print(uni["name"], "--------", uni["web_pages"][0],  "--------", uni["domains"][0])
