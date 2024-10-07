Aplikacja z podziałem na role: Admi, User

Admin ma dostęp do CRUDa na danych użytkownika
Użytkownik po pierwszym logowaniu musi zmieniać hasło,
system zapamiętuje 12 ostatnich haseł użytkownika i każde następne musi być różne od tych 12.
Wariant hasła: conajmniej 8 znaków, jedna wielka litera, jeden znak specjalny
Po minięciu podanego czasu od ostatniej zmiany hasła użytkownik także będzie musiał zmienić hasło

Struktura bazy
{
ID: str,
passwords: list(str),
role: str,
new_user: bool,
change_timestamp: timestamp,
}
