import sys
import csv

siftCommands = ['__startswith',
                '__contains',
                '__gt',
                '__lt']
postSiftCommands = ['order_by']
    
def get_valid_keywords_from_csv(csvFile):
    headerLine = csvFile.readline().replace('\n', '').split(', ')
    result = {}
    for i, row in enumerate(headerLine):
        result.update({row: i})
    return result

def generate_full_valid_keyword_dict(validKeywords):
    
    allKeywords = {}

    for keyword in validKeywords:
        allKeywords.update({keyword: [validKeywords[keyword]]})

    for keyword in validKeywords:
        for command in siftCommands:
           allKeywords.update({f'{keyword}{command}' : [command, validKeywords[keyword]]})

        for command in postSiftCommands:
            allKeywords.update({command: [validKeywords[keyword]]})

    return allKeywords

def map_keywords(validKeywords, passedInKeywords):
    result = {}
    for keyword in passedInKeywords:
        if keyword in postSiftCommands:
            result.update({keyword: validKeywords[keyword]})
        elif keyword in validKeywords:
            result.update({passedInKeywords[keyword] : validKeywords[keyword]})
        else:
            raise ValueError(f'keyword: {keyword} is not a valid filter.\n')
    #print(result)
    return result

def split_post_and_pre_csv_sifting_commands(mappedKeywords):
    
    n = 2
    result = [{} for _ in range(n)]

    for element in mappedKeywords:
        if element in postSiftCommands:
            result[0].update({element: mappedKeywords[element]})
        else:
            result[1].update({element:mappedKeywords[element]})
    
    print(result)
    return result

def sift_csv_file(csvFile, siftKeywords):
    result = []
    isValidLine = True
    csvReader = csv.reader(csvFile)

    for line in csvReader:

        for element in siftKeywords:

            if type(siftKeywords[element][0]) is int:
                if line[siftKeywords[element][0]] != element:
                    isValidLine = False
            else:
                if siftKeywords[element][0] == siftCommands[0]:
                    #print(1)
                    if not line[element[1]].startswith(element):
                        isValidLine = False

                elif siftKeywords[element][0] == siftCommands[1]:
                    #print(2)
                    if line[element[1]].find(element) == -1:
                        isValidLine = False

                elif siftKeywords[element][0] == siftCommands[2]:
                    #print(3)
                    if not greater_than(line[siftKeywords[element][1]], element):
                        isValidLine = False
                        
                elif siftKeywords[element][0] == siftCommands[3]:
                    #print(4)
                    if not less_than(line[siftKeywords[element][1]], element):
                        isValidLine = False

            if not isValidLine:
                break

        if isValidLine:
            result.append(line)

        isValidLine = True
    
    return result

def run_post_sift_commands(data, postSiftKeywords):
    for keyword in postSiftKeywords:
        if keyword == postSiftCommands[0]:
            print(keyword)
            data.sort(key = data[keyword])

def greater_than(number, lowerLimit):
    doubleNum = float(number)
    doubleLimit = float(lowerLimit)

    #print(f'{doubleNum} ? {doubleLimit}')
    if doubleNum > doubleLimit:
        return True
    
    return False

def less_than(number, upperLimit):
    doubleNum = float(number)
    doubleLimit = float(upperLimit)
    if doubleNum < doubleLimit:
        return True
    
    return False

def filter(fileName, **keywords):
    try:
        with open(fileName, 'r') as csvFile:
            
            validRowKeywords = get_valid_keywords_from_csv(csvFile)
            
            allValidKeywords = generate_full_valid_keyword_dict(validRowKeywords)
            
            mappedKeywords = map_keywords(allValidKeywords, keywords)
            
            postSiftKeywords, preSiftKeywords = map(dict,split_post_and_pre_csv_sifting_commands(mappedKeywords))
            
            #print(postSiftCommands)
            #print(preSiftKeywords)
            data = sift_csv_file(csvFile, preSiftKeywords)
            run_post_sift_commands(data, postSiftKeywords)
            return data

    except OSError:
        raise OSError(f'Failed to open file: {fileName}\n')

def count(fileName, **keywords):
    data = filter(fileName, keywords)
    return len(data)

def first(fileName, **keywords):
    data = filter(fileName, keywords)
    if len(data) > 0:
        return data[0]
    return data

def last(fileName, **keywords):
    data = filter(fileName, keywords)
    if len(data):
        return data[len(data) - 1]
    return data

def main():
    data = filter(sys.argv[1], salary__gt=1000, salary__lt=3000, order_by ='salary')
    #print(data)

if __name__ == '__main__':
    main()
