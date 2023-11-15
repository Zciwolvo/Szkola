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

Z poziomu interface'u użytkownika informacja o istniejących kolejkach komunikatów może być
pobrana poleceniem

```bash
$ ipcs -q

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages    

```

W przypadku gdyby w kolejce były opecje jakieś rekordy możemy je wyczyścić za pomocą:

`$ ipcrm [-Q msgkey] | [-q msgid]`

Celem obsługi tego sposobu komunikacji, w obszarze pamięci jadra tworzona jest tablica
kolejek msgque[] o rozmiarze (maksymalnym) MSGMNI, której elementem składowym są
struktury o definicji (w linux/msg.h)

Tablica ta jest indeksowana za pośrednictwem identyfikatora danej kolejki qid. Zauważmy, że
Struktura ta zawiera w szczególności wskazania, w postaci msg_first i msg_last
identyfikujące listę komunikatów powiązanych z daną kolejką.

Nowa kolejka jest tworzona, co wiąże się z "dopisaniem" do tablicy msgque struktury
msqid_ds a jeżeli już istnienie, to jest otwierana celem uzyskania dostępu wywołaniem funkcji
msgget().

TODO

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/msg.h>
#include <time.h>
#define PROJECTID 666
int main( void )
{
    key_t key;
    int flag, msqid;
    struct msqid_ds buffer;
    //Generujemy klucz dla potrzeb utworzenia kolejki podając pewien arbitralnie obrany
    //(ale – koniecznie – istniejący katalog; z pewnością /tmp będzie istniał), a ponadto pewną
    //wartość liczbową (tutaj stała PROJECTID)
    key = ftok( "/tmp",_PROJECT_ID );
    //Następnie tworzymy kolejkę (uprawnienia odczytu i zapisu tylko dla użytkownika)
    flag = IPC_CREAT | 0x100 | 0x80;
    msqid = msgget( key,flag );
    if( msqid<0 ){ perror( "!.!..msgget().." ); exit( 1 ); }
    else
    {
        //Jeżeli tak, to pobieramy o niej informacje
        if( !msgctl( msqid,IPC_STAT,&buffer ) )
        {
            //Identyfikator kolejki
            printf( "\tKOLEJKA [%d]\n",(int)msqid );
            //Dla pewności pobieramy nasz UID i GID
            printf( "\tuid:%d gid:%d\n",(int)getuid(),(int)getgid() );
            //... i sprawdzenia zawartości struct msqid_ds
            printf( "\t%s",ctime( &(buffer.msg_ctime ) ) );
            printf( "\tuid:%dgid:%d\n",(int)buffer.msg_perm.uid,
            (int)buffer.msg_perm.gid );
            printf( "\tkey: 0x%x\n",buffer.msg_perm.__key );
            printf( "\trozmiar kolejki: %lu B / %u MSG\n",
            buffer.msg_cbytes,(unsigned)buffer.msg_qnum );
            /* msgctl( msqid,IPC_RMID,&buffer ); */
        }
        else{ perror( "!.!..msgctl.." ); exit( 2 ); }
    }
    return 0;
}
```