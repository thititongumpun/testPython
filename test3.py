import requests
from bs4 import BeautifulSoup
import json
import re

url = 'https://www.nice.org.uk/guidance/ta558/history'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')




# print(soup)  //test
# print(soup.prettify())  //test

# print title DONE
#########################################################################
titles = []
for i in soup.find_all('h3', {'class': 'h5'}):
    if i.text:
        titles.append(i.text)
# for a in range(len(titles)):  //test
    # title = json.dumps(titles)
    # print('title:',titles[a]) //test
#########################################################################        

####### print pdf title
#########################################################################
links_with_text = []
for a in soup.find_all('a', {'class': 'track-link'}):
    if a.text:         
        links_with_text.append(a.text)
        reduceSize = [i.replace(' ', '') for i in links_with_text]
        splitSize = [j.split() for j in reduceSize]

# for i in range(len(links_with_text)): //test
#     print(splitSize[i]) //test

#########################################################################


####### print pdf url 
#########################################################################

links_with_text = []
for a in soup.find_all('a', {'class': 'track-link'} ,href=True): 
    if a.text: 
        http = 'https://www.nice.org.uk'
        links_with_text.append(http + a['href'])

# for i in range(len(links_with_text)): //test
    # print(links_with_text[i]) //test
#########################################################################

#print pdf size 
#########################################################################
pdfSizes = []
for s in soup.find_all('sup', {'class': 'download-metadata'}):
    if s.text:
        pdfSizes.append(s.text)
        reduceSize = [i.replace(' ', '') for i in pdfSizes]
        removeChar = [j.replace('\n','') for j in reduceSize]

# for t in range(len(reduceSize)): //test
    # print(removeChar[t]) //test
#########################################################################

#print time 
#########################################################################
times = []
for s in soup.find_all('time', {'class': 'data-date'}):
    if s.text:
        times.append(s.text)
        # print(s.text)      //test   
        reduceSpace = [i.replace(u"\u00a0", "") for i in times]
        
# for y in range(len(times)):  //test
    # print(reduceSpace[y]) //test

#########################################################################



###################### store .json ########################################
data = [{
    'title':titles[0],
    'pdf':[
        {
            'title': splitSize[0],
            'pdf': links_with_text[0],            
            'pdf_size': removeChar[0],
            'time': times[0]
        }
    ]
},
{
    'title':titles[1],
    'pdf':[
        {
            'title': splitSize[1],
            'pdf': links_with_text[1],
            'pdf_size': removeChar[1],
            'time': times[1]
        },
        {
            'title': splitSize[2],
            'pdf': links_with_text[2],
            'pdf_size': removeChar[2],
            'time': times[2]
        },
        {
            'title': splitSize[3],
            'pdf': links_with_text[3],
            'pdf_size': removeChar[3],
            'time': times[3]
        },
        {
            'title': splitSize[4],
            'pdf': links_with_text[4],
            'pdf_size': removeChar[4],
            'time': times[4]
        }
    ]
},
{
    'title':titles[2],
    'pdf':[
        {
            'title': splitSize[5],
            'pdf': links_with_text[5],
            'pdf_size': removeChar[5],
            'time': times[5]
        },
        {
            'title': splitSize[6],
            'pdf': links_with_text[6],
            'pdf_size': removeChar[6],
            'time': times[6]
        },
        {
            'title': splitSize[7],
            'pdf': links_with_text[7],
            'pdf_size': removeChar[7],
            'time': times[7]
        },
        {
            'title': splitSize[8],
            'pdf': links_with_text[8],
            'pdf_size': removeChar[8],
            'time': times[8]
        }
    ]
},
{
    'title':titles[3],
    'pdf':[
        {
            'title': splitSize[9],
            'pdf': links_with_text[9],
            'pdf_size': removeChar[9],
            'time': times[9]
        },
        {
            'title': splitSize[10],
            'pdf': links_with_text[10],
            'pdf_size': removeChar[10],
            'time': times[10]
        },
        {
            'title': splitSize[11],
            'pdf': links_with_text[11],
            'pdf_size': removeChar[11],
            'time': times[11]
        },
        {
            'title': splitSize[12],
            'pdf': links_with_text[12],
            'pdf_size': removeChar[12],
            'time': times[12]
        }
    ]
},
{
    'title':titles[4],
    'pdf':[
        {
            'title': splitSize[13],
            'pdf': links_with_text[13],
            'pdf_size': removeChar[13],
            'time': times[13]
        },
        {
            'title': splitSize[14],
            'pdf': links_with_text[14],
            'pdf_size': removeChar[14],
            'time': times[14]
        }
    ]
}]
# print(data)

  
#save json
with open('data.json', 'w') as outFile:
    json.dump(data, outFile, indent = 4)