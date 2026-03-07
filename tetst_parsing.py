import requests
from bs4 import BeautifulSoup

url = "https://schedule.nspu.ru/group_shedule_weeks.php?fancy=+%28%D0%BB.%3A+24-28+%D0%BD%D0%B5%D0%B4.+)&pred=%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B+%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9+%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8+%D0%B8+%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D0%BA%D0%B8&prep=%D0%A1%D0%B0%D1%84%D0%BE%D0%BD%D0%BE%D0%B2+%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9+%D0%93%D0%B5%D0%BD%D0%BD%D0%B0%D0%B4%D1%8C%D0%B5%D0%B2%D0%B8%D1%87&weeks=24-28%7C%7C%7C%7C%7C"

headers = {
    "User-Agent": "Mozilla/5.0"  # представляемся браузером
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
file = open("example.txt", "w")
file.write(str(soup))
file.close()
print("soup")
