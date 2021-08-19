import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html').content

soup = BeautifulSoup(webpage, 'html.parser')

#print(soup)
rating_tag = soup.find_all(attrs = {'class': 'Rating'})
# print(rating_tag)

ratings = []
for rate in range(1, len(rating_tag)):
   rate_text = rating_tag[rate].get_text()
   rate_float = float(rate_text)
   ratings.append(rate_float)

plt.hist(ratings)
plt.show()

companies = soup.select('.Company')
# print(companies)
company = []
for comp in companies[1:]:
  company_text = comp.get_text()
  company.append(company_text)
 
# print(company)

cocoa = soup.select('.CocoaPercent')
percentage_of_cocoa = []


for coc in cocoa[1:]:
  cocoa_text = coc.get_text()
  cocoa_float_strip = float((cocoa_text).strip('%'))
  percentage_of_cocoa.append(cocoa_float_strip) 

print(len(percentage_of_cocoa))
data = {'Company': company, 'Ratings': ratings, 'Cocoa': percentage_of_cocoa}

df = pd.DataFrame(data)
print(df.head())

mean_rate = df.groupby('Company').Ratings.mean()
top_10 = mean_rate.nlargest(10)
print(top_10)
plt.clf()
plt.scatter(df.Cocoa, df.Ratings)
z = np.polyfit(df.Cocoa, df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(df.Cocoa, line_function(df.Cocoa), "r--")
plt.show()







