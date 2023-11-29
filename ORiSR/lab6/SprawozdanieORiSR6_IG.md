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

<h2 style="text-align:center; border: none;"><b>Sprawozdanie nr 6</b></h3>
<h2 style="text-align:center; border: none;">Użycie i zarządzanie wątkami</h2>

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

## Przebieg ćwiczenia

Proces jako pewna instancja programu, w trakcie wykonania, ze swej natury w każdym
systemie operacyjnym wyróżniają:
- prawa własności zasobu a jednym z fundamentalnych zadań systemu jest ochrona przed jednoczesnym dostępem;
- szeregowanie i wykonanie procesów odbywa się z poziomu systemu operacyjnego.

W odróżnieniu od procesu, wątek stanowi podzbiór przestrzeni adresowej procesu,
współdzielący jego stan i zasoby (również deskryptory plików) – aczkolwiek nie dziedziczy
stosu procesu (stack).

Dzięki temu komunikacja między wątkowa nie wymaga użycia systemowych mechanizmów
inter-process communication a przełączanie kontekstu (context switch) jest niewspółmiernie
szybsze niż w przypadku procesu.

Ponieważ jest uzupełnieniem API systemowego, wymagana jest jawna konsolidacja z
libpthread.so (albo libpthread.a)

**gcc -Wall <source>.c -o <exec> -lpthread**

Podobnie jak każdemu procesowi w chili jego tworzenia przypisywane jest unikalne \
**pid_t id;**
tak też i wątkowi \
**pthread_t id;**

Wątek może pobrać swój identyfikator wywołaniem

**#include <pthread.h>**\
**pthrad_t pthread_self(void);**

Wątek tworzony jest wywołaniem funkcji **pthread_create()**

Zakończenie wątku może nastąpić z czterech przyczyn:
- zwrócenie sterowania z wątku (wywołanie return, exit(), _exit());
- wywołanie z wątku nadrzędnego (macierzystego);
- z innego wątku wywołaniem\
**#include <pthread.h>**\
**int pthread_cancel( pthread_t tid );**\
- jawne wywołanie funkcji **pthread_exit()** z kodem powrotu code.
**#include <pthread.h>**\
**void pthread_exit( void *code );**

Przedstawimy teraz prosty przykład tego co się stanie jeśli uruchomimy jednocześnie proces i wątek, żeby działały równocześnie

```cpp
#include<stdio.h>
#include<pthread.h>
#define LIMIT 100

void* o( void* unused )
{
    (void)unused;
    while( LIMIT ){ putchar( 'o' ); }
    return 0;
}

int main( void )
{
    int current = 0;
    pthread_t tid;
    pthread_create( &tid,NULL,&o,NULL );
    while( current < LIMIT )
    { 
        putchar( 'x' ); 
        current += 1;    
    }
    return 0;
}
```