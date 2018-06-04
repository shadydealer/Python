import sys
import json

EACH_MEMBER_MUST_HAVE = "Each member of 'people' must have"

def build_head(file, full_name):
    file.write('''<head>\n'''
               f'''<title>{full_name}</title>\n'''
               '''<link rel="stylesheet" type="text/css" href="styles.css">\n'''
               '''</head>\n''')

def build_skills_class(file, skills):
    file.write('''<div class="skills">\n'''
               '''<h2>Skills:</h2>\n'''
               '''<ul>\n''')
    for skill in skills:
        file.write(f'<li>{skill["name"]} - {skill["level"]}</li>\n')
    file.write('''</ul>\n'''
               '''</div>\n''')


def build_interests_class(file, interests):
    file.write('''<div class="interests">\n'''
               '''<h2>Interests:</h2>\n'''
               '''<ul>\n''')
    for interest in interests:
        file.write(f'<li>{interest}</li>\n')
    file.write('''</ul>\n'''
               '''</div>\n''')

def build_business_card_class(file, person):
    
    gender = person['gender']
    full_name = f'{person["first_name"]} {person["last_name"]}'
    avatar = f'{person["avatar"]}'
    age = person['age']
    birth_date = person['birth_date']
    birth_place = person['birth_place']
    interests = person['interests']
    skills = person['skills']

    file.write(f'''<div class="business card {gender}">\n'''
               f'''<h1 class="full-name">{full_name}</h1>\n'''
               f'''<img class="avatar" src="{avatar}">\n'''
               f'''<div class="base-info">\n'''
               f'''<p>Age: {age}</p>\n'''
               f'''<p>Birth date: {birth_date}</p>\n'''
               f'''<p>Birth place: {birth_place}</p>\n'''
               f'''<p>Gender: {gender}</p>\n'''
               f'''</div>\n''')
    
    build_interests_class(file, interests)
    build_skills_class(file,skills)
    file.write('''</div>\n''')

def build_body(file, person):
    
    if 'gender' not in person:
        raise ValueError(f'{EACH_MEMBER_MUST_HAVE} a "gender" member.')
    if 'avatar' not in person:
        raise ValueError(f'{EACH_MEMBER_MUST_HAVE} an "avatar" member.')
    if 'age' not in person:
        raise ValueError(f'{EACH_MEMBER_MUST_HAVE} an "age" member.')
    if 'birth_date' not in person:
        raise ValueError(f'{EACH_MEMBER_MUST_HAVE} a "birth_date" member.')
    if 'birth_place' not in person:
        raise ValueError(f'{EACH_MEMBER_MUST_HAVE} a "birth_place" member.')
    if 'interests' not in person:
        raise ValueError(f'{EACH_MEMBER_MUST_HAVE} an "interests" member.')
    if 'skills' not in person:
        raise ValueError(f'{EACH_MEMBER_MUST_HAVE} an "skills" member.')

    file.write('''<body>\n''')
    build_business_card_class(file, person)
    file.write('''</body>\n''')

def json_to_dict(json_file_name):
    result = {}
    try:
        with open(json_file_name) as file:
            result = json.load(file)
        
        return result
    except OSError:
        raise OSError(f'Invalid file path : {json_file_name}')
    except ValueError:
        raise ValueError(f'Invalid format of json file: {json_file_name}')


def build_html(json_data):
    
    full_name = ""

    for person in json_data['people']:
        full_name = f'{person["first_name"]}_{person["last_name"]}'
        with open(f'{full_name}.html', 'w+') as file:
            file.write('''<!DOCTYPE html>\n'''
                       '''<html>\n''')
            build_head(file, full_name)
            build_body(file,person)
            file.write('</html>')


def main():
    data = json_to_dict(sys.argv[1])
    build_html(data)
    pass


if __name__ == '__main__':
    main()
