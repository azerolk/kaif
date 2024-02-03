import csv

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter = ',')
    answer = list(reader)[1:]
    c = {}
    s = {}
    for id, name, titleProject_id, level, score in answer:
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {id}")
        c[level] = c.get(level, 0) + 1
        s[level] = s.get(level, 0) + (int(score) if score != 'None' else 0)
    for x in answer:
        if x[-1] == 'None':
            x[-1] = round(s[x[-2]] / c[x[-2]], 3)
with open('students_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.writer(file)
    w.writerow(['id','Name', 'titleProject_id', 'class', 'score'])
    w.writerows(answer)



git init
