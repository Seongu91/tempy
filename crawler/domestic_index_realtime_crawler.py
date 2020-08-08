from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import pymongo as pm
import datetime
import requests

def get_code() :
    return ['KOSPI', 'KOSDAQ', 'KOSPI_200', 'KR4101Q90009']


def get_ip() :
    return '13.124.27.94'

def get_port() :
    return 43775


def get_url(code, page) :
    if code == 'KR4101Q90009' :
        return "http://finance.daum.net/api/future/{}/times?page={}&perPage=100&pagination=true".format(code, page)
    else :
        return "http://finance.daum.net/api/market_index/times?page={}&perPage=100&market={}&pagination=true".format(page, code)

def get_data(code) :
    cur_page = 1
    lst_data = []


    while True :
        url = get_url(code,cur_page)
        headers = {
                    'Referer': 'http://finance.daum.net',
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.127'
        }
        response = requests.get(url, headers=headers)
        jsonObj = response.json()

        total_pages = jsonObj["totalPages"]
        datas = jsonObj["data"]


        for data in datas :
            dic_data = {}
            dic_data["time"] = datetime.datetime.strptime(data["date"],  "%Y-%m-%d %H:%M:%S")
            dic_data["closing"] = data["tradePrice"]
            lst_data.append(dic_data)
            
        
        if lst_data[0]["time"].date != lst_data[-1]["time"].date :
            t = lst_data[0]["time"].date()
            lst_data = [x for x in lst_data if x['time'] > datetime.datetime(t.year, t.month, t.day)]
            break

        if cur_page == total_pages :
            break
            
        print(total_pages)
        print(cur_page)
        print(data["date"])

        cur_page += 1

    return  lst_data

def save_to_DB_Indexes(code, lst_data) :
    #client =  pm.MongoClient(get_ip(), get_port())
    client = pm.MongoClient('mongodb://{}:{}@{}:{}'.format("donn", "terarosa", get_ip(), get_port()))

    db = client["donn"]
    col = db["domestic_indexes"]
        
    t = lst_data[0]['time'].date()
    
    dict_rst = {"code" : code, "date": datetime.datetime(t.year, t.month, t.day)    }
    
    col.update_many(dict_rst, {"$addToSet" : {"prices" : {"$each" : lst_data}}}, True )
    

def crawl_data() :
    for code in get_code() : 
        lst_data = get_data(code)
        save_to_DB_Indexes(code, lst_data)

if __name__ == "__main__":
    crawl_data()
