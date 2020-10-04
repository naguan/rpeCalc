import csv

def process(filename):
    with open(filename, 'r', encoding='utf-8-sig') as datafile:
        datareader = csv.reader(datafile, delimiter=',')
        data = {}
        for row in datareader:
            data[row[0]] = row[1:]
        #print(float(data[0][5]) * 134)
        return(data)

def rpeSelection(data, rpe, weight, rep):
    percentages = data.get(rpe)
    return(float(percentages[rep-1]) * weight)



if __name__=="__main__": 
    print(rpeSelection(process('/Users/nathanguan/projects/rpe.csv'), '10', 405, 1))