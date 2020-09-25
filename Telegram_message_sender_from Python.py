import requests

adres="https://pomber.github.io/covid19/timeseries.json"

cevap=requests.get(adres)

bilgi=cevap.json()["Turkey"]

gunSayisi=len(bilgi)

tarih=bilgi[gunSayisi-1]["date"]
vakaSayisi=bilgi[gunSayisi-1]["confirmed"]
olumSayisi=bilgi[gunSayisi-1]["deaths"]
iyilesmeSayisi=bilgi[gunSayisi-1]["recovered"]

#mesaj="{} tarihinde \nToplam Vaka sayısı:{}\nToplam Ölüm Sayısı:{}\nToplam İyileşme Sayısı:{}\nSağlıklı Günler Dileriz...".format(tarih,vakaSayisi,olumSayisi,iyilesmeSayisi)
mesaj = "Şerefsizlik yapmayalım"
print(mesaj)

#requests.post(url = 'https://api.telegram.org/bot1354993750:AAG39h-7rITmd5sefMwNYnAZwNTrDfVltAU/sendMessage',data={'chat_id':1296834804,'text':mesaj}).json() #utku

requests.post(url = 'https://api.telegram.org/bot1354993750:AAG39h-7rITmd5sefMwNYnAZwNTrDfVltAU/sendMessage',data={'chat_id':1173837667,'text':mesaj}).json()

#requests.post(url = 'https://api.telegram.org/bot1354993750:AAG39h-7rITmd5sefMwNYnAZwNTrDfVltAU/sendMessage',data={'chat_id':1248496141,'text':mesaj}).json()

