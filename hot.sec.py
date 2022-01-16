import requests
from bs4 import BeautifulSoup

sl = []
sf = []
m = 1

resp = requests.get("https://www.kugou.com/yy/rank/home/1-4681.html?from=rank")
resp.encoding = "utf-8"
res = resp.text
soup = BeautifulSoup(res, "html.parser")

d1 = soup.find(name="div", class_="pc_temp_wrap pc_temp_2col_critical")
d2 = d1.find(name="div", class_="pc_temp_main")
d3 = d2.find(name="div", class_="pc_temp_content")
d4 = d3.find(name="div", class_="pc_temp_container")
d5 = d4.find(name="div", id="rankWrap")
d6 = d5.find(name="div", class_="pc_temp_songlist")

ul = d6.find(name="ul")

li = ul.find_all(name="li")

for i in li:
    preli = i["title"].split()
    n = 0
    
    while True:
        st = preli[n]
        
        if st != "-":
            preli.pop(n)

        else:
            preli.pop(n)
            break

    sn = " ".join(preli)
    sl.append(sn)
    sf.append(str(m) + "." + sn)
    m += 1

if __name__ == "__main__":
    print("Very Good Songs From BillBoard -- By lanlan2_")
    
    sf.pop()
    sf.pop()
    for j in sf:
        print("\n" + j)

    print("\n...")
    input("\nPress RETURN to exit the program.")
