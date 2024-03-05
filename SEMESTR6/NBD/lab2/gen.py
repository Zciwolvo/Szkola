import random
from faker import Faker




subjects = ["Mathematics", "English Language", "History", "Science", "Computer Science", "Physical Education"]
states = ["true", "false"]

out = open("./SEMESTR6/NBD/lab2/out.txt", "a")
fake = Faker()

out.write("use my_app;\n")
out.write("""
db.createCollection("courses", {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: ["student_id", "student_name", "student_surname", "subjects"],
         properties: {
            student_id: {
               bsonType: "int",
               description: "ID of the student"
            },
            student_name: {
               bsonType: "string",
               description: "Name of the student"
            },
            student_surname: {
               bsonType: "string",
               description: "Surname of the student"
            },
            subjects: {
               bsonType: "array",
               description: "List of subjects",
               items: {
                  bsonType: "object",
                  required: ["subject", "grade", "final"],
                  properties: {
                     subject: {
                        bsonType: "string",
                        description: "Name of the subject"
                     },
                     grade: {
                        bsonType: ["int", "double"],
                        description: "Grade of the student for the subject"
                     },
                     final: {
                        bsonType: "bool",
                        description: "Whether the grade is final or not"
                     }
                  }
               }
            }
         }
      }
   }
});

""")

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
        out.write(f'"grade": "{random.randint(2,5)}",\n')
        out.write(f'"final": "{random.choice(states)}"\n')
        out.write('},\n')
    out.write('],\n')
    out.write("},\n")
out.write("])\n")



