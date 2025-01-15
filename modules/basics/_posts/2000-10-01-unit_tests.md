---
title: Unit Testing met pytest
---

<div class="header1" id="top" markdown="1"># Unit Testing met pytest
</div>

<div class="header2" markdown="1">## Introductie
</div>

### Wat is Unit Testing?

Unit testing is het proces van het testen van kleine stukjes code, genaamd "units", om ervoor te zorgen dat ze correct werken. Een unit kan een enkele functie, methode of klasse zijn.

**Waarom is unit testing belangrijk?**

- **Vroegtijdige bugdetectie:** Het helpt bij het vinden van fouten vroeg in het ontwikkelproces.
- **Betere codekwaliteit:** Zorgt voor betrouwbare en onderhoudbare code.
- **Gemakkelijkere wijzigingen:** Met tests kun je code aanpassen zonder bang te zijn iets te breken.

### pytest

pytest is een populair en gebruiksvriendelijk testframework voor Python. Het maakt het schrijven van tests eenvoudig en leesbaar.

**Voordelen van pytest:**

- Eenvoudige syntax met gebruik van standaard `assert`-statements.
- Automatische testontdekking zonder extra configuratie.
- Uitbreidbaar met plugins en fixtures.

### Installatie van pytest

#### Stap 1: Installeren van pytest

Installeer pytest via `pip3` (het pakketbeheerprogramma voor Python):

```bash
pip3 install pytest
```

#### Controleren van de installatie

Controleer of pytest correct is geïnstalleerd:

```bash
pytest --version
```

Je zou iets moeten zien als `This is pytest version X.X.X`.

### Schrijven van je Eerste Test

#### Stap 1: Een eenvoudige functie schrijven

Maak een nieuw Python-bestand genaamd `rekenmachine.py` en voeg de volgende code toe:

```python
# rekenmachine.py

def optellen(a, b):
    return a + b
```

Deze functie neemt twee getallen en retourneert hun som.

#### Stap 2: Een testbestand maken

Maak een nieuw bestand genaamd `test_rekenmachine.py` in dezelfde map en voeg de volgende code toe:

```python
# test_rekenmachine.py

from rekenmachine import optellen

def test_optellen():
    assert optellen(2, 3) == 5
```

**Uitleg:**

- **Importeren van de functie:** We importeren de `optellen`-functie uit `rekenmachine.py`.
- **Schrijven van de testfunctie:** Testfuncties beginnen met `test_` zodat pytest ze automatisch kan vinden.
- **Gebruik van `assert`:** We gebruiken het `assert`-statement om te controleren of `optellen(2, 3)` gelijk is aan `5`.

#### Stap 3: De test uitvoeren

Open de terminal, navigeer naar de map met je bestanden en voer uit:

```bash
pytest
```

**Verwachte output:**

```bash
==================== test session starts ====================
collected 1 item

test_rekenmachine.py .                                 [100%]

===================== 1 passed in X.XXs ======================
```

Een punt `.` betekent dat de test is geslaagd.

### Experimenteren met Tests

#### Meerdere asserties toevoegen

Je kunt meer asserties toevoegen om verschillende gevallen te testen:

```python
def test_optellen():
    assert optellen(2, 3) == 5
    assert optellen(-1, 1) == 0
    assert optellen(0, 0) == 0
```

Voer de tests opnieuw uit met `pytest` om te zien of ze slagen.

#### Fouten opsporen

Probeer een fout te introduceren om te zien hoe pytest reageert:

```python
def test_optellen():
    assert optellen(2, 3) == 6  # Dit zal falen
```

Voer `pytest` uit en bekijk de foutmelding. Dit helpt je begrijpen hoe pytest je informeert over testfouten.

### Oefeningen

#### Oefening 1: Omkeren van een String

**Opdracht:**

Maak een nieuw bestand `strings.py` en schrijf een functie `omkeren(tekst)` die een string retourneert in omgekeerde volgorde.

In `test_strings.py`, schrijf een testfunctie `test_omkeren()` die de `omkeren`-functie test met verschillende strings, waaronder lege strings, palindromen en normale woorden.

**Startcode (`strings.py`):**

```python
# strings.py

def omkeren(tekst):
    # Jouw code hier
    pass
```

---

#### Oefening 2: Is het een Palindroom?

**Opdracht:**

