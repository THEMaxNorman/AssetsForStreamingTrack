import _tkinter as tk
from bs4 import BeautifulSoup
import urllib2
import itertools
ua = 'https://www.athletic.net/TrackAndField/Print/EntryMeet.aspx?Meet=319755&t=ivhwc'
def editFile(file,string):
    f = open(file,'w')
    f.write(string)
    f.close()
def getRace(url):
    u = urllib2.urlopen(url)
    soup = BeautifulSoup(u, "html5lib")
    allTDs = soup.find_all('td')
    end = []
    for x in allTDs:

        txt = x.text

        if (txt != u''):
            if txt == u'V':
                txt = '\n'
            if txt == 'JV':
                txt = '\n'
            end.append(txt)

    return end[10:]
def sepRace(lst):
    spl = [list(y) for x, y in itertools.groupby(lst, lambda z: z == u'\xa0') if not x]
    return spl
def comb(list):
    text = ""
    for x in list:
        text += x
        text += ' '
    return text






ls = getRace(ua)
print ls
listOfRaces = sepRace(ls)
editFile("test.txt",comb(listOfRaces[2]))



