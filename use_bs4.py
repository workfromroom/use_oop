import requests
from bs4 import BeautifulSoup

url="https://detik.com"
try:
    response = requests.get('https://detik.com')
    if response.status_code == 200 :
        print(f"Success! Response={response.status_code}")
        soup = BeautifulSoup(response.text, features="html.parser")
        print("Hasil Pemanggilan dari ",url)
        print("Title: ",{soup.title.string})
    else:
        print("Woooppps, Ada kesalahan")
except Exception as e:
    print("There is an Error")