In `strings.py`, schrijf je nu een functie `is_palindroom(tekst)` die `True` retourneert als de `tekst` een palindroom is (een woord dat hetzelfde leest van voor naar achter), en `False` anders.

Schrijf in `test_strings.py` een testfunctie `test_is_palindroom()` die deze functie test met verschillende woorden en zinnen. Vergeet niet om te testen met hoofdletters en spaties.

---

#### Oefening 3: Getallen Lijst Optellen

**Opdracht:**

Schrijf in `rekenmachine.py` een functie `som_lijst(getallen)` die een lijst van getallen als parameter neemt en de som van deze getallen retourneert.

Schrijf in `test_rekenmachine.py` een testfunctie `test_som_lijst()` die de `som_lijst`-functie test met verschillende lijsten, waaronder een lege lijst, een lijst met positieve getallen, en een lijst met negatieve getallen.

---

#### Oefening 4: Factorial Berekenen

**Opdracht:**

In een nieuw bestand `wiskunde.py`, schrijf een functie `factorial(n)` die de faculteit van een positief geheel getal `n` retourneert. De faculteit van `n` is het product van alle positieve gehele getallen kleiner dan of gelijk aan `n`.

Schrijf in `test_wiskunde.py` een testfunctie `test_factorial()` die de `factorial`-functie test met verschillende waarden van `n`, inclusief `n = 0` (waarbij de faculteit gedefinieerd is als 1).

**Startcode (`wiskunde.py`):**

```python
# wiskunde.py

def factorial(n):
    # Jouw code hier
    pass
```

---

#### Oefening 5: Even of Oneven

**Opdracht:**

Schrijf in `wiskunde.py` een functie `is_even(n)` die `True` retourneert als `n` een even getal is en `False` als het oneven is.

Schrijf in `test_wiskunde.py` een testfunctie `test_is_even()` die deze functie test met zowel positieve als negatieve gehele getallen en nul.


<div class="header2" markdown="1">## Basisasserties en Testuitvoering
</div>

### Het Gebruik van Asserties

Een `assert`-statement controleert of een bepaalde conditie waar is. Als de conditie niet waar is, faalt de test.

**Voorbeeld:**

```python
def test_vergelijking():
    assert 10 == 10  # Deze test slaagt
    assert 10 != 5   # Deze test slaagt ook
```

### Uitvoeren van Tests met pytest

Voer je tests uit met het commando:

```bash
pytest
```

**Nuttige opties:**

- **Meer details tonen:**

  ```bash
  pytest -v
  ```

  Dit geeft meer informatie over elke test.

- **Alle tests in een specifieke map uitvoeren:**

  ```bash
  pytest tests/
  ```

### Schrijven van Tests voor Verschillende Functies

#### **Stap 1: Nieuwe functies toevoegen**

Voeg de volgende functies toe aan `rekenmachine.py`:

```python
def aftrekken(a, b):
    return a - b

def vermenigvuldigen(a, b):
    return a * b

def delen(a, b):
    return a / b
```

#### **Stap 2: Tests schrijven voor deze functies**

In `test_rekenmachine.py` voeg je de volgende testfuncties toe:

```python
def test_aftrekken():
    assert aftrekken(5, 3) == 2
    assert aftrekken(0, 0) == 0
    assert aftrekken(-1, -1) == 0

def test_vermenigvuldigen():
    assert vermenigvuldigen(2, 3) == 6
    assert vermenigvuldigen(-1, 5) == -5
    assert vermenigvuldigen(0, 100) == 0

def test_delen():
    assert delen(10, 2) == 5
    assert delen(-9, -3) == 3
    assert delen(5, 2) == 2.5
```

**Let op:** Vergeet niet om de nieuwe functies te importeren:

```python
from rekenmachine import optellen, aftrekken, vermenigvuldigen, delen
```

#### **Stap 3: Tests uitvoeren**

Voer opnieuw `pytest` uit en controleer of alle tests slagen.

### Omgaan met Fouten

Wat gebeurt er als je probeert te delen door nul?

```python
def test_delen_door_nul():
    assert delen(10, 0) == "Onmogelijk"
```

Dit zal een fout veroorzaken. In het volgende hoofdstuk leer je hoe je uitzonderingen kunt testen.

### Oefeningen

#### Instructies voor het Uitvoeren van de Oefeningen

