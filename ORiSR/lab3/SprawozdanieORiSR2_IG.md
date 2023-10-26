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

<h2 style="text-align:center; border: none;"><b>Sprawozdanie nr 3</b></h3>
<h2 style="text-align:center; border: none;">Łącza nazwane</h2>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

GRUPA: 2B / SEMESTR: 5 / ROK: 3

Igor Gawłowicz / 59096

Krystian Niedźwiedź / 58824

<div style="page-break-after: always;"></div>

Prócz ewidentnych zalet i korzyści wynikających z użycia w
komunikacji międzyprocesowej łączy nienazwanych, mimo
wszystko nie zawsze warto (a nawet można) je stosować.
Zasadniczym utrudnieniem w przypadku łączy nienazwanych
jest kwestia współużytkowania takiego łącza przez procesy
niespokrewnione.
W takiej sytuacji zwykle lepszym wyborem będą łącza w
postaci potoku nazwanego (**named pipe**). 

W odróżnieniu od nienazwanych, łącze nazwane (**named pipe**):

- jest identyfikowane przez nazwę i może z niego korzystać dowolny proces (także niespokrewniony), o ile ma odpowiednie uprawnienia;
-  posiada organizację **FIFO**, czyli **First In First Out** (stąd i ich skrótowa nazwa);
- posiada dowiązanie w systemie plików (jako plik specjalny urządzenia), aż do momentu jawnego usunięcia;
-  mimo iż zachowuje cechy pliku – jak wyjaśnia to dokumentacja systemowa LINUX: ... is a window into the kernel memory, that "looks" like a file ...

**Named pipe**, podobnie jak i łącza nienazwane, mogą być tworzone w dwojaki sposób, a
mianowicie z:
- systemowego interface'u użytkownika;
- procesu (czy wątku), wywołaniem odpowiedniej funkcji API systemowego
  
Z poziomu interface systemowego łącza nazwane FIFO, tworzone są komendą

`$ mkfifo -m mode name`

mode maska praw dostępu, czyli symbolicznie dla **u** (user), **g** (group), **o** (other), **a** (all)
dodaje (+), ujmuje (-) od istniejących lub ustawia (=) prawo **r** (read), **w** (write), **x** (execute)
name nazwa pliku specjalnego FIFO, ewentualnie wraz ze ścieżką

Usunięcie łącza nazwanego odbywa się w identyczny sposób jak każdego pliku dyskowego, a więc

`$ rm name`

Utwórzmy w takim razie przykładowe łącze FIFO 

`$ mkfifo -m a=rw /tmp/km-fifo`

Jeżeli wykonamy teraz

```bash
$  ls -l /tmp/km-*
prw-rw-rw- 1 zciwolvo zciwolvo 0 Oct 26 15:41 /tmp/km-fifo
```

Takie cechy pliku km-fifo potwierdza także, w szczegółach, komenda stat

```bash
$ stat /tmp/km-fifo
  File: /tmp/km-fifo
  Size: 0               Blocks: 0          IO Block: 4096   fifo
Device: 51h/81d Inode: 2594713     Links: 1
Access: (0666/prw-rw-rw-)  Uid: ( 1000/zciwolvo)   Gid: ( 1000/zciwolvo)
Access: 2023-10-26 15:41:51.685573925 +0000
Modify: 2023-10-26 15:41:51.685573925 +0000
Change: 2023-10-26 15:41:51.685573925 +0000
Birth: 2023-10-26 15:41:51.685573925 +0000
```

Otwórzmy teraz dwie sesje terminala, w oknie pierwszego pierwszego wpisujemy

`$ cat < /tmp/km-fifo`

czyli przekierujemy zawartość km-fifo na wejście komendy systemowej cat. Ta, jak wiadomo,
wyświetla na swoim wyjściu (czyli tutaj w oknie terminala pierwszego), to co otrzyma na wejściu.
Teraz przełączamy się na drugie okno terminala, i wykonujemy

`$ cat > /tmp/km-fifo`

czyli w przeciwnym kierunku, zatem wejście drugiego terminala zostało przekierowane na plik kmfifo. Efekt będzie taki, że cokolwiek wprowadzimy w oknie terminala drugiego, natychmiast
zobaczymy w oknie pierwszego. Zauważmy że plik ten będzie miał przez cały czas rozmiar zerowy. 

input (odróżniamy od outputu za pomocą znaku `>`)
```bash
$ cat > /tmp/km-fifo
test polaczenie km-fifo
```

output (odróżniamy od outputu za pomocą znaku `<`)
```bash
$ cat < /tmp/km-fifo
test polaczenie km-fifo
```


