import random
from faker import Faker




subjects = ["Mathematics", "English Language", "History", "Science", "Computer Science", "Physical Education"]
states = ["true", "false"]

out = open("./lab2/out.txt", "a")
fake = Faker()

out.write("use my_app;\n")

out.write("db.courses.insertMany([\n")
for i in range(100):
    out.write("{\n")
    out.write(f'"student_id": {i},\n')
    out.write(f'"student_name": "{fake.first_name()}",\n')
    out.write(f'"student_surname": "{fake.last_name()}",\n')
    out.write(f'"subjects": [\n')
    for sub in subjects:
        out.write('{\n')
        out.write(f'"subject": "{sub}",\n')
        out.write(f'"grade": {random.randint(2, 5)},\n')  # Integers instead of strings
        out.write(f'"final": {str(random.choice(states)).lower()}\n')  # Boolean values instead of strings
        out.write('},\n')
    out.write('],\n')
    out.write("},\n")
out.write("])\n")