- **Bestanden Aanmaken:**
  - Maak voor elke oefening de benodigde Python-bestanden aan, zoals `strings.py` en `test_strings.py`, of hergebruik bestaande bestanden indien van toepassing.
- **Functies Implementeren:**
  - Schrijf de gevraagde functies in het aangegeven Python-bestand.
- **Tests Schrijven:**
  - Schrijf de bijbehorende testfuncties in het testbestand. Zorg ervoor dat testfuncties beginnen met `test_`.
- **Asserties Gebruiken:**
  - Gebruik `assert`-statements om te controleren of de functies correct werken volgens de verwachtingen.
- **Tests Uitvoeren:**
  - Voer je tests uit met `pytest` en controleer of alle tests slagen.
  - Gebruik eventueel `pytest -v` voor meer gedetailleerde output.
- **Fouten Onderzoeken:**
  - Als een test faalt, lees dan de foutmelding aandachtig om te begrijpen wat er misgaat.
  - Corrigeer je code of je tests indien nodig.

#### Tips

- **Dekking van Testcases:**
  - Zorg ervoor dat je tests verschillende situaties dekken, inclusief randgevallen zoals lege lijsten of negatieve getallen.
- **Code Leesbaarheid:**
  - Houd je code overzichtelijk en gebruik duidelijke namen voor functies en variabelen.
- **Experimenteren:**
  - Probeer bewust fouten te introduceren in je code om te zien hoe pytest reageert. Dit helpt je beter te begrijpen hoe asserties en foutmeldingen werken.

---

#### Oefening 1: Vind de Maximumwaarde

**Opdracht:**

Schrijf een functie `max_waarde(getallen)` die de grootste waarde retourneert uit een lijst van getallen.

Schrijf een testfunctie `test_max_waarde()` die controleert of de functie correct de maximumwaarde retourneert voor verschillende invoerlijsten.

**Startcode (`lijstfuncties.py`):**

```python
# lijstfuncties.py

def max_waarde(getallen):
    # Jouw code hier
    pass
```

---

#### Oefening 2: Controleer op Deelbaarheid

**Opdracht:**

Schrijf een functie `is_deelbaar(x, y)` die controleert of `x` deelbaar is door `y`. De functie retourneert `True` als dit zo is, anders `False`.

Schrijf een testfunctie `test_is_deelbaar()` die de functie test met verschillende combinaties van `x` en `y`, inclusief het geval waar `y = 0`.

**Startcode (`getalfuncties.py`):**

```python
# getalfuncties.py

def is_deelbaar(x, y):
    # Jouw code hier
    pass
```

---

#### Oefening 3: Converteer Temperatuur

**Opdracht:**

Schrijf een functie `celsius_naar_fahrenheit(celsius)` die een temperatuur in graden Celsius converteert naar graden Fahrenheit.

Schrijf een testfunctie `test_celsius_naar_fahrenheit()` die controleert of de conversie correct is voor verschillende temperaturen.

**Startcode (`conversies.py`):**

```python
# conversies.py

def celsius_naar_fahrenheit(celsius):
    # Jouw code hier
    pass
```

---

#### Oefening 4: Tel Het Aantal Woorden

**Opdracht:**

Schrijf een functie `tel_woorden(zin)` die het aantal woorden in een gegeven string `zin` retourneert.

Schrijf een testfunctie `test_tel_woorden()` die de functie test met verschillende zinnen, inclusief lege strings en strings met meerdere spaties.

**Startcode (`strings.py`):**

```python
# strings.py

def tel_woorden(zin):
    # Jouw code hier
    pass
```

---

#### Oefening 5: Filter Even Getallen

**Opdracht:**

Schrijf een functie `filter_even(getallen)` die een lijst van gehele getallen `getallen` ontvangt en een nieuwe lijst retourneert met alleen de even getallen.

Schrijf een testfunctie `test_filter_even()` die controleert of de functie correct werkt met verschillende invoerlijsten.

**Startcode (`lijstfuncties.py`):**

```python
# lijstfuncties.py

def filter_even(getallen):
    # Jouw code hier
    pass
```





<div class="header2" markdown="1">## Gebruik van Fixtures en Testdata
</div>

### Wat zijn Fixtures?

Fixtures zijn functies die vooraf testdata of objecten aanmaken die je tests nodig hebben. Ze helpen bij het voorbereiden van een testomgeving.

**Voorbeeld:**

