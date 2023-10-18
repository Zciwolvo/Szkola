# Skład grupy

- Igor Gawłowicz
- Tomasz Wawoczny

# Zrozumienie wymagań

1. Nazwa obiektu: Klinika medyczna "HealthCare Plus"
2. Liczba pracowników: 15
3. Liczba urządzeń: 25 (w tym komputery lekarzy i sprzęt medyczny)
4. Usługi sieciowe: Przechowywanie i udostępnianie historii medycznych pacjentów oraz wyników badań.

# Wybór topologii sieci

Rozważmy najpierw nasze możliwości

## Topologia Gwiazdy:
- Wszystkie urządzenia są podłączone bezpośrednio do głównego switcha lub koncentratora.
- Zapewnia łatwy dostęp do zarządzania i diagnostyki sieci.
- Zapewnia redundancję w razie awarii jednego łącza, ponieważ pozostałe urządzenia pozostają aktywne.

Wady:
- Wymaga większej ilości kabli, ponieważ każde urządzenie musi być bezpośrednio podłączone do centralnego urządzenia.

## Topologia Magistrali:

- Wszystkie urządzenia są podłączone do jednego wspólnego kabla.
- Prosta w implementacji i kosztoszczędna.

Wady:
- Brak redundancji, awaria kabla głównego może unieruchomić całą sieć.

## Topologia Pierścienia:

- Każde urządzenie jest podłączone do dwóch sąsiednich urządzeń, tworząc zamknięty pierścień.
- Ma wbudowaną redundancję, ponieważ w przypadku awarii jednego odcinka, dane nadal mogą krążyć w drugim kierunku.

Wady:
- Skomplikowana w zarządzaniu i wymaga więcej kabli niż topologia gwiazdy.

<div style="page-break-after: always;"></div>

## Wnioski

Dla kliniki medycznej "HealthCare Plus", najlepszym wyborem może być topologia gwiazdy. Jest to stabilne rozwiązanie, które zapewnia prosty dostęp do zarządzania siecią oraz pozwala na łatwe rozszerzenie sieci w przyszłości. Ponadto, można rozważyć wykorzystanie switchy z funkcją redundancji (np. stosowane w technologii High Availability), aby zapewnić niezawodność w przypadku awarii.