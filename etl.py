# extract -> Transform -> Load

import requests      # requsets from enternet
import pandas as pd  # pandas dealing with data (row /column)
from datetime import datetime # import library tool datetime only to record date and time
from sqlalchemy import create_engine

from sqlalchemy import create_engine




def extract():   # funcation to extract data from API and called anytime to run the inside code
      #url => link to  pull data from API  and from=USD --> take price for dolars
    url = "https://api.frankfurter.app/latest?from=USD"
    
    try:  # try the code if error obtain don't stop all program go to except 

          response = requests.get(url) # wait for reply from server and store data and another things inside varible response 
          response.raise_for_status  # confirm the request was successful if the API return error (400 or 500) this line stop the run and go to except
          data = response.json() # transform json (API string) data to dictionary
          print("pull data is done")
          return data 
    except requests.exceptions.RequestException as e: # if erroe in try statment , except can run . e --> store details of error in variable e
        print(f"error during pull data:{e}")
        return None

def transform(data):  # (dataframe) take raw data from extract funcation as an entrance to it
     

    if data is None:
        print ("no data to tarnsform")
        return None 
    
    rates = data["rates"] # pull row of rates from API and put in in new column called rates
    #rates.items==? transform  dictionary to pair ( currencey and rate)
    df=pd.DataFrame(list(rates.items()),columns=["currency" ,"rate"]) # tranform dictionery to dataframe

    df["base_currency"] = data["base"] # add columns of base_currency
    df["rate_date"] = data["date"]  # add columns rate_date from API
    df["extracted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # add column show when data was pulled

    print("data is done")
    return df

def load(df):  # take dataframe (df) as input and store dataframe in database (sqlite)

    if df is None:  # if transform (df) was error (no data) , stop the load using return 

        print("no data to store")
        return
    # python => create_engine => sql
    engine = create_engine("sqlite:///exchange_rates.db") # create_exchange is func from library sqlalchemy responsible for communication with database
    #sqlite is the name of database ,,, ///exchange_rates.db is the name of sql and the title of database and store all data ( the file if not available it can created)
    df.to_sql("exchange_rates", con=engine, if_exists="append",index="False")
    #df.to_sql : trasform pandas to sql
    #exchange_rates : the name of table
    #con=engine : use the communication
    #if_exists="append" : if the table is available then add the new rows under  old rows don't delete any rows
    #if_exists="replace" : delete old rows then put the new rows
    #index="False" :  don't add 0,1... 
    print("data stored in sql")

if __name__ == "__main__":
    raw_data = extract()
    df = transform(raw_data)
    load(df)