Je hebt een databaseverbinding nodig voor meerdere tests. Een fixture kan deze verbinding tot stand brengen en beschikbaar maken voor je tests.

### Een Eenvoudige Fixture Maken

#### Stap 1: Een fixture definiëren

In `test_rekenmachine.py`:

```python
import pytest

@pytest.fixture
def getallenpaar():
    return (10, 5)
```

#### Stap 2: De fixture gebruiken in een test

```python
def test_optellen(getallenpaar):
    a, b = getallenpaar
    assert optellen(a, b) == 15
```

Hier geeft de fixture `getallenpaar` de waarden `(10, 5)` aan de testfunctie.

### Meerdere Fixtures Gebruiken

Je kunt meerdere fixtures definiëren:

```python
@pytest.fixture
def positief_getal():
    return 42

@pytest.fixture
def negatief_getal():
    return -13
```

Gebruik ze in je tests:

```python
def test_aftrekken(positief_getal, negatief_getal):
    assert aftrekken(positief_getal, negatief_getal) == 55
```

### Oefeningen

#### **Oefening 1: Woordenlijst**

**Opdracht:**

Schrijf een fixture `woordenlijst` die een lijst retourneert met enkele voorbeeldwoorden, zoals `["hallo", "wereld", "pytest"]`.

Schrijf een testfunctie `test_woordenlijst_lengte()` die controleert of de lengte van de woordenlijst correct is.

**Startcode:**

```python
# test_strings.py
import pytest

@pytest.fixture
def woordenlijst():
    # Jouw code hier
    pass

def test_woordenlijst_lengte(woordenlijst):
    pass
```

---

#### **Oefening 2: Een Persoon als Object**

**Opdracht:**

Schrijf een fixture `persoon` die een dictionary retourneert met informatie over een persoon, zoals:

```python
{
    "naam": "Jan",
    "leeftijd": 25,
    "woonplaats": "Amsterdam"
}
```

Schrijf een testfunctie `test_persoon_informatie()` die controleert of de leeftijd en woonplaats van de persoon correct zijn.

**Startcode:**

```python
# test_persoon.py
import pytest

@pytest.fixture
def persoon():
    # Jouw code hier
    pass

def test_persoon_informatie(persoon):
    pass
```

---

#### **Oefening 3: Getallenlijst voor Berekeningen**

**Opdracht:**

Schrijf een fixture `getallenlijst` die een lijst retourneert met de getallen `[2, 4, 6, 8]`.

Schrijf twee testfuncties:
1. `test_som_getallenlijst()` controleert of de som van de lijst correct is.
2. `test_max_getallenlijst()` controleert of het maximale getal in de lijst correct is.

**Startcode:**

```python
# test_getallen.py
import pytest

@pytest.fixture
def getallenlijst():
    # Jouw code hier
    pass

def test_som_getallenlijst(getallenlijst):
    pass

def test_max_getallenlijst(getallenlijst):
    pass
```



<div class="header2" markdown="1">## Testen van Uitzonderingen en Foutafhandeling
</div>

### Het Belang van Uitzonderingstesten

Soms moet je code testen die een fout moet genereren, bijvoorbeeld wanneer ongeldige input wordt gegeven. Het is belangrijk om te controleren of je code correct reageert op dergelijke situaties.

### Gebruik van `pytest.raises`

#### Voorbeeld: Delen door nul

In `rekenmachine.py` pas je de `delen`-functie aan:

```python
def delen(a, b):
    if b == 0:
        raise ZeroDivisionError("Kan niet delen door nul.")
    return a / b
```

#### Schrijven van de test

In `test_rekenmachine.py`:

```python
def test_delen_door_nul():
    with pytest.raises(ZeroDivisionError):
        delen(10, 0)
```

**Uitleg:**

- De test zal slagen als `delen(10, 0)` een `ZeroDivisionError` opwerpt.
- Als er geen uitzondering wordt opgeworpen, faalt de test.

### Testen van Specifieke Foutberichten

Je kunt ook controleren op het exacte foutbericht:

```python
def test_delen_door_nul():
    with pytest.raises(ZeroDivisionError) as excinfo:
        delen(10, 0)
    assert "Kan niet delen door nul" in str(excinfo.value)
```

### Andere Uitzonderingen Testen

Als je bijvoorbeeld een functie hebt die een `ValueError` moet opwerpen bij ongeldige input:

```python
def wortel(x):
    if x < 0:
        raise ValueError("Negatief getal.")
    return x ** 0.5
```

