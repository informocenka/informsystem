import pandas as pd


def get_data():
    data = pd.read_excel('C:/Users/1/Desktop/test_data.xlsx')
    #y = data['Удельная цена']
    #X = data.drop('Удельная цена', axis = 1)
    #return X, y
    return data

def get_av_price(prices):
    get_data()
    return sum(prices)/len(prices)

def get_price(zone, rooms, floor, wall_material, remont, lift, parking):
    object_val = {'Район': zone,
                  'Комнат': rooms,
                  'Этаж': floor,
                  'Материал стен': wall_material,
                  'Ремонт': remont,
                  'Парковка': parking,
                  'Лифт': lift}

    X, y = get_data()
    X = X.append(object_val, ignore_index = True)

    categorical_columns = [c for c in X.columns if X[c].dtype.name == 'object']
    numerical_columns = [c for c in X.columns if X[c].dtype.name != 'object']

    data_nonbinary = pd.get_dummies(X[categorical_columns])
    X = pd.concat((data_nonbinary, X[numerical_columns]), axis = 1)

    return 0








