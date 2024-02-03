import csv
import random
import string


def create_login(s: string):
    names = s.split()
    return f"{names[0]}_{names[1][0]}{names[2][0]}."


def create_password():
    c = string.ascii_letters + string.digits
    password = ''.join(random.choice(c) for _ in range(8))
    return password


s_w_p = []
with open('students.csv', encoding='utf8') as file:
    answer = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for x in answer:
        x['login'] = create_login(x["Name"])
        x['password'] = create_password()
        s_w_p.append(x)
with open('students_password.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['id','Name','titleProject_id','class','score','login','password'])
    w.writeheader()
    w.writerows(s_w_p)