Test:

```python
def test_wortel_negatief():
    with pytest.raises(ValueError):
        wortel(-4)
```

### **Oefeningen**

#### **Oefening 1: Leeftijd Validatie**

**Opdracht:**

Schrijf een functie `controleer_leeftijd(leeftijd)` die een `ValueError` opwerpt als de leeftijd negatief is, met de boodschap `"Leeftijd kan niet negatief zijn"`. Als de leeftijd 0 of hoger is, retourneert de functie `"Leeftijd is geldig"`.

Schrijf in `test_leeftijd.py` een testfunctie `test_negatieve_leeftijd()` die controleert of de juiste uitzondering wordt opgeworpen voor negatieve leeftijden, inclusief het foutbericht.

**Startcode (`leeftijd.py`):**

```python
# leeftijd.py

def controleer_leeftijd(leeftijd):
    # Jouw code hier
    pass
```

**Startcode (`test_leeftijd.py`):**

```python
# test_leeftijd.py
import pytest
from leeftijd import controleer_leeftijd

def test_negatieve_leeftijd():
    pass
```

---

#### **Oefening 2: Deling Met Een Foutbericht**

**Opdracht:**

Schrijf een functie `veilige_deling(a, b)` die een `ZeroDivisionError` opwerpt als `b` nul is, met de foutmelding `"Deling door nul is niet toegestaan"`. Als `b` niet nul is, retourneert de functie de waarde van `a / b`.

Schrijf in `test_deling.py` een testfunctie `test_deling_door_nul()` die controleert of de juiste uitzondering en foutmelding worden gegenereerd.

**Startcode (`deling.py`):**

```python
# deling.py

def veilige_deling(a, b):
    # Jouw code hier
    pass
```

**Startcode (`test_deling.py`):**

```python
# test_deling.py
import pytest
from deling import veilige_deling

def test_deling_door_nul():
    pass
```

---

#### **Oefening 3: Geldige Emailadressen**

**Opdracht:**

Schrijf een functie `valideer_email(email)` die een `ValueError` opwerpt als de string `email` geen `"@"` bevat, met de foutmelding `"Ongeldig emailadres"`. Als het emailadres wel geldig is, retourneert de functie `"Email is geldig"`.

Schrijf in `test_email.py` testfuncties die het volgende controleren:

1. `test_ongeldige_email()` controleert of de juiste uitzondering en foutmelding worden gegenereerd voor een ongeldig emailadres zoals `"gebruikergmail.com"`.
2. `test_geldige_email()` controleert of de functie correct werkt voor een geldig emailadres zoals `"gebruiker@gmail.com"`.

**Startcode (`email.py`):**

```python
# email.py

def valideer_email(email):
    # Jouw code hier
    pass
```

**Startcode (`test_email.py`):**

```python
# test_email.py
import pytest
from email import valideer_email

def test_ongeldige_email():
    pass

def test_geldige_email():
    pass
```


<div class="header2" markdown="1">## Best Practices en Toepassing in een Project
</div>

### Best Practices

- **Duidelijke en beschrijvende testnamen:**

  Gebruik namen die aangeven wat er wordt getest, bijvoorbeeld `test_optellen_met_positieve_getallen`.

- **Eén assert per test (indien mogelijk):**

  Dit maakt het gemakkelijker om te zien welke specifieke check faalt.

- **Tests onafhankelijk houden:**

  Tests moeten onafhankelijk van elkaar kunnen draaien zonder in een specifieke volgorde.

- **Regelmatig tests uitvoeren:**

  Voer je tests vaak uit tijdens het coderen om problemen vroeg te detecteren.

Hier is een alternatieve opdracht die aansluit bij het hoofdstuk over sorteeralgoritmen, waarbij de nadruk ligt op de toepassing van algoritmen, unit tests, fixtures, en foutafhandeling:

---

### **Mini-Project: Een Eenvoudige Bestandsbeheerder**

**Stap 1: Projectstructuur**  
Maak een map voor je project met de volgende structuur:  

```plaintext
bestandsbeheer_project/
├── bestandsbeheer.py
├── test_bestandsbeheer.py
```

---

**Stap 2: Functionaliteiten Implementeren**  
In `bestandsbeheer.py` implementeer je de volgende functies:  

