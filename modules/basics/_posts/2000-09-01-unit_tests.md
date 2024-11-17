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

### Fixture Scope

Fixtures kunnen verschillende "scopes" hebben:

- **Function (standaard):** Voor elke test opnieuw aangemaakt.
- **Module:** Eén keer per module.
- **Session:** Eén keer per testsessie.

**Voorbeeld:**

```python
@pytest.fixture(scope="module")
def gedeelde_resource():
    # Code om resource aan te maken
    yield resource
    # Code om resource op te ruimen
```


<div class="header2" markdown="1">## Parameterisatie van Tests
</div>

### Waarom Parameteriseren?

Parameterisatie stelt je in staat om dezelfde test met verschillende sets data uit te voeren zonder code te dupliceren.

### Gebruik van `@pytest.mark.parametrize`

#### **Voorbeeld:**

```python
@pytest.mark.parametrize("a, b, resultaat", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_optellen(a, b, resultaat):
    assert optellen(a, b) == resultaat
```

Hier wordt de `test_optellen`-functie drie keer uitgevoerd met verschillende waarden.

### Complexere Parameterisatie

Je kunt ook meer complexe data testen:

```python
@pytest.mark.parametrize("woord, omgekeerd", [
    ("hallo", "ollah"),
    ("python", "nohtyp"),
    ("", ""),
])
def test_omkeren(woord, omgekeerd):
    assert omkeren(woord) == omgekeerd
```

**Opmerking:** Je moet de functie `omkeren` zelf implementeren voordat dit werkt.

### Parameterisatie van Fixtures

Je kunt fixtures ook parameteriseren:

```python
@pytest.fixture(params=[0, 1, -1])
def getal(request):
    return request.param

def test_is_positive(getal):
    assert (getal > 0) == is_positive(getal)
```

**Opmerking:** Ook hier moet je de functie `is_positive` zelf definiëren.

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

<div class="header2" markdown="1">## Best Practices en Toepassing in een Project

### Best Practices

- **Duidelijke en beschrijvende testnamen:**

  Gebruik namen die aangeven wat er wordt getest, bijvoorbeeld `test_optellen_met_positieve_getallen`.

- **Eén assert per test (indien mogelijk):**

  Dit maakt het gemakkelijker om te zien welke specifieke check faalt.

- **Tests onafhankelijk houden:**

  Tests moeten onafhankelijk van elkaar kunnen draaien zonder in een specifieke volgorde.

- **Regelmatig tests uitvoeren:**

  Voer je tests vaak uit tijdens het coderen om problemen vroeg te detecteren.

### Mini-Project: Een Eenvoudige Rekenmachine

#### Stap 1: Projectstructuur

Maak een map voor je project met de volgende structuur:

```
rekenmachine_project/
├── rekenmachine.py
├── test_rekenmachine.py
```

#### Stap 2: Functionaliteiten Implementeren

In `rekenmachine.py` implementeer je de functies:

- `optellen(a, b)`
- `aftrekken(a, b)`
- `vermenigvuldigen(a, b)`
- `delen(a, b)`
- `machtsverheffen(a, b)`
- `wortel(x)`

Zorg voor foutafhandeling waar nodig.

#### Stap 3: Tests Schrijven**

In `test_rekenmachine.py` schrijf je tests voor alle functies, inclusief:

- Normale gevallen
- Randgevallen (bijv. nul, negatieve getallen)
- Uitzonderingen (bijv. delen door nul)

Gebruik fixtures en parameterisatie om je tests efficiënt te maken.

#### **Stap 4: Tests Uitvoeren en Verbeteren**

Voer je tests uit met `pytest` en corrigeer eventuele fouten in je code of tests.




<div class="header2" markdown="1">## Veelgestelde Vragen
</div>

**1. Waarom zou ik tijd besteden aan het schrijven van tests?**

Tests helpen je om fouten vroegtijdig te vinden, wat tijd en moeite bespaart op de lange termijn. Ze zorgen ook voor betrouwbare en onderhoudbare code.

**2. Is pytest het enige testframework voor Python?**

Nee, er zijn ook andere frameworks zoals `unittest` (standaard in Python) en `nose`. Echter, pytest is populair vanwege zijn eenvoud en flexibiliteit.

**3. Wat als ik een test niet begrijp of vastloop?**

Probeer de foutmelding te lezen en te begrijpen wat er misgaat. Je kunt ook online zoeken naar oplossingen of vragen stellen op forums zoals Stack Overflow.
