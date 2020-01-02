import requests
from bs4 import BeautifulSoup
import pandas as pd

# TODO: Разделить функционал при переносе
base_url = "https://www.24tr.ru"
user_agent = {'User-agent': 'Mozilla/5.0'}
tram_url = "/krasnodar/tramvay/"

print(base_url + tram_url)
r = requests.get(base_url + tram_url, headers=user_agent)
print(r)
c = r.content
soup = BeautifulSoup(c, 'html.parser')
one_dir = ['7', '12', '22']
l = []
o = []
r = []
t = []
p = []
routes = []
direct_stations = []
two_ways_routes = []
for i in soup.findAll("div", {"class": "numberlist"}):
    for b in i.find_all('a', href=True):
        print(b.get('href'))
        routes.append(b.text)
        if b.text not in one_dir:
            two_ways_routes.append(b.text)
        r = requests.get(base_url + b.get('href'), headers=user_agent)
        print(r)
        c = r.content
        soup = BeautifulSoup(c, 'html.parser')
        table = soup.find("table", {"class": "table table-striped m-b-none"})
        for row in table.find_all("tr"):
            for td in row.find_all("td"):
                if b.text not in one_dir:
                    l.append(td.text.replace('Прямой путь маршрута:', ''))
                else:
                    o.append(td.text.replace('Путь маршрута:', ''))

j = l[::11]
r = l[1::11]

for i in j:
    direct_stations.append(i.lstrip().rstrip())

for i in r:
    t.append(i.replace('Обратный путь маршрута:', '').lstrip().rstrip())

with open("Directpath.txt", "w", encoding="utf-8") as f:
    for item in j:
        f.write("%s\n" % item)
with open("Reversepath.txt", "w", encoding="utf-8") as f:
    for item in t:
        f.write("%s\n" % item)

s = o[::10]
for i in s:
    # .replace('\n\r\n','')
    p.append(i.lstrip().rstrip())
with open("Singlepath.txt", "w", encoding="utf-8") as f:
    for item in p:
        f.write("%s" % item)

data = {"Route":one_dir,
       "Direct Stations":p}
df = pd.DataFrame(data)
df["Reverse Stations"] = ""

data = {"Route":two_ways_routes,
       "Direct Stations":direct_stations,
       "Reverse Stations":t
       }
dz = pd.DataFrame(data)

df_row = pd.concat([df, dz])
df_row.sort_values(by=['Route'])
df_row.to_csv('File Name.csv')

ll=[]
s = df_row.iloc[0,1]
ll= s.split(" - ")

dz.iloc[10,:]