1. **Bestanden sorteren op grootte**  
   ```python
   def sorteer_op_grootte(bestanden: list[tuple[str, int]]) -> list[tuple[str, int]]:
       """Sorteert een lijst van (bestandsnaam, grootte) op grootte."""
   ```

2. **Bestanden filteren op extensie**  
   ```python
   def filter_op_extensie(bestanden: list[str], extensie: str) -> list[str]:
       """Filtert bestanden die eindigen op een bepaalde extensie."""
   ```

3. **Bestanden splitsen op grootte (groter of kleiner dan een drempelwaarde)**  
   ```python
   def splits_op_grootte(bestanden: list[tuple[str, int]], drempel: int) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
       """Splitst bestanden in twee groepen op basis van grootte."""
   ```

4. **Een samenvatting genereren**  
   ```python
   def genereer_samenvatting(bestanden: list[tuple[str, int]]) -> dict:
       """Geeft een samenvatting met totaal aantal bestanden, gemiddelde grootte, grootste en kleinste bestand."""
   ```

**Zorg voor foutafhandeling waar nodig, bijvoorbeeld:**  
- Controleer of inputs geldig zijn (bijv. correcte types of niet-leeg).  
- Geef een foutmelding als een bestandsgrootte negatief is.

---

**Stap 3: Tests Schrijven**  
In `test_bestandsbeheer.py` schrijf je tests voor alle functies, inclusief:  

1. **Normale gevallen**  
   - Een lijst van bestanden met verschillende groottes en extensies.  
   - Test op correcte sortering, filtering, splitsing en samenvatting.  

2. **Randgevallen**  
   - Lege lijsten.  
   - Bestanden zonder extensie.  
   - Bestanden met gelijke groottes.  

3. **Uitzonderingen**  
   - Negatieve bestandsgroottes.  
   - Verkeerde types (bijv. een string in plaats van een lijst).  

**Gebruik fixtures en parameterisatie:**  
- Maak gebruik van een fixture om voorbeeldgegevens aan te maken (bijv. lijsten van bestanden).  
- Parameteriseer tests met verschillende invoercombinaties.  

---

**Uitbreiding (optioneel):**  
Als er tijd is, kun je een extra functie implementeren om bestanden te sorteren op meerdere criteria (bijvoorbeeld eerst op extensie, dan op grootte).



<div class="header2" markdown="1">## Veelgestelde Vragen
</div>

**1. Waarom zou ik tijd besteden aan het schrijven van tests?**

Tests helpen je om fouten vroegtijdig te vinden, wat tijd en moeite bespaart op de lange termijn. Ze zorgen ook voor betrouwbare en onderhoudbare code.

**2. Is pytest het enige testframework voor Python?**

Nee, er zijn ook andere frameworks zoals `unittest` (standaard in Python) en `nose`. Echter, pytest is populair vanwege zijn eenvoud en flexibiliteit.

**3. Wat als ik een test niet begrijp of vastloop?**

Probeer de foutmelding te lezen en te begrijpen wat er misgaat. Je kunt ook online zoeken naar oplossingen of vragen stellen op forums zoals Stack Overflow.

### Unit Tests met Classes

Naast het testen van losse functies, kun je ook unit tests schrijven voor classes en hun methoden. Hier is een voorbeeld van hoe je dit kunt doen.

#### Stap 1: Een eenvoudige class schrijven

Maak een nieuw Python-bestand genaamd `bankrekening.py` en voeg de volgende code toe:

```python
# bankrekening.py

class Bankrekening:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def storten(self, bedrag):
        if bedrag > 0:
            self.saldo += bedrag
        else:
            raise ValueError("Bedrag moet positief zijn")

    def opnemen(self, bedrag):
        if bedrag > self.saldo:
            raise ValueError("Onvoldoende saldo")
        self.saldo -= bedrag

    def get_saldo(self):
        return self.saldo
```

Deze class vertegenwoordigt een eenvoudige bankrekening met methoden om geld te storten, op te nemen en het saldo op te vragen.

#### Stap 2: Een testbestand maken

Maak een nieuw bestand genaamd `test_bankrekening.py` in dezelfde map en voeg de volgende code toe:

