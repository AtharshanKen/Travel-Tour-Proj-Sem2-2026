from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
# from Cal import Cal
from dateutil import parser
import pandas as pd
import os

folder1 = "./Dataset/Crowd/data_weather/Final"
dfs_comb = pd.DataFrame()
for df in [pd.read_csv(os.path.join(folder1,f)) for f in os.listdir(folder1) if f.endswith('.csv')]:
    dfs_comb = pd.concat([dfs_comb,df],axis='rows')
dfs_comb['Date'] = dfs_comb['Date'].apply(lambda x: parser.parse(x).date())#datetime.date(YYYY, MM, DD)

folder2 = "./Dataset/Crowd/Flight/flight_paths.csv"
flights = pd.read_csv(folder2)
flights['apt_time_dt_ds'] = flights['apt_time_dt_ds'].apply(lambda x: parser.parse(x).date())#datetime.date(YYYY, MM, DD)
flights['apt_time_dt_dp'] = flights['apt_time_dt_dp'].apply(lambda x: parser.parse(x).date())

app = FastAPI()

@app.post("/Health")
async def backend_up():
    return 

# def obtain_models():
#     return 

@app.post("/dfs_flgh_data")
async def dfs_flgh_data():
    return [dfs_comb.to_dict(orient="records"),flights.to_dict(orient="records")]
# @app.post("/FilterOps")
# async def get_fl_ops():
#     return [flights['City_dp'].unique().tolist(),
#             dfs_comb['Attraction_Category'].unique().tolist(),
#             dfs_comb['Type_of_Attraction'].unique().tolist(),
#             pois['Location_Name'].unique().tolist()]

# class FrCtReq(BaseModel):
#     model:str
#     origin:str
#     arrival_date:str
#     dest:str
# @app.post("/Forecasting")
# async def forecasting(input:FrCtReq):
#     return 

# @app.post("/Recommendation")
# async def recommendation():
#     return 


# class Input(BaseModel):
#     op:str
#     x:int
#     y:int
# @app.post("/Cal")
# async def operate(input:Input):
#     print(input)
#     print(type(input))
#     result = Cal(input.op, input.x, input.y)
#     return result