import requests

# response = requests.get("https://google.com")
# aaa = response.text
# print(aaa) 
rating_pages = []
for i in range(5):
    url = "index?year=2010&month=1&weekIndex={}".format(i)
    response = requests.get(url)
    rating_page = response.text 
    rating_pages.append(rating_page)

print(len(rating_pages))
print(rating_pages[0])