```python
# test_bankrekening.py

import pytest
from bankrekening import Bankrekening

@pytest.fixture
def nieuwe_rekening():
    return Bankrekening()

def test_storten(nieuwe_rekening):
    nieuwe_rekening.storten(100)
    assert nieuwe_rekening.get_saldo() == 100

def test_opnemen(nieuwe_rekening):
    nieuwe_rekening.storten(100)
    nieuwe_rekening.opnemen(50)
    assert nieuwe_rekening.get_saldo() == 50

def test_opnemen_onvoldoende_saldo(nieuwe_rekening):
    nieuwe_rekening.storten(50)
    with pytest.raises(ValueError):
        nieuwe_rekening.opnemen(100)

def test_storten_negatief_bedrag(nieuwe_rekening):
    with pytest.raises(ValueError):
        nieuwe_rekening.storten(-50)
```

**Uitleg:**

- **Fixture:** De fixture `nieuwe_rekening` maakt een nieuwe `Bankrekening`-instantie aan voor elke test.
- **Testmethoden:** Elke testmethode test een specifieke functionaliteit van de `Bankrekening`-class.
- **Uitzonderingen:** Tests controleren ook of de juiste uitzonderingen worden opgeworpen bij ongeldige operaties.

#### Stap 3: De tests uitvoeren

Open de terminal, navigeer naar de map met je bestanden en voer uit:

```bash
pytest
```

**Verwachte output:**

```bash
==================== test session starts ====================
collected 4 items

test_bankrekening.py ....                                 [100%]

===================== 4 passed in X.XXs ======================
```

Een punt `.` betekent dat de test is geslaagd.

Met deze aanpak kun je eenvoudig unit tests schrijven voor classes en hun methoden, wat helpt bij het waarborgen van de betrouwbaarheid en correctheid van je code.

### Oefeningen met Classes

#### Oefening 1: Een Simpele Rekenmachine Class

**Opdracht:**

Schrijf een class `Rekenmachine` in `rekenmachine_class.py` met de volgende methoden:

```python
# rekenmachine_class.py

class Rekenmachine:
    def optellen(self, a, b):
        return a + b

    def aftrekken(self, a, b):
        return a - b

    def vermenigvuldigen(self, a, b):
        return a * b

    def delen(self, a, b):
        if b == 0:
            raise ValueError("Kan niet delen door nul.")
        return a / b
```

Schrijf in `test_rekenmachine_class.py` testfuncties voor alle methoden van de `Rekenmachine` class. Zorg ervoor dat je ook uitzonderingen test, zoals delen door nul.

**Startcode (`test_rekenmachine_class.py`):**

```python
# test_rekenmachine_class.py
import pytest
from rekenmachine_class import Rekenmachine

@pytest.fixture
def rekenmachine():
    return Rekenmachine()

def test_optellen(rekenmachine):
    pass

def test_aftrekken(rekenmachine):
    pass

def test_vermenigvuldigen(rekenmachine):
    pass

def test_delen(rekenmachine):
    pass

def test_delen_door_nul(rekenmachine):
    pass
```

---

#### Oefening 2: Een Simpele Bankrekening Class

**Opdracht:**

Schrijf een class `Bankrekening` in `bankrekening_class.py` met de volgende methoden:

```python
# bankrekening_class.py

class Bankrekening:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def storten(self, bedrag):
        if bedrag > 0:
            self.saldo += bedrag
        else:
            raise ValueError("Bedrag moet positief zijn")

    def opnemen(self, bedrag):
        if bedrag > self.saldo:
            raise ValueError("Onvoldoende saldo")
        self.saldo -= bedrag

    def get_saldo(self):
        return self.saldo
```

Schrijf in `test_bankrekening_class.py` testfuncties voor alle methoden van de `Bankrekening` class. Zorg ervoor dat je ook uitzonderingen test, zoals het opnemen van meer geld dan beschikbaar is en het storten van een negatief bedrag.

---

#### Oefening 3: Een Simpele Product Class

**Opdracht:**

Schrijf een class `Product` in `product_class.py` met de volgende methoden:

```python
# product_class.py

class Product:
    def __init__(self, naam, prijs):
        self.naam = naam
        self.prijs = prijs

    def wijzig_prijs(self, nieuwe_prijs):
        if nieuwe_prijs < 0:
            raise ValueError("Prijs kan niet negatief zijn")
        self.prijs = nieuwe_prijs

    def get_prijs(self):
        return self.prijs
```

Schrijf in `test_product_class.py` testfuncties voor alle methoden van de `Product` class. Zorg ervoor dat je ook uitzonderingen test, zoals het instellen van een negatieve prijs.

