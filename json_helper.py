import json
import os
import glob
import pickle


def json_helper(string_path):
    with open(string_path, 'r') as file:
        data = json.load(file)
        return data

def read_all_json_files(string_path):
    obj_list = []
    for filename in os.listdir(string_path):
        if filename.endswith('.json'):
            filepath = os.path.join(string_path, filename)
            with open(filepath, 'r') as file:
                obj_list.append(json.load(file))

    return obj_list

def write_pickle(string_path, data):
    with open(string_path, 'wb') as file:
        pickle.dump(data, file)

def load_pickle(string_path):
    with open(string_path, 'rb') as file:
        data = pickle.load(file)
    return data





print(read_all_json_files('/Users/jacobp/Desktop/projects/WEEK4/PythonFundamentals.Exercises.Part9/data/super_smash_bros'))
