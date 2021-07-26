import csv

def try_me(ddd):
    with open('/home/pietro/code/pietrow33/piepack/piepack/data/ddd.csv', mode='r') as csv_file:
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