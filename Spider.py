from bs4 import BeautifulSoup
import requests


s = requests.session()
host = 'http://car.austohome.com.cn'
# url = host + '/AsLeftMenu/As_LeftListNew.ashx'
url = "http://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=2%20&brandId=0%20&fctId=0%20&seriesId=0"



# params = {
#     'typeId': "2",
#     'brandId': "0",
#     'fctId': "0",
#     'seriesId': "0"
# }


response = s.get(url)
bs = BeautifulSoup(response.text, 'lxml')

# print(response.text)


for i in bs.find_all('i', class_="icon10 icon-sjr"):
    father = i.parent
    print("hi")
    link = father.find('a')['href']
    next_url = host+link

    print('fetching'+next_url+'\n')

    # response_brand = s.get(next_url)
    # bs = BeautifulSoup(response_brand, 'lxml')
    #
    # regex_series = re.compile(r'/photo/series/21066/1/2776860.html#pvareaid=2042264')













