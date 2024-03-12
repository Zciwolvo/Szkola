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
<h1>LABORATORIUM PROJEKTOWANIE I OBSŁUGA SIECI KOMPUTEROWYCH II</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>07.02.2023</Rtext>
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

<b>Temat: </b> Packet Tracer - Określanie DR i BDR

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

## Packet Tracer - Określanie DR i BDR

_W tym ćwiczeniu będziesz testował przydzielanie ról DR i BDR i obserwował ich migrację, kiedy w sieci będą zachodziły zmiany. Następnie zmodyfikujesz priorytety, aby kontrolować przydział ról i wymusisz ponowny wybór ról. Na końcu zweryfikujesz czy routery pełnią wymagane role._

## Część 1: Sprawdzanie procesu zmiany ról routerów DR i BDR

### Krok 1: Poczekaj, aż bursztynowe kontrolki łącza zmieni kolor na zielony.

_Po otwarciu pliku w programie Packet Tracer możesz zauważyć, że lampki wskazujące stan portu na przełączniku są pomarańczowe. Kontrolki te pozostaną pomarańczowe przez 50 sekund podczas których protokół STP przełącznika upewnia się, że żaden z dołączonych do niego routerów nie jest innym przełącznikiem. Alternatywnie możesz kliknąć na opcję Fast Forward Time, aby ominąć ten proces._

### Krok 2: Zweryfikuj obecne stany sąsiadów OSPF.

```bash
RA# show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
192.168.31.33     2   FULL/DR         00:00:35    192.168.1.3     GigabitEthernet0/0
192.168.31.22     1   FULL/BDR        00:00:35    192.168.1.2     GigabitEthernet0/0

RB# show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
192.168.31.11     1   FULL/DROTHER    00:00:36    192.168.1.1     GigabitEthernet0/0
192.168.31.33     2   FULL/DR         00:00:36    192.168.1.3     GigabitEthernet0/0

RC# show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
192.168.31.11     1   FULL/DROTHER    00:00:39    192.168.1.1     GigabitEthernet0/0
192.168.31.22     1   FULL/BDR        00:00:38    192.168.1.2     GigabitEthernet0/0
```

_Który z routerów jest routerem DR?_

`RC`

_Który z routerów jest routerem BDR?_

`RB`

_Jaki jest stan protokołu OSPF routera RA?_

`DROTHER`

### Krok 3: Włącz debugowanie przyległości OSPF.

```bash
RA# debug ip ospf adj
RB# debug ip ospf adj
```

### Krok 4: Wyłącz interfejs GigabitEthernet 0/0 na RC.

```bash
RC(config) #interface g0/0
RC(config-if) #shutdown
```

_Zgodnie z wynikami debugowania, który router został wybrany jako DR, a który router został wybrany jako BDR?_

`RB is now DR and RA is now BDR.`

### Krok 5: Włącz ponownie interfejs GigabitEthernet 0/0 na RC.

a) Zestaw ponownie łącze pomiędzy RC i przełącznikiem.

```bash
RC(config) #interface g0/0
RC(config-if) #no shutdown
```

b) Poczekaj na nową elekcję routerów DR i BDR.

_Czy DR i BDR zamieniają się rolami. Wyjaśnij._

`Nie, ponieważ OSPF nie aktualizuje DR/BDR tak długo jak są jeszcze aktywne`

c) Sprawdź przypisania DR i BDR za pomocą polecenia show ip ospf neighbor na routerze RC.

```bash
RC# show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
192.168.31.22     1   FULL/DR         00:00:34    192.168.1.2     GigabitEthernet0/0
192.168.31.11     1   FULL/BDR        00:00:34    192.168.1.1     GigabitEthernet0/0
```

### Krok 6: Wyłącz interfejs GigabitEthernet0/0 na RB.

_Zgodnie z wynikami debugowania na RA, który router został wybrany jako DR, a który router został wybrany jako BDR?_

`RC jest teraz BDR i RA jest teraz DR. RA było DBR, kiedy DR nie powiodło się zostało DR`

### Krok 7: Włącz ponownie interfejs GigabitEthernet0/0 na RB.

_Poczekaj na nową elekcję routerów DR i BDR. Czy DR i BDR zamieniają się rolami. Wyjaśnij._

`Nie, rolę nie zmieniły się ponieważ DR i BDR są wciąż aktywne. router z wyższym priorytetem nie przyjmie roli BDR dopóki taka wciąż istnieje`

_Jaki jest status routera RC teraz?_

`BDR`

### Krok 8: Wyłącz debugowanie.

`undebug all` na RA i RB

## Część 2: Modyfikacja priorytetu OSPF i wymuszanie wyboru

### Krok 1: Skonfiguruj priorytety OSPF na każdym routerze.

```bash
RA(config)# interface g0/0
RA(config-if)# ip ospf priority 200
```

```bash
RB(config)# interface g0/0
RB(config-if)# ip ospf priority 100

RC(config)# interface g0/0
RC(config-if)# ip ospf priority 1
```

### Krok 2: Wymuś wybory, resetując proces OSPF na routerach.

Używamy polecenia `clear ip ospf process` na każdym routerze zaczynając od `RA`.

### Krok 3: Sprawdź, czy wybór DR i BDR odbył się pomyślnie.

_Zgodnie z danymi wyjściowymi polecenia show ip ospf neighbor na routerach, który router jest teraz routerem DR, a który routerem BDR?_

`RA jest teraz DR, a RB jest teraz BDR`
