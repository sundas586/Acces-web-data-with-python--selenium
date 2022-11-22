'''
step 1 : import all libraries
'''
import requests
from bs4 import BeautifulSoup
import re
'''
step 2 : Fetch HTML contents of given url as string
'''
url = input("url please : ") #"https://sundas-portfolio.herokuapp.com/"
r = requests.get(url) # get request for desired url
htmlContent = r.content
'''
step 3 : Parse the HTML string
'''
# it will parse through html string/ content and then show the content in a proper structure like
soup = BeautifulSoup(htmlContent, "html.parser")
#print(soup)
#print(soup.prettify) # to see even more properly
'''
step 4 : HTML tree traversal
'''
#_________ Below are all examples of traversing html tree using beautiful soup

# get the title of HTML page
urlTitle = soup.title
#print(urlTitle)

# get all the paragraphs of html page
paras = soup.find_all('p')
#print(paras)

# to find elements by class name
mydivs = soup.find_all("div", {"class": "progress"})
#or
#mydivs = soup.find_all("div", class_= progress)
#print(mydivs)

my_italic = soup.find_all("i", {"class": "val"})
#or
#my_italic = soup.find_all("i", class_= "val")
#print(my_italic)

#Find all names of classes of a paragraphs
my_classes = soup.find('i')['class']
#print(my_classes)

# get text of paragraphs
#print(soup.find('p').get_text())
# alas! its giving only first most text of first most paragraph

# get text of paragraphs
#print(soup.find('p', class_="description").get_text())
# alas! its giving only first most text of first most paragraph of class = description


# getting all the paragraphs
#using for loop worked, but the result is not in a list format
#for para in soup.find_all("p"):
#    print(para.get_text())

# to get the all texts of whole soup(HTML page)
txt = soup.get_text()
#print(txt)


# get all the anchor tags of html page
anchorTags = soup.find_all('a')
#print(anchorTags)

# get all the anchor tags of html page only containig https:// links only (gives in a list)
links = soup.find_all("a", href=re.compile("https://"))
#print(links)

# get links in anchor tags of html page (not in a list)
#for links in anchorTags :
#    print(links.get('href'))
# as it is giving me all the links, which also includes the links that do not take me any where to new web page ,and the links that are repeated more than once e.g :
# index.html
# #about
# #contact
# #
# #
# /static/img/certifications/STAT_.jpg
# /static/img/certifications/STAT_.jpg
# /static/img/certifications/LA_.jpg
# /static/img/certifications/LA_.jpg
# index.html
# ....

# get all links in html page, but not the # links and no repeated links,
# to ignore repeated links, we will save all links in a set, so set will automatically delete repeated links, which a list type do not do.
#links = soup.find_all("a", href=re.compile("https://"))#
#all_links = set()
#for i in links :
#    if(i.get('href') != '#'):   # not necessary to specify this statment as re. is already givig us https:// links only
#        all_links.add(i.get('href'))
#print(all_links)
# now it gives only https:// links and also non-repitative

# # Find children of an element
# id = soup.find("ul", {"id":"portfolio-flters"})
# children = id.findChildren() # returns child elements list
# # Print all children of an element
# for child in children:
#     print(child)