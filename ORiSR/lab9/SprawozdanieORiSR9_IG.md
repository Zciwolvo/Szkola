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

<h2 style="text-align:center; border: none;"><b>Sprawozdanie nr 9</b></h3>
<h2 style="text-align:center; border: none;">mutex</h2>

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


## Przebieg ćwiczenia

W odniesieniu do wątków, podobnie jak i procesów można stosować celem synchronizacji
semafory POSIX aczkolwiek jest to sposób co najmniej niewygodny.
Standard IEEE POSIX począwszy od 1003.1c (1995), dla potrzeb wątków implementuje
semafory MUTEX.

Są one reprezentowane za pośrednictwem typu mutex_t (bits/pthreadtypes.h włączany do
pthreads.h). Przed użyciem semafor mutex musi być – oczywiście – zainicjowany, a - kiedy
już będzie niepotrzebny - z pamięci.

MUTEX z definicji jest semaforem binarnym a więc dwustanowym, przeznaczonych od ochrony
zasobów udostępnianych na wyłączność.
Chęć dostępu do zasobu powinna być poprzedzona wywołaniem **pthread_mutex_lock()** a jego
zwolnienie **pthread_mutex_unlock()**, co stanowi analogię **P()** **(wait())** i **V()** **(signal())**
Dijkstry.

Funkcja pthread_mutex_trylock() dokonuje dostępności zasobu bez wprowadzania blokady,
aczkolwiek generuje błąd **EBUSY** jeżeli zasób współdzielony jest niedostępny.

Zacznijmy od prostego przykładu Daniela Robbinsa (nieznacznie zmodyfikowanego)
ilustrującego sytuację wyścigu w dostępie do zasobu – tutaj – będzie to zmienna globalna, w
przypadku dwóch wątków: główny w **main()** a potomny wykona **thread()**.

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
int N=0; //...zmienna na której będziemy działać
void *thread( void *arg )
{
    int n,i;
    for ( i=0;i<5;i++ )
    {
        n = N; //...pobieramy wartość zmiennej globalnej
        n++; //...inkrementacja kopii lokalnej
        printf("thread() [%lu]\n",(unsigned long)pthread_self());
        fflush( stdout );
        sleep( 1 ); //...czekamy 1 sekundę
        N = n; //...przypisanie wartości zmiennej globalnej
    }
    pthread_exit( NULL );
}

int main( void )
{
    pthread_t tid;
    int i;
    //...tworzymy jeden wątek potomny (może trochę niefortunne określenie)
    if( pthread_create( &tid,NULL,thread,NULL ) )
    { 
        perror( "...pthread_create()..." ); 
        exit( 1 ); 
    }
    for ( i=0;i<5;i++)
    {
        N--; //...dekrementacja globalnej, w wątku głównym
        printf( "main() [%lu]\n",(unsigned long)pthread_self() );
        fflush( stdout );
        sleep( 1 ); //...czekamy 1 sekundę
    }
    if( pthread_join( tid,NULL ) )
    { 
        perror( "...pthread_join()..." ); 
        exit( 2 ); 
    }
    printf( "\nglobalnie N=%d, po wykonaniu 5+5 iteracji\n",N );
    return 0;
}
```

Co ciekawe pomimo tego że zarówno wątek jak i proces, wykonują tą samą lecz przeciwną operację wynik nie wychodzi równy 0 tylko jak poniżej

```bash
$ ./zero
main() [140390545930048]
thread() [140390545925888]
main() [140390545930048]
thread() [140390545925888]
main() [140390545930048]
thread() [140390545925888]
main() [140390545930048]
thread() [140390545925888]
thread() [140390545925888]
main() [140390545930048]
```

Prześledźmy wykonanie wątków:
- proces jest uruchamiany N = 0
- zgodnie z komunikatem main() wykonuje N-- (czyli jest -1) i zasypia na 1 sekundę;

następnie:

- sterowanie uzyskuje thread() pobiera pobiera N i przypisuje n (czyli jest-1), wykonuje n++ (czyli w n jest 0) i zasypia na 1 sekundę;
- w tym momencie budzi się main() i wykonuje wykonuje N-- (czyli jest -2) i zasypia;
- budzie się thread() i wykonuje przypisanie N=n, więc podstawia 0 do N, i rozpoczynając kolejną iterację n będzie także 0, więc po n++ będzie miał w n wartość 1, i zasypia;
- powraca mian() mając w zmiennej globalnej 0, wykonuje N-- (czyli jest -1) i zasypia;
- ale thread() odzyskuje sterowanie i podstawia pod N wartość 1, następnie pobiera tę wartość i inkrementuje w zmiennej lokalnej n (uzyskuje w ten sposób 2);

proces ten jest kontynuowany i w efekcie finalnym uzyskujemy

4

zamiast

0

bowiem konieczne byłoby tutaj zastosowania semafora zamykającego w niepodzielnym bloku –
mimo i wbrew relacjom czasowym – działań realizowanych przez oba wątki.

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER; //...konieczna deklaracja
int N=0;
void *thread( void *arg )
{
    int n;
    int i;
    for ( i=0;i<5;i++ )
    {
        pthread_mutex_lock( &mutex ); //...zgłoszenie
        n = N; n++;
        printf( "thread() [%lu]\n",(unsigned long)pthread_self() );
        fflush( stdout );
        sleep( 1 ); N = n;
        pthread_mutex_unlock( &mutex ); //...i zwolnienie
    }
    pthread_exit( NULL );
}

int main( void )
{
    pthread_t tid;
    int i;
    if( pthread_create( &tid,NULL,thread,NULL ) )
    { 
        perror( "...pthread_create()..." ); 
        exit( 1 ); 
    }
    for ( i=0; i<5; i++)
    {
    pthread_mutex_lock( &mutex );
    N--;
    printf( "main() [%lu]\n",(unsigned long)pthread_self() );
    fflush( stdout );
    sleep( 1 );
    pthread_mutex_unlock( &mutex );
    }
    if( pthread_join( tid,NULL ) )
    { 
        perror( "...pthread_join()..." ); 
        exit( 2 ); 
    }
    if( pthread_mutex_destroy( &mutex) )
    { 
        perror( "...pthread_mutex_destroy()..." ); 
        exit( 3 ); 
    }
    printf( "\nglobalnie N=%d, po wykonaniu 5+5 iteracji\n",N );
    return 0;
}
```

Tym razem otrzymamy już oczekiwany wynik

```bash
$ ./tzero
main() [133727424735040]
main() [133727424735040]
thread() [133727424730880]
thread() [133727424730880]
thread() [133727424730880]
thread() [133727424730880]
thread() [133727424730880]
main() [133727424735040]
main() [133727424735040]
main() [133727424735040]
```

Natomiast wniosek bardziej ogólny jest taki, że w przypadku wątków należy zwracać baczną
uwagę na ewentualne skutki uboczne do zmiennych globalnych, które zawsze są
"współdzielone" między wątkami.

Jak wiadomo suma kolejnych liczb naturalnych wyraża się

n=1,2,3,....,n

n*(n+1)/2

Przygotujemy program, który wykorzystując wątki oblicza sumę tego rodzaju ciągu.
