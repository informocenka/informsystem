import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def get_data():
    data = pd.read_excel('C:/Users/1/Desktop/test_data.xlsx')
    y = data['Удельная цена']
    X = data.drop('Удельная цена', axis = 1)
    return X, y
    #return data


def get_price(zone, rooms, floor, wall_material, remont, lift, parking):
    object_val = {'Район': zone,
                  'Комнат': rooms,
                  'Этаж': floor,
                  'Материал стен': wall_material,
                  'Ремонт': remont,
                  'Парковка': parking,
                  'Лифт': lift}

    x, y = get_data()
    x = x.append(object_val, ignore_index = True)

    categorical_columns = [c for c in x.columns if x[c].dtype.name == 'object']
    numerical_columns = [c for c in x.columns if x[c].dtype.name != 'object']

    data_nonbinary = pd.get_dummies(x[categorical_columns])
    x = pd.concat((data_nonbinary, x[numerical_columns]), axis = 1)

    obj_eval = x.iloc[len(x) - 1]
    x = x.drop(len(x) - 1, axis=0)

    clf = RandomForestRegressor()
    clf.fit(x, y)
    obj_eval = [obj_eval]
    predict_price = clf.predict(obj_eval)

    return predict_price








