import requests

d={"username":"NIVEDITHA00","password":"Ni_07_vi_14"}

r=requests.post('https://riviera.vit.ac.in/events/evt_2777583ebda6432d8d1dfe57378b36fc',params=d)
r1=requests.get('https://vtop.vit.ac.in/vtop/content')

print(r1.text)
