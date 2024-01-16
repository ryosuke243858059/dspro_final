from bs4 import BeautifulSoup
import requests

url = 'https://www.twr.co.jp/route/tabid/119/Default.aspx'
r = r = requests.get(url)

url = 'https://www.twr.co.jp/route/tabid/119/Default.aspx'
r = requeｓts.get(url)

html_soup = BeautifulSoup(r.text,'html.parser')
print(type(html_soup))

a1_list = ['#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(1) > th:nth-child(1)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(1) > td > a','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(2) > th:nth-child(1)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(2) > td > a:nth-child(1)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(2) > td > a:nth-child(2)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(2) > td > a:nth-child(3)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(2) > td > a:nth-child(4)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(2) > td > a:nth-child(5)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > th:nth-child(1)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(1)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(2)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(3)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(4)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(5)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(6)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(7)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(8)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(3) > td > a:nth-child(9)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(4) > th:nth-child(1)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(4) > td > a:nth-child(1)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(4) > td > a:nth-child(2)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(4) > td > a:nth-child(3)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(4) > td > a:nth-child(4)','#dnn_ctr1053_ViewTabs_ctr1070_ModuleContent > div > table > tbody > tr:nth-child(4) > td > a:nth-child(5)']
for a1 in a1_list:
    soup_h_list = html_soup.select_one(a1)
    for soup_a in soup_h_list:
        print(soup_a.text)
