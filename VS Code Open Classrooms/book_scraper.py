import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')


#product_page_url
product_page_url = soup.find_all('h1', class_='table table-striped')

universal_product_code = soup.find_all('th', class_='table table-striped')
print(universal_product_code)
#book_title
#price_including_tax
#price_excluding_tax


quantity_available = soup.find_all('p', class_='instock availability')
quantities=[]
for quantity in quantity_available:
    quantities.append(quantity.string)



#print(quantity_available)

#product_description
#category
#review_rating()
#image_rl




"""

#Create list for the headers
headers = ["title", "description"]

#Open a new file to write to called ‘data.csv’
with open('data.csv', 'w', newline='') as csvfile:
    #Create a writer object with that file
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    #Loop through each element in titles and descriptions lists
    for i in range(len(titles)):
        #Create a new row with the title and description at that point in the loop
        row = [titles[i], descriptions[i]]
        writer.writerow(row)

 """