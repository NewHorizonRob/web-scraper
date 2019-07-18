# Robert Thomas
# AIST 2120
# Homework 6
# 7/3/19
# downloadxkcd.py


import requests, os, bs4   #imports the requests, os and beautiful soup modules

url = 'http://xkcd.com'         # assigns the webiste url in a string to the variable name url
os.makedirs('xkcd', exist_ok=True) # puts the photos in the xkcd folder


while not url.endswith('#'): # while loop condition runs as long as url doesnt end with a #
    print('Downloading Page %s...' % url) #print statement with the url formatted in 
    res = requests.get(url) # download request from the url 
    res.raise_for_status() # checks to see if there is a bad download within the url

    soup = bs4.BeautifulSoup(res.text) #creates a beautiful soup object named soup

    
    comicElem = soup.select('#comic img') # looks for the img attribute in the webpage
    if comicElem == []: # if the list is empty run the code block below
        print('Could not find image')
    else:
        comicUrl = 'http:' + comicElem[0].get('src') # 
        print('Downloading image %s...' % (comicUrl)) # print statement with new url formatted in 
        res = requests.get(comicUrl) # download request for new url
        res.raise_for_status() # checks to see if there is a bad download within the url

    
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') #opens the file in write binary mode 
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # gets the previous button's url
    prevLink = soup.select('a[rel="prev"]')[0] 
    url = 'http://xkcd.com' + prevLink.get('href')

