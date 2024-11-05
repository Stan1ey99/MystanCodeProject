"""
File: webcrawler.py
Name: Stanley
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        }
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        tags = soup.find_all('table', {'class': 't-stripe'})
        # ----- Write your code below this line ----- #
        # d = {}
        # count = 0     # 檢查次數使用
        male_total = 0
        female_total = 0
        for tag in tags:
            # print(tag.text.split())
            lst = tag.text.split()
            # print(lst)
            for i in range(15, 202*5+1, 5):
                male_total += int(lst[i].replace(",", ""))
                # count += 1    # 檢查次數使用
                # print(count)  # 看次數
                # print(male_total)   # 看加總
            for j in range(17, 203*5+1, 5):
                female_total += int(lst[j].replace(",",""))
            print('Male Number:' + str(male_total))
            print('Female Number:' + str(female_total))


if __name__ == '__main__':
    main()
