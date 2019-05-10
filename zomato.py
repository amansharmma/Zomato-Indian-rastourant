from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://www.zomato.com/indore'

def request(url):
	driver = webdriver.Chrome()
	driver.get(url)
	response = driver.execute_script("return document.documentElement.outerHTML")
	driver.quit()
	soup = BeautifulSoup(response,'html.parser')
	return (soup)
soup = (request(url))
you1=[]
search = soup.find("div",class_="ui segment row")
c = search.find_all('a',class_="col-l-1by3 col-s-8 pbot0")
a = 0
url = []
for j in c:
	url.append(j["href"])
	k = ((j.span).text)
	var = (j.text)
	v = ""
	a += 1
	for h in var :
		if ("(") == h :
			break
		else :
			v = v + h
	print (str(a) + "   " + v.strip() + "  " + k + "\n")
user = input("Type place here ====>>  ")
d = request(url[int(user)-1])
q = d.find_all("div",{"class":"fontsize1 semi-bold mt2"})
a = 0
for r in q :
	a += 1
	print (str(a) + "   " + (r.text.strip()) + "  " + "\n")
l = []
z = d.find_all("div",{"class": "white-bg sub-cat-container mbot "})
for o in z :
	f = o.find("div",{"class": "pb5 bt ptop0 ta-right"})
	l.append(f.find("a").get("href"))
user2 = int(input("What do you want ====>>  "))
y = request(l[(user2)-1])
new = y.find_all('div',class_='js-search-result-li even status 1')
dic = {}
list1 = []
for i in new:
	data=i.find("div",class_="col-s-16 col-m-12 pl0 ")
	main=data.find("div",class_="col-s-12").find('a',class_='result-title hover_feedback zred bold ln24 fontsize0 ')
	dic["name"] = (main.text.strip())
	rat=i.find("div",class_="ta-right floating search_result_rating col-s-4 clearfix")
	rating=rat.find("div")
	new_rating=(rating.text).strip()
	dic["rating"] = ((new_rating))
	cost=i.find("span",class_="col-s-11 col-m-12 pl0")
	dic["cast"] = (cost.text.strip())
	list1.append(dic.copy())
pprint (list1)