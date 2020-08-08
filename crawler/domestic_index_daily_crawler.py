from pykrx import stock
import datetime
import pymongo as pm

def get_ip() :
    # db ip 
    # need to make it as config later
    return '13.124.27.94'

def get_port() :
    # db port
    # need to make it as config later
    return 43775

# tickers
dic_ticker = {'코스피' : "KOSPI", '코스피 200' : "KOSPI_200", "코스닥" : 'KOSDAQ'}

# save daily index
def save_daily_index(interval  = 1) :
    # get data -interval day from today
    dt_now = datetime.datetime.now()
    dt_start = dt_now + datetime.timedelta(days=-1 *interval)

    # make db client
    client = pm.MongoClient('mongodb://{}:{}@{}:{}'.format("donn", "terarosa", get_ip(), get_port()))
    db = client["donn"]
    col = db["domestic_indexes"]

    # for each tickers
    for i in range(len(dic_ticker)) : 
        df = stock.get_index_ohlcv_by_date(datetime.datetime.strftime(dt_start, "%Y%m%d"), datetime.datetime.strftime(dt_now, "%Y%m%d"), lst_ticker[i])
        df = df.reset_index()
        for key, row in df.iterrows() :
            dict_key = {}
            dict_key["code"] = dic_ticker[list(dic_ticker.keys())[i]]
            t = row['날짜'].date()
            dict_key["date"] = datetime.datetime(t.year,t.month,t.day)

            dict_value = {}
            dict_value['opening'] = row['시가']
            dict_value['high'] = row['고가']
            dict_value['low'] = row['저가']
            dict_value['closing'] = row['종가']

            col.update_one(dict_key, {"$set" : dict_value}, True)


if  __name__ == "__main__":
    save_daily_index(3)
