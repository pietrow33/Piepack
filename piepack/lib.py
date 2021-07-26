from os.path import abspath
from os.path import dirname
import csv
import piepack

def try_me(ddd):
    datapath = dirname(abspath(piepack.__file__)) + "/data"
    data = "{}/ddd.csv".format(datapath)
    with open(data, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            if row['Prefixo'] == str(ddd):
                return row['Estado']
            else:
                continue
        return 'DDD não encontrado'

if __name__ == "__main__":
    ddd = 21
    state = try_me(ddd)
    print(state)