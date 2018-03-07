import json
import codecs
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
#define example
with open('output.json') as data_file:
    data = json.load(data_file)
values = array(data)
print(values)
# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print(integer_encoded)

# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
print(type(onehot_encoded))
oneHotList =onehot_encoded.tolist()
with open('oneHotEncoding.json', 'w') as outfile:
    json.dump(oneHotList, outfile)


'''
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
'''

'''
oneHotReshaped = onehot_encoded.arrange(6713).reshape()
arrayToList = onehot_encoded.tolist()
json_file = "oneHotEncoded.json"
json.dump(onehot_encoded, codecs.open(json_file, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4) ### this saves the array in .json format
'''
'''
print(onehot_encoded)
with open('oneHotEncoded.json', 'w') as outfile:
    json.dump(listOneHot, outfile)
'''
