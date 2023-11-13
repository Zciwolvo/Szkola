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
<h1>Uniwersytet Bielsko-Bialski </h1>

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

<h2 style="text-align:center; border: none;"><b>Sprawozdanie nr 4</b></h3>
<h2 style="text-align:center; border: none;">Kolejki komunikatów IPC</h2>

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

## Cel ćwiczenia

TODO

Współbieżność procesów (czy wątków) wiąże się często z potrzebą okresowej (asynchronicznej)
wymiany komunikatów. Żaden z omawianych wcześniej mechanizmów nie spełniłby się
najlepiej w tej roli. Po raz pierwszy problem ten znalazł rozwiązanie w

**UNIX System V**

w postaci

**kolejki komunikatów, ang. message queues**

wprowadzonym jeszcze przez AT&T w roku 1983, a stosowanych do chwili obecnej w rodzinie
systemów nawiązujących po spuścizny UNIX.

Kolejki komunikatów stanowią jeden z kilku elementów funkcjonalnych tworzących

**InterProcess Communication, IPC**

implementowany standardowo w obrębie jądra systemów będących potomkami UNIX System V.

Również **MsWindows**, którego twórcy mają od pewnego czasu aspiracje stworzenie systemu
wspierającego współbieżność dysponuje także swoistym **IPC**.

Kolejka komunikatów stanowi połączona listę wiadomości przechowywanych w obszarze pamięci jądra systemowego i jest identyfikowana przez unikalny klucz – identyfikator **qmsqid (queue identifier)** – będący nieujemną liczbą całkowitą. 