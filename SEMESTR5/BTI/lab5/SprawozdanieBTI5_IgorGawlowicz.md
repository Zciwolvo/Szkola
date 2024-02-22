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
}f
 </style>
<h1>LABORATORIUM BEZPIECZEŃSTWO TECHNOLOGII INFORMATYCZNYCH</h1>

&nbsp;

&nbsp;

<style>

</style>

<centerer>
    <Ltext>Data wykonania ćwiczenia:</Ltext>
    <div align="center">
        <rectangle>
            <Rtext>07.11.2023</Rtext>
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
            <Rtext>5</Rtext>
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
        <Rtext>5</Rtext>
    </rectangle>
</row>

&nbsp;

&nbsp;

<b>Temat: </b> Analiza Plików Cookie i Sposobów Ich Wykorzystywania

&nbsp;

&nbsp;

<b>Osoby wykonujące ćwiczenia: </b>

1. Igor Gawłowicz

&nbsp;

&nbsp;

<h1>Katedra Informatyki i Automatyki</h1>

<div style="page-break-after: always;"></div>

### **Cel zadania:**

Celem tego ćwiczenia jest zrozumienie, jak witryny internetowe wykorzystują pliki cookie i jak można je analizować.

### **Wstęp teoretyczny**

Pliki cookie są powszechnie stosowanym narzędziem w dzisiejszym świecie internetu. Służą do przechowywania informacji na komputerach użytkowników, pozwalając witrynom internetowym na personalizację treści, dostosowywanie preferencji użytkowników i śledzenie ich aktywności. Pliki cookie mogą mieć wiele zastosowań, zarówno w celu ułatwienia korzystania z witryny, jak i w celach marketingowych i analitycznych.

Podczas gdy pliki cookie mogą być użyteczne dla witryn i użytkowników, istnieją również pewne obawy dotyczące prywatności i bezpieczeństwa. Ze względu na to, że pliki cookie przechowują informacje na komputerach użytkowników, mogą stwarzać potencjalne ryzyko związane z prywatnością i bezpieczeństwem. Przechowywane w plikach cookie dane, takie jak identyfikatory sesji, preferencje użytkownika czy informacje o zakupach, mogą stać się celem ataków, nadużyć lub naruszeń prywatności.

W ramach tego ćwiczenia laboratoryjnego zajmiemy się analizą plików cookie na przykładzie różnych witryn internetowych. Naszym celem będzie zrozumienie, w jaki sposób witryny wykorzystują pliki cookie oraz jakie informacje gromadzą. Będziemy także rozważać kwestie związane z bezpieczeństwem i prywatnością użytkowników w kontekście plików cookie.

Pliki cookie to nie tylko narzędzie, które pozwala witrynom internetowym na zapamiętywanie naszych preferencji czy zawartości koszyka zakupowego. To także element, który może mieć wpływ na naszą prywatność i bezpieczeństwo online. Dlatego analiza ich działania i zrozumienie, jakie informacje gromadzą, jest kluczowym elementem w dziedzinie bezpieczeństwa informatycznego.

### **Wybór witryn i analiza plików cookies**

## marmaid

Pierwszą witryną którą przebadamy będzie strona *https://mermaid.js.org*, która zawiera dokumentacje narzędzia do tworzenia wykresów i diagramów.

Witryna korzysta z następujących ciasteczek:

### dotcom_user
Wartość: `Zciwolvo` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `2024-10-19T11:04:19.023Z` \

### logged_in
Wartość: `yes` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `2024-10-19T11:04:19.023Z` \

### _device_id
Wartość: `71abe65922f62f16228cbe46bff8d28d` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `2024-10-19T11:04:19.023Z` \

### _octo_
Wartość: `GH1.1.413365645.1697713439` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `2024-10-19T11:04:19.023Z` \

### __Host-user_session_same_site
Wartość: `fcKIBg8Nx6Ux0S1c2n-waKQGnJKKTA9jgo3glBblqpQj4hSv` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `2024-10-19T11:04:19.023Z` \

### user_session
Wartość: `fcKIBg8Nx6Ux0S1c2n-waKQGnJKKTA9jgo3glBblqpQj4hSv` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `2024-10-19T11:04:19.023Z` \

### _gh_sess
Wartość: `%2BxmD73VqkcJWMQDJMP4jEKXHbSJOiS3Y8Y4nkbVYm55QmhppfZGcWO%2BPVUTDAxsPLBMlNKrmb6BpVwO%2FEG9FxNh1NxX%2Ftjyox8NUUVtdhfSAzN%2FqWDin7Asb%2BputCCKJJDPGbb%2FksYUE2XOSBg1iqGuYeMuyl6b2hQ8g2a95d5aeliHOxpNCp3IiYwV6AIaGouyM09qxAc3vLqcQvmnK7%2FD0G%2BAU%2FgqTp%2F4oPN93joAJH4NIg%2FfJIXY0EtkKDihT%2BKdjjclQhfXFFXsuPkC9iqhqrEbZhp9TYpdoA2jCeAqcOEX4weNAvYUf5GmFpYC9b%2FoptVr2HIMRJ8owKnK3cix6wDLPQXqJQAvtXxvk%2BZE%2FKXDcztJfcgTEesc2adjYf1ibK2wlRjLMy2VxVB9jpaMoVGQiK4tlHtnlJ9DkveTxdD8D9eB3KRVOltxfCuoFr9qkSk%2FVNhFC6cg3AInuY3xY60YV%2Bov8NDuCc6CHXMq8jhs0gOXIrIFS%2FH4k0RHv0scJWGjrsPPEaDIQjjOTCsnObOywDf6mlhtrGwG%2F3pKrZEd%2Bi9b%2BVuu0wu7SsPjJcw3oUgncIGNHV%2F9vBWIHC%2B3MvgncgXkiUcWx4%2BsJMSLn424aPtweQSjc5VHToKZe62S17XU2BhyggpBF9LHe3YsnsdJurJ2ixV3bDTDpDTy9HqP5p7ZWgrDEfhHRi%2FDtllrdfJ8SgcLnCTo5RUpaROZ8hM58oIi2U26mNUWTOvRgj692WWwhFT9seUAvWTSEup%2FwUe2l54YGfatm09k0a0LumUqw064kRpQoHAtp9mpQSRuciZzVhcO1HotPqGiZylHkUhRZOUKbcw3OJk%2FTSWD80F3SKLzQwAFajZQ4IKcoUZKWyHppOIt4%2FzaCAUzrj3NXaOH1m0dKWQKhAg9MWDaPYUF%2BwZp1A4F5IlFxlLAzXuZoBVuxW4994tvksM9drPWJ8jJQsnlss2ZsIGIaszLfsPFi13gU1%2FMfrujEXpuA0jjWTZ%2BFlg%3D%3D--AbFa6Oqrg%2FTmc%2Fol--ww3Hi6EASqs4rZYoI18PAA%3D%3D` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `Session` \

