<style>
h1, h4 {
    border-bottom: 0;
    display:flex;
    flex-direction: column;
    align-items: center;
      }
      
centerer{
    display: grid;
    grid-template-columns: 6fr 1fr 4fr;
    grid-template-rows: 1fr;

}
rectangle{
    border: 1px solid black;
    margin: 0px 50px 0px 50px;
    width: 200px;
    height: 4em;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
}
Ltext{
    margin: auto auto auto 0;
    font-weight: bold;
    margin-left: 4em
}
Rtext{
    margin: auto;
}

row {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center; 
}
 </style>
<h1>LABORATORIUM NIERELACYJNE BAZY DANYCH</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>26.02.2023</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Rok studiów:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>3</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Semestr:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>6</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Grupa studencka:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>2</Rtext>
        </rectangle>
    </div>
</centerer>

<centerer>
    <Ltext>Grupa laboratoryjna:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>2B</Rtext>
        </rectangle>
    </div>
</centerer>

&nbsp;

&nbsp;

<row>
    <b>Ćwiczenie nr.</b>
    <rectangle>
        <Rtext>2</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Modelowanie danych w MongoDB: Tworzenie Struktury Kolekcji (Zadanie nr.2)

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz
2. Andrzej Macura
3. Patryk Ihas

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Opis zadania

**System Oceny Studentów:**

**Kolekcja "courses" z zagnieżdżonymi ocenami dla każdego studenta.**

Aby stworzyć kolekcje odpowiedzialną za system oceny studentów musieliśmy rozważyć strukturę naszej tabeli, więc zaczęliśmy od napisania przykładowej struktury rekordu

```json
[
    {
        "student_id": 1,
        "student_name": "Anna",
        "student_surname": "Nowak",
        "subjects": [
            {
                "subject": "math",
                "grade": 4,
                "final": true
            },
            {
                "subject": "history",
                "grade": 5,
                "final": true
            }
        ]
    }
]
```

Postanowiliśmy że potrzebujemy osobnego rekordu dla każdego studenta, gdzie każdy student będzie miał swoją tabelę ocen dla każdego przedmiotu, w ten sposób doszliśmy do zdefiniowania kolekcji w następujący sposób

```bash
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
```

## Operacje CRUD

## Przykładowe dane

Do celów testowych przygotowaliśmy skrpyt generujący duże zestawy losowych danych który możemy następnie uruchomić przez mongo shell, tworząc automatycznie naszą tabelę i zapełniając ją podaną ilością rekordów, z w pełni losowymi sztucznymi danymi.

```bash
db.courses.insertMany([
{
"student_id": 0,
"student_name": "Shannon",
"student_surname": "Dennis",
"subjects": [
{
"subject": "Mathematics",
"grade": "4",
"final": "false"
},
{
"subject": "English Language",
"grade": "5",
"final": "true"
},
{
"subject": "History",
"grade": "2",
"final": "false"
},
{
"subject": "Science",
"grade": "2",
"final": "true"
},
{
"subject": "Computer Science",
"grade": "3",
"final": "false"
},
{
"subject": "Physical Education",
"grade": "3",
"final": "true"
},
],
},
...itd
```