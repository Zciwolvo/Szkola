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
            <Rtext>06.05.2023</Rtext>
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
        <Rtext>7</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b>  Obliczenia rozproszone. MapReduce w MONGODB

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

##  Obliczenia rozproszone. MapReduce w MONGODB

Utwórz kolekcję, dla której będą przechowywane dokumenty źródłowe MapReduce

```bash
> db.createCollection("selling")
{ ok: 1 }
```

Wypełnij kolekcję danymi.

```bash
test> db.selling.insert({name: 'Nexus One', date: new Date(2013, 0, 20, 12, 00)})
DeprecationWarning: Collection.insert() is deprecated. Use insertOne, insertMany, or bulkWrite.
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb1e57c610e377160566') }
}
test> db.selling.insert({name: 'Nexus One', date: new Date(2013, 0, 20, 13, 00)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb1e57c610e377160567') }
}
test> db.selling.insert({name: 'iPhone 4', date: new Date(2013, 0, 20, 13, 30)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb1f57c610e377160568') }
}
test> db.selling.insert({name: 'Nexus One', date: new Date(2013, 0, 20, 14, 00)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb1f57c610e377160569') }
}
test> db.selling.insert({name: 'iPhone 4', date: new Date(2013, 0, 21, 15, 30)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb1f57c610e37716056a') }
}
test> db.selling.insert({name: 'iPhone 4', date: new Date(2013, 0, 21, 15, 40)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb1f57c610e37716056b') }
}
test> db.selling.insert({name: 'Nexus One', date: new Date(2013, 0, 21, 16, 20)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb1f57c610e37716056c') }
}
test> db.selling.insert({name: 'iPhone 4', date: new Date(2013, 0, 21, 17, 00)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb2057c610e37716056d') }
}
test> db.selling.insert({name: 'Nexus One', date: new Date(2013, 0, 21, 18, 00)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb2057c610e37716056e') }
}
test> db.selling.insert({name: 'Nexus One', date: new Date(2013, 0, 22, 19, 00)})
{
  acknowledged: true,
  insertedIds: { '0': ObjectId('6638cb2457c610e37716056f') }
}
```

Utwórz funkcję Map w konsoli (konsola umożliwia wprowadzanie konstrukcji wielokreskowych).

```bash
test> var map = function() {
... var key = {
... name: this.name,
... year: this.date.getFullYear(),
... month: this.date.getMonth(),
... day: this.date.getDate()
... };
... emit(key, {count: 1}); }
```

Utwórz funkcję Reduce w konsoli

```bash
test> var reduce = function(key, values) {
... var sum = 0;
... values.forEach(function(value) {
... sum += value['count'];
... });
... return {count: sum};
... };
```

Wykonaj polecenie MapReduce na kolekcji „selling”. Określ parametr „inline: 1”, aby
wyprowadzić wynik do konsoli.

```bash
test> db.selling.mapReduce(map, reduce, {out: {inline: 1}})
DeprecationWarning: Collection.mapReduce() is deprecated. Use an aggregation instead.
See https://docs.mongodb.com/manual/core/map-reduce for details.
{
  results: [
    {
      _id: { name: 'Nexus One', year: 2013, month: 0, day: 20 },
      value: { count: 3 }
    },
    {
      _id: { name: 'iPhone 4', year: 2013, month: 0, day: 21 },
      value: { count: 3 }
    },
    {
      _id: { name: 'Nexus One', year: 2013, month: 0, day: 21 },
      value: { count: 2 }
    },
    {
      _id: { name: 'Nexus One', year: 2013, month: 0, day: 22 },
      value: { count: 1 }
    },
    {
      _id: { name: 'iPhone 4', year: 2013, month: 0, day: 20 },
      value: { count: 1 }
    }
  ],
  ok: 1
}
```

Funckja jest przestarzała według mongo ale wszystko działa tak jak powinnno działać.

Odczytaj wynik działania mapReduce

```bash
test> db.selling.mapReduce(map, reduce, {out: {inline: 1}})
{
  results: [
    {
      _id: { name: 'Nexus One', year: 2013, month: 0, day: 22 },
      value: { count: 1 }
    },
    {
      _id: { name: 'iPhone 4', year: 2013, month: 0, day: 20 },
      value: { count: 1 }
    },
    {
      _id: { name: 'iPhone 4', year: 2013, month: 0, day: 21 },
      value: { count: 3 }
    },
    {
      _id: { name: 'Nexus One', year: 2013, month: 0, day: 20 },
      value: { count: 3 }
    },
    {
      _id: { name: 'Nexus One', year: 2013, month: 0, day: 21 },
      value: { count: 2 }
    }
  ],
  ok: 1
}
```

Wykonaj polecenie MapReduce z kolekcja „selling”. Aby wyprowadzić wynik do kolekcji, parametr
„out” przyjmuje nazwę wynikowej kolekcji.

```bash
test> db.selling.mapReduce(map, reduce, {out: 'sellingResult'})
{ result: 'sellingResult', ok: 1 }
```

Sprawdź, czy funkcja działała bez błędów i czy wynik jest zgodny z oczekiwaniami.

Wszystkie wyniki zgadzają się z oczekiwaniami

Zapytaj o listę dokumentów z kolekcji „sellingResult”:

```bash
test> db.sellingResult.find()
[
  {
    _id: { name: 'iPhone 4', year: 2013, month: 0, day: 20 },
    value: { count: 1 }
  },
  {
    _id: { name: 'iPhone 4', year: 2013, month: 0, day: 21 },
    value: { count: 3 }
  },
  {
    _id: { name: 'Nexus One', year: 2013, month: 0, day: 21 },
    value: { count: 2 }
  },
  {
    _id: { name: 'Nexus One', year: 2013, month: 0, day: 22 },
    value: { count: 1 }
  },
  {
    _id: { name: 'Nexus One', year: 2013, month: 0, day: 20 },
    value: { count: 3 }
  }
]
```

Porównaj listę otrzymanych dokumentów z oczekiwanym wynikiem:

```bash
{ "_id" : { "name" : "Nexus One", "year" : 2013, "month" : 0, "day" : 20 }, "value" : { "count" : 3 } }
{ "_id" : { "name" : "Nexus One", "year" : 2013, "month" : 0, "day" : 21 }, "value" : { "count" : 2 } }
{ "_id" : { "name" : "Nexus One", "year" : 2013, "month" : 0, "day" : 22 }, "value" : { "count" : 1 } }
{ "_id" : { "name" : "iPhone 4", "year" : 2013, "month" : 0, "day" : 20 }, "value" : { "count" : 1 } }
{ "_id" : { "name" : "iPhone 4", "year" : 2013, "month" : 0, "day" : 21 }, "value" : { "count" : 3 } }
```

Kolejność rekordów jest inna wygląda na losową, poza tym wynik bez zmian

Utwórz kolekcję dokumentów, aby przetworzyć je za pomocą MapReduce

Wypełnij kolekcję dokumentami.

Wykonaj przetwarzanie kolekcję przy użyciu modelu przetwarzania rozproszonego
MapReduce.