### color_mode
Wartość: `%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `Session` \

### tz
Wartość: `Europe%2FWarsaw` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `Session` \

### preferred_color_mode
Wartość: `dark` \
Domain: `.github.com` \
Path: `/` \
Data wygaśnięcia: `Session` \

Z racji że powyższa strona jest witryną postawioną na githubie jako github docs, większość plików cookie zawiera informacje o statusie logowania oraz o identyfikatorach sesji, część z tych danych to tokeny potwierdzające nasze dane za pomocą czegoś takiego jak JWT Token, a pozostała część to preferencje takie jak preferowana kolorystyka czy strefa czasowa użytkownika.

Na podstawie tych cookies nie jesteśmy zagrożeni ponieważ wszystkie te dane to tylko tymczasowe tokeny lub publicznie widoczne dane, chyba najbardziej wrażliwą informacją w tej puli jest moja nazwa użytkownika na githubie która i tak jest informacją publiczną widoczną na stronie.

## aliexpress

Troszkę innym rodzajem witryny są strony marketingowe, których głównym celem jest zdobycie jak największej ilość informacji od użytkownika, przykładem takiej strony będzie np. Aliexpress, już na pierwszy rzut oka możemy zauważyć, że zamiast kilku bezpiecznych ciasteczek widzimy ich dziesiątki, gdzię duża część nie dość że nie jest bezpieczna to ma nic nie przekazywującą nazwę, a w środku kolejne nic nie znaczące dla użytkownika tokeny.

### sca
Wartość: `2ca676d7` \
Domain: `.mmstat.com` \
Path: `/` \
Data wygaśnięcia: `Session` \
### l

Wartość: `fBQGiQAHPRlWDG7CBOfwFurza77OsKRA_uPzaNbMi9fP_b5J565lW1FZ5TYvCnMNFsn9R3Rinax6BeYBqCDn9kPSNwG_N7HmnXr9aX5..` \
Domain: `.aliexpress.com` \
Path: `/` \
Data wygaśnięcia: `2024-05-05T17:25:38.000Z` \

### _m_h5_tk_enc  
Wartość: `15fe8cbd9c0485ef54ec16b1be0ee572` \
Domain: `.aliexpress.com` \
Path: `/` \
Data wygaśnięcia: `2023-11-14T17:25:37.432Z` \

### intl_locale
Wartość: `pl_PL` \
Domain: `.aliexpress.com` \
Path: `/` \
Data wygaśnięcia: `Session` \

### intl_common_forever
Wartość: `9qfoOwgbp/8E8ApiqX01pTw5Bx3r8qwVLFjPiJfzG9iab1CtOHuArQ==` \
Domain: `.aliexpress.com` \
Path: `/` \
Data wygaśnięcia: `2024-12-11T17:25:34.350Z` \

### ali_apache_tracktmp
Wartość: ` ` \
Domain: `.aliexpress.com` \
Path: `/` \
Data wygaśnięcia: `Session` \

### isg
Wartość: `BL-_QoK45rxuM-KgMqdyDN9sXpNJpBNGmyCz_FGMW261YN_iWXSjlj1ioCieI-u-` \
Domain: `.alicdn.com` \
Path: `/`  \
Data wygaśnięcia: `2024-05-05T17:25:47.000Z` \

Jest to tylko kilka z wielu, jednak już z takiej dawki możemy wyciągnąć kilka wniosków.

Duża ilość plików cookie zazwyczaj oznacza to, że strona ma dokładniejszy profil użytkownika co ma swoje plusy i minusy, w ten sposób otrzymamy np. reklamy trafiające w nasze preferencje i zapotrzebowania, jednak tym samym sposobem jesteśmy bombardowani reklamami z każdej strony.

Musimy tutaj także zauważyć, że wbrew pozorą aliexpress jest stroną pozornie bezpieczną więc w najgorszym przypadku ktoś może zdobyć nasze preferencje reklamowe, jednak przy bardziej podejrzanych i potencjalnie niebezpiecznych witrynach, źle wykorzystane pliki cookies czasem mogą nawet wpłynąć na wydajność naszych przeglądarek.

## Wnioski

Pliki cookie stanowią istotne narzędzie w świecie internetowym, umożliwiając personalizację treści, śledzenie aktywności użytkowników, analizę statystyk i efektywne reklamowanie. Jednak ich przydatność niesie ze sobą kwestie bezpieczeństwa i zagrożenia dla prywatności. Bez odpowiedniego zabezpieczenia i transparentności ze strony witryn, dane użytkowników przechowywane w plikach cookie mogą być narażone na ryzyko ataków hakerskich oraz naruszeń prywatności. Dlatego ważne jest, aby witryny i przeglądarki oferowały mechanizmy ochrony przed śledzeniem i były przejrzyste w kwestiach związanych z polityką prywatności, pozwalając użytkownikom kontrolować wykorzystanie plików cookie. Warto być świadomym zarówno korzyści, jak i potencjalnych zagrożeń związanych z plikami cookie.