import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,area,bedroom,floor_num,furnishing,apartment):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = bedroom
    x[2] = floor_num
    x[3] = furnishing
    x[4] = apartment
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # first 5 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/Flats_for_Rent_in_Mumbai_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
   # print(get_location_names())
    print(get_estimated_price('mulund west',2000, 4, 15,1,1))