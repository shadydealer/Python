import sys
import os
import json

def extract_best_by_skill(file_name):
    try:
        file = open(file_name,'r')
        data = {}
        result = {}

        if  os.path.getsize(file_name):
            
            data = json.load(file)
            
            if 'people' not in data:
                file.close()
                raise ValueError("Expected 'people' object in json file: {}.", format(file_name))

            for person in data['people']:

                if 'skills' not in person:
                    file.close()
                    raise ValueError("Expected every 'people' member to have a 'skill' member in json file: {}".format(file_name))

                for skill in person['skills']:
                    if (skill['name'] not in result) or (skill['level'] > result[skill['name']][0]):
                        result.update({skill['name']: (skill['level'], person['first_name'], person['last_name'])})
        
        
        file.close()
        return result

    except OSError:
        raise OSError("Invalid file path: {}".format(file_name)) 

def print_result(best_by_skill):
    for skill in best_by_skill:
        print(f'{skill} - {best_by_skill[skill][1]} {best_by_skill[skill][2]}')

def main():
    print_result(extract_best_by_skill(sys.argv[1]))

if __name__ == "__main__":
    main()