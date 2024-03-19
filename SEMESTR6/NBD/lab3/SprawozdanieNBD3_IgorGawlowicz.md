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
        <Rtext>3</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> MongoDB. Filtrowanie i Sortowanie Danych. Indeksowanie

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

### Przygotowanie Środowiska.

Na ostatnich labach przygotowaliśmy środowisko a także stworzyliśmy testową kolekcje `courses`, gdzie wprowadziliśmy przykładowe dane dla 100 testowych studentów.

### Filtrowanie Danych.

*Przeprowadź 5 zapytań, aby wyświetlić tylko zażądane informacje. Wykorzystaj różne operatory porównania (np. $eq, $ne, $gt, $lt) do filtrowania danych*

1. Znajdź wszystkich studentów, którzy otrzymali ocenę wyższą niż 4 z przedmiotu "Mathematics".

```bash
db.courses.find({"subjects.subject": "Mathematics", "subjects.grade": {$gt: 4}})
[
  {
    _id: ObjectId('65f83c77f23ac558846c9de5'),
    student_id: 0,
    student_name: 'Evelyn',
    student_surname: 'Roberts',
    subjects: [
      { subject: 'Mathematics', grade: 3, final: false },
      { subject: 'English Language', grade: 4, final: true },
      { subject: 'History', grade: 3, final: true },
      { subject: 'Science', grade: 2, final: true },
      { subject: 'Computer Science', grade: 3, final: true },
      { subject: 'Physical Education', grade: 5, final: true }
    ]
  },
  ...
```
2. Znajdź wszystkich studentów, którzy nie otrzymali oceny 5 z przedmiotu "English Language".

```bash
db.courses.find({"subjects.subject": "English Language", "subjects.grade": {$ne: 5}})
[
  {
    _id: ObjectId('65f83c77f23ac558846c9de7'),
    student_id: 2,
    student_name: 'Kristina',
    student_surname: 'Young',
    subjects: [
      { subject: 'Mathematics', grade: 4, final: false },
      { subject: 'English Language', grade: 3, final: true },
      { subject: 'History', grade: 2, final: true },
      { subject: 'Science', grade: 2, final: true },
      { subject: 'Computer Science', grade: 3, final: true },
      { subject: 'Physical Education', grade: 2, final: true }
    ]
  },
  ...
```

3. Znajdź wszystkich studentów, którzy otrzymali co najmniej jedną ocenę niższą niż 3.

```bash
db.courses.find({"subjects.grade": {$lt: 3}})
[
      {
    _id: ObjectId('65f83c77f23ac558846c9dfc'),
    student_id: 23,
    student_name: 'Jeffrey',
    student_surname: 'Glass',
    subjects: [
      { subject: 'Mathematics', grade: 3, final: false },
      { subject: 'English Language', grade: 3, final: true },
      { subject: 'History', grade: 2, final: false },
      { subject: 'Science', grade: 2, final: false },
      { subject: 'Computer Science', grade: 3, final: true },
      { subject: 'Physical Education', grade: 2, final: false }
    ]
  },
  ...
```

4. Znajdź wszystkich studentów, którzy otrzymali ocenę 5 z przedmiotu "Science".

```bash
db.courses.find({"subjects.subject": "Science", "subjects.grade": {$eq: 5}})
[
      {
    _id: ObjectId('65f83c77f23ac558846c9dfd'),
    student_id: 24,
    student_name: 'Amy',
    student_surname: 'Sexton',
    subjects: [
      { subject: 'Mathematics', grade: 4, final: true },
      { subject: 'English Language', grade: 5, final: true },
      { subject: 'History', grade: 4, final: true },
      { subject: 'Science', grade: 5, final: true },
      { subject: 'Computer Science', grade: 5, final: false },
      { subject: 'Physical Education', grade: 5, final: true }
    ]
  }
  ...
```

5. Znajdź wszystkich studentów, którzy nie otrzymali oceny końcowej (final: false) z co najmniej jednego przedmiotu.

```bash
db.courses.find({"subjects.final": false})

[  
{
    _id: ObjectId('65f83c77f23ac558846c9df8'),
    student_id: 19,
    student_name: 'John',
    student_surname: 'Rodgers',
    subjects: [
      { subject: 'Mathematics', grade: 3, final: false },
      { subject: 'English Language', grade: 2, final: false },
      { subject: 'History', grade: 5, final: true },
      { subject: 'Science', grade: 3, final: true },
      { subject: 'Computer Science', grade: 4, final: false },
      { subject: 'Physical Education', grade: 3, final: false }
    ]
  }

```
