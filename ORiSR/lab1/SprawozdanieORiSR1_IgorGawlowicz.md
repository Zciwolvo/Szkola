<style>
h1, h4, h2 {
    border-bottom: 0;
    display:flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
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
<h1>Akademia Techniczno-Humanistyczna w Bielsku-Białej </h1>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

<h1 style="text-align: center;"><b>LABORATORIUM</b></h1>
<h1 style="text-align:center"><b>Obliczeń Równoległych i Systemów Rozproszonych </b></h1>

&nbsp;

&nbsp;

<h2 style="text-align:center; border: none;"><b>Sprawozdanie nr 1</b></h3>
<h2 style="text-align:center; border: none;">Zarządzanie procesami</h2>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

GRUPA: 2B / SEMESTR: 5 / ROK: 3

Igor Gawłowicz / 59096

<div style="page-break-after: always;"></div>

### **Proces**

to ciąg (sekwencja) logicznie uporządkowanych czynności, w wyniku których powstaje określony efekt (rezultat) działania (produkt, usługa), z którego korzysta klient (zewnętrzny lub wewnętrzny).

Każdy proces może utworzyć jedene lub więcej procesów potomnych **(child)** wobec którego staje się procesem macierzystym **(parent)**. W chwili tworzenia procesu system operacyjny alokuje, celem jego reprezentacji, strukturę danych w postaci **PCB** (Process Control Block)

Każdy system operacyjny oferuje usługi umożliwiające pobranie informacji o aktywności i stanie bieżących procesów. W systemach rodziny **_POSIX_** służą temu m.in. zestaw poleceń konsoli:

```bash
ps top watch time
```

```bash
ps [option] -o [format]
```

np.

```bash
ps group users tty 3 -o pid,cmd
```

Wyświetli dla grupy _users_ z terminala _3_ informację o jej procesach podająć _PID_ oraz komendę jaka uaktywniła proces.

### Listing procesów

Procesy możemy wyświetlić w postaci struktury drzewa, poczynając od procesu _init_ albo _pid_

```
pstree [options] [pid|user]
```
