# WPAM-Projekt-Backend

Backend do aplikacji mobilnej wykonanej w ramach projektu z przedmiotu WPAM.  
Link do aplikacji mobilnej: [LINK](https://github.com/kubasikora/WPAM-Projekt-Aplikacja)

**Autorzy**:  
- Adam Jęczmień
- Jakub Sikora

## Instalacja 
W pierwszym kroku należy przygotować wirtualne środowisko języka Python. W tym celu wykorzystany zostanie `virtualenv`. 
Po sklonowaniu repozytorium i przejściu do korzenia projektu, należy wywołać polecenie `virtualenv .`. Utworzy to wirtualne środowisko, poprzez utworzenie folderów `bin/` i `lib/` oraz pliku `pyvenv.cfg`. 

Aby wejść do wirtualnego środowiska, należy wykonać polecenie `source bin/activate`. W wirtualnym środowisku, korzystamy z bibliotek oraz Pythona w tej samej wersji. Przy pierwszym uruchomieniu środowiska wirtualnego należy zainstalować wszystkie pakiety za pomocą polecenia `pip install -r requirements.txt`. W celu skonfigurowania lokalnej bazy danych w sqlite3, należy wykonać polecenie `python manage.py migrate`. 

## Uruchomienie aplikacji
Aplikacje uruchamiamy w wirtualnym środowisku. W celu uruchomienia serwera deweloperskiego, należy wykonać polecenie `python manage.py runserver`. Serwer automatycznie odświeża aplikacje przy zapisaniu plików źródłowych oraz nasłuchuje na porcie `8000`.

## Zmiana modelu
W celu zmiany modelu danych, w pierwszej kolejności zmieniamy plik models.py. Uaktualni to wewnętrzny model aplikacji. Kolejnym krokiem jest przygotowanie migracji bazy danych. Wykonujemy to poleceniem `python manage.py makemigrations`. Utworzy to skrypt migracji, wykonujemy go poleceniem `python manage.py migrate`. Aktualnie korzystamy z lokalnej bazy, więc nie dodajemy skryptów migracyjnych do repozytorium.

## Dodawanie zewnętrznych bibliotek
Dodatkowe biblioteki instalujemy poprzez `pip`. W pierwszej kolejności, upewniamy się że jesteśmy w wirtualnym środowisku. Instalujemy pakiet za pomocą polecenia `pip install <nazwa-biblioteki>`. Ostatnim krokiem jest zaktualizowanie pliku `requirements.txt` za pomocą polecenia `pip freeze > requirements.txt`. Zapisze to informacje o dodatkowej bibliotece i pozwoli innym osobom w projekcie na szybką instalację.

## Utworzenie admina
Przed użyciem aplikacji należy stworzyć konto admina, wykorzystując polecenie `python manage.py createsuperuser`. Po uzupełnieniu wszystkich informacji, zostanie utworzone konto administracyjne. Panel administracyjny można otworzyć w przeglądarce wchodząc na stronę `http://localhost:8000/admin`. Z poziomu administratora można tworzyć nowe konta zwykłych użytkowników.

## Deployment na chmurę
Aplikacja jest hostowana na heroku pod linkiem [https://wpamprojekt-prod.herokuapp.com/](https://wpamprojekt-prod.herokuapp.com/). Aby wrzucić nową wersję należy zalogować się w heroku CLI za pomocą polecenia `heroku login`. Następnie budujemy nowy obraz aplikacji i wrzucamy go na chmurę za pomocą polecenia `heroku container:push web --app wpamprojekt-prod`. Po poprawnym wrzuceniu obrazu, uruchamiamy kontener za pomocą polecenia `heroku container:release web --app wpamprojekt-prod`. Po chwili aplikacja powinna zostać zaktualizowana. Podobne działania należy wykonać z wersją deweloperską, hostowaną pod linkiem [https://wpamprojekt-dev.herokuapp.com/](https://wpamprojekt-dev.herokuapp.com/). Różnica pomiędzy prodem a devem jest taka że na prodzie wymagany jest token uwierzytelniający a na devie nie.

## Uruchomienie offline
Aby uruchomić backend lokalnie, należy upewnić się że ma się zainstalowany serwer bazy danych `postgres`. Najwygodniejszym sposobem jest uruchomienie kontenera z bazą, z podpiętym volumem, tak aby nie utracić danych. Aby uruchomić kontener należy wykonać polecenie: `docker container run -p 5432:5432 -v wpamprojekt:/var/lib/postgresql/data -e POSTGRES_USER=wpam -e POSTGRES_DB=wpam -e POSTGRES_PASSWORD=wpam postgres`. Aby przełączyć się na lokalną bazę danych, należy ustawić zmienną środowiskową `USE_LOCAL_DB` na wartość `True`. Oprócz tego ustawiamy zmienne `LOCAL_DB_NAME`, `LOCAL_DB_USER` oraz `LOCAL_DB_PASSWORD` na to co ustawiliśmy przy uruchamianiu kontenera (tutaj wszędzie `wpam`).
