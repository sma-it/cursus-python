---
title: Tekstbestanden
---

<div class="header1" id="top" markdown = "1"># Tekstbestanden
</div>

<div class="header2" markdown = "1">## Bestanden lezen
</div>

### Bestanden openen en sluiten

Om een tekstbestand te lezen, gebruik je de functie `open()`, gevolgd door de modus waarin je het bestand wilt openen. De meestgebruikte modus voor het lezen van bestanden is de **leesmodus** (`"r"`). 

#### Syntax:
```python
bestand = open("bestandsnaam.txt", "r")
```

Hiermee wordt het bestand `bestandsnaam.txt` geopend in de leesmodus. Na het openen moet je altijd het bestand sluiten zodra je klaar bent, om te voorkomen dat er geheugen wordt vastgehouden.

#### Bestand sluiten:
```python
bestand.close()
```

### Gebruik van `with` voor veilige bestandstoegang

Een veilige en aanbevolen manier om met bestanden te werken, is door gebruik te maken van het **`with`** statement. Dit zorgt ervoor dat het bestand automatisch wordt gesloten zodra de indented code is uitgevoerd, zelfs als er een fout optreedt.

#### Voorbeeld:
```python
with open("bestandsnaam.txt", "r") as bestand:
    inhoud = bestand.read()
    print(inhoud)
```

Hier hoef je het bestand niet expliciet te sluiten, want Python sluit het automatisch zodra de code binnen het `with`-blok klaar is.

---

### Leesmethoden in detail

Er zijn verschillende manieren om de inhoud van een bestand te lezen, afhankelijk van wat je nodig hebt. De belangrijkste methoden zijn:

#### `read()` – Leest de volledige inhoud van het bestand

De `read()` methode leest het hele bestand als een enkele string.

**Voorbeeld**:
```python
with open("bestandsnaam.txt", "r") as bestand:
    inhoud = bestand.read()
    print(inhoud)
```

Dit leest de volledige inhoud van het bestand in één keer. Als het bestand groot is, kan dit echter veel geheugen gebruiken.

#### `readline()` – Leest één regel per keer

De `readline()` methode leest één regel van het bestand per keer, wat handig is als je het bestand regel voor regel wilt verwerken.

**Voorbeeld**:
```python
with open("bestandsnaam.txt", "r") as bestand:
    regel = bestand.readline()
    while regel:
        print(regel, end="")
        regel = bestand.readline()
```

Elke keer dat `readline()` wordt aangeroepen, wordt de volgende regel van het bestand gelezen. Dit gaat door tot het einde van het bestand is bereikt.

#### `readlines()` – Leest alle regels en slaat ze op in een lijst

De `readlines()` methode leest alle regels van het bestand en retourneert deze als een lijst van strings, waarbij elke regel een element in de lijst is.

**Voorbeeld**:
```python
with open("bestandsnaam.txt", "r") as bestand:
    regels = bestand.readlines()
    for regel in regels:
        print(regel, end="")
```

Dit leest alle regels van het bestand en je kunt door de lijst van regels itereren om elke regel afzonderlijk te verwerken.

---

### Omgaan met bestandslocaties en paden

Als je met bestanden werkt, moet je soms bestanden openen die zich in een andere directory bevinden dan waar je script wordt uitgevoerd. In dat geval kun je een **absoluut pad** of een **relatief pad** opgeven.

- **Relatief pad**: Je specificeert het pad ten opzichte van de directory waarin je script wordt uitgevoerd.
  
  **Voorbeeld**:
  ```python
  with open("submap/bestandsnaam.txt", "r") as bestand:
      inhoud = bestand.read()
  ```

- **Absoluut pad**: Je specificeert het volledige pad van de locatie van het bestand op het systeem.

  **Voorbeeld**:
  ```python
  with open("/volledig/pad/naar/bestandsnaam.txt", "r") as bestand:
      inhoud = bestand.read()
  ```

Bij het werken met paden in Python, vooral op verschillende besturingssystemen, is het handig om de module `os` te gebruiken voor bestandslocaties. Je kunt bijvoorbeeld `os.path.join()` gebruiken om paden op een platformonafhankelijke manier samen te voegen.

**Voorbeeld met `os.path.join()`**:
```python
import os

bestandspad = os.path.join("submap", "bestandsnaam.txt")
with open(bestandspad, "r") as bestand:
    inhoud = bestand.read()
    print(inhoud)
```

<div class="header2" markdown = "1">## Oefeningen
</div>

Kopieer de volgende grap en sla deze op als een bestand **jokes.txt** in dezelfde map waar je je Python-scripts schrijft.

---

```
How many programmers does it take to change a light bulb? None – It’s a hardware problem
Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25.
Programming is like sex. One mistake and you have to support it for the rest of your life.
When I wrote this code, only me and God knew how it works. Now only God knows…
Give a man a program, and frustrate him for a day. Teach a man to program, frustrate him for a lifetime.
What did Java code call a C code? You have no class.
Debugging is like being the detective in a crime movie where you’re also the murderer.
If you put a million monkeys at a million keyboards, one of them will eventually write a Java program. The rest of them will write Python programs.
```
---

### Oefening 1: Lees en druk de inhoud van het bestand af

Schrijf een Python-script dat het bestand **jokes.txt** opent en de volledige inhoud afdrukt in de console.

### Oefening 2: Tel hoe vaak elk woord voorkomt

Schrijf een Python-script dat het aantal keren telt dat elk woord in **jokes.txt** voorkomt en dit weergeeft. Houd geen rekening met hoofdletters (alle woorden moeten als kleine letters worden geteld). Tip: start met `from collections import Counter`

### Oefening 3: Tel hoe vaak elke letter voorkomt

Schrijf een Python-script dat telt hoe vaak elke letter voorkomt in **jokes.txt**. Negeer hoofdletters en beschouw alleen letters (geen spaties, cijfers of leestekens).

### Oefening 4: Bestand manueel verplaatsen naar een submap en opnieuw openen

Verplaats het bestand **jokes.txt** nu handmatig naar een submap genaamd **data**. Deze submap bevindt zich in dezelfde map als het script.

**Instructies**:
- Verplaats het bestand handmatig naar de submap **data**.
- Schrijf een Python-script dat het bestand leest, zelfs als het zich nu in de submap bevindt.
- Gebruik `os.path.join` om het pad naar het bestand op te bouwen.
- Elke regel bevat een andere grap. Toon een willekeurige grap op het scherm.

### Oefening 5: Bestand manueel verplaatsen naar een andere map op je computer en opnieuw openen

Verplaats het bestand **jokes.txt** handmatig naar een andere map op je computer (bijvoorbeeld je bureaublad).

**Instructies**:
- Schrijf een Python-script dat het bestand leest, zelfs als het zich nu in een andere map bevindt.
- Gebruik een **absoluut pad** om het bestand te vinden.
- Tel hoe vaak het woord "programmers" voorkomt in de tekst.

<div class="header2" markdown = "1">## Bestanden Opslaan
</div>

### Bestanden openen voor schrijven

Om naar een bestand te schrijven, gebruik je de functie `open()`, net zoals bij het lezen van bestanden. Het enige verschil is de **modus** waarin je het bestand opent. Voor schrijven gebruik je de volgende veelvoorkomende modi:

- `"w"`: Schrijft naar een bestand en **overschrijft** de bestaande inhoud als het bestand al bestaat. Als het bestand niet bestaat, wordt het nieuw aangemaakt.
- `"a"`: **Append**-modus. Voegt nieuwe inhoud toe aan het einde van het bestand zonder de bestaande inhoud te overschrijven. Als het bestand niet bestaat, wordt het nieuw aangemaakt.

#### Syntax:
```python
bestand = open("bestandsnaam.txt", "w")  # Schrijfmodus
bestand.write("Dit is een tekst die naar het bestand wordt geschreven.")
bestand.close()  # Sluit het bestand na het schrijven
```

Hiermee wordt het bestand **bestandsnaam.txt** geopend voor schrijven. Als het bestand al bestond, wordt de oude inhoud verwijderd. Als het bestand nog niet bestaat, wordt het aangemaakt.

---

### Het `with`-statement gebruiken

Net als bij het lezen van bestanden, is het een goede gewoonte om het `with`-statement te gebruiken wanneer je naar bestanden schrijft. Dit zorgt ervoor dat het bestand automatisch wordt gesloten zodra de code in het `with`-blok is uitgevoerd, zelfs als er een fout optreedt.

#### Voorbeeld:
```python
with open("bestandsnaam.txt", "w") as bestand:
    bestand.write("Dit is een tekst die naar het bestand wordt geschreven.")
```

In dit voorbeeld hoef je het bestand niet expliciet te sluiten omdat Python dat automatisch doet wanneer het `with`-statement wordt verlaten.

---

### Tekst schrijven naar een bestand

Je kunt de **`write()`**-methode gebruiken om tekst naar een bestand te schrijven. Let op dat `write()` alleen strings accepteert. Als je andere gegevens wilt schrijven, zoals getallen, moet je deze eerst omzetten naar een string met **`str()`**.

#### Voorbeeld:
```python
with open("resultaat.txt", "w") as bestand:
    bestand.write("Het resultaat van mijn programma is: ")
    bestand.write(str(42))  # Schrijf een getal naar het bestand
```

Dit schrijft de tekst en het getal 42 naar het bestand **resultaat.txt**.

---

### Meerdere regels naar een bestand schrijven

Als je meerdere regels tekst naar een bestand wilt schrijven, kun je de **`write()`**-methode meerdere keren aanroepen of een string met **regelteruglooptekens** (`\n`) gebruiken om nieuwe regels toe te voegen. Een handigere manier is om de **`writelines()`**-methode te gebruiken, waarmee je een lijst van strings kunt doorgeven die elk als een nieuwe regel in het bestand worden geschreven.

#### Voorbeeld met `write()`:
```python
with open("gegevens.txt", "w") as bestand:
    bestand.write("Naam: Alice\n")
    bestand.write("Leeftijd: 30\n")
    bestand.write("Land: Nederland\n")
```

#### Voorbeeld met `writelines()`:
```python
gegevens = ["Naam: Alice\n", "Leeftijd: 30\n", "Land: Nederland\n"]

with open("gegevens.txt", "w") as bestand:
    bestand.writelines(gegevens)
```

In beide voorbeelden worden de gegevens "Naam", "Leeftijd" en "Land" op afzonderlijke regels naar het bestand **gegevens.txt** geschreven.

---

### Tekst toevoegen aan een bestand

Als je niet de bestaande inhoud van een bestand wilt overschrijven, maar nieuwe tekst aan het einde van het bestand wilt toevoegen, gebruik je de **append-modus** (`"a"`). Dit zorgt ervoor dat nieuwe inhoud wordt toegevoegd zonder de bestaande inhoud te verwijderen.

#### Voorbeeld:
```python
with open("logboek.txt", "a") as bestand:
    bestand.write("Nieuwe logregel: Het programma is succesvol uitgevoerd.\n")
```

In dit voorbeeld wordt de nieuwe tekstregel toegevoegd aan het einde van het bestand **logboek.txt**. Als het bestand nog niet bestaat, wordt het aangemaakt.

---

### Werken met variabelen en gegevens in bestanden

Vaak wil je gegevens uit je programma naar een bestand schrijven. Dit kunnen variabelen, resultaten van berekeningen of de output van functies zijn. Aangezien de **`write()`**-methode alleen strings accepteert, moet je ervoor zorgen dat niet-stringwaarden worden omgezet naar strings met **`str()`**.

#### Voorbeeld:
```python
resultaat = 100
meting = 25.6

with open("meting.txt", "w") as bestand:
    bestand.write("De laatste meting was: ")
    bestand.write(str(meting) + "\n")  # Getal omzetten naar string
    bestand.write("Het resultaat is: ")
    bestand.write(str(resultaat) + "\n")
```

In dit voorbeeld worden de waarden van de variabelen `meting` en `resultaat` naar het bestand **meting.txt** geschreven.

---

### Bestanden schrijven in verschillende mappen

Als je bestanden wilt schrijven naar een specifieke map of submap, kun je het pad naar de locatie specificeren in de `open()`-functie. Als de map nog niet bestaat, kun je deze aanmaken met de **`os.makedirs()`**-functie.

#### Voorbeeld met schrijven naar een submap:
```python
import os

# Maak de submap 'output' als deze nog niet bestaat
if not os.path.exists("output"):
    os.makedirs("output")

# Schrijf naar een bestand in de submap
with open("output/rapport.txt", "w") as bestand:
    bestand.write("Dit is het rapport van de meting.")
```

In dit voorbeeld wordt de map **output** aangemaakt (als deze nog niet bestaat), en wordt het bestand **rapport.txt** in deze submap geschreven.

---

### Belangrijke tips bij het schrijven naar bestanden

- **Bestandssluiting**: Zorg er altijd voor dat bestanden worden gesloten nadat je ermee hebt gewerkt. Het gebruik van het `with`-statement is een veilige manier om dit te doen.
- **Beveiliging en rechten**: Controleer altijd de bestandsrechten van de map waarin je schrijft. Zorg ervoor dat je schrijfrechten hebt.
- **Opslaglocaties**: Denk goed na over waar je bestanden opslaat. Gebruik bijvoorbeeld specifieke mappen zoals `output` of `logfiles` om bestanden overzichtelijk te houden.
- **Omgaan met fouten**: Wees voorbereid op situaties waarin bestanden niet kunnen worden geopend of geschreven, bijvoorbeeld als je geen schrijfrechten hebt of de schijf vol is.

<div class="header2" markdown = "1">## Oefeningen
</div>


### Oefening 1: Schrijf een bericht naar een bestand

Schrijf een Python-script dat de gebruiker vraagt om een bericht in te voeren en dit bericht naar een tekstbestand genaamd **bericht.txt** schrijft.

**Instructies**:
- Vraag de gebruiker om een bericht in te voeren.
- Schrijf het bericht naar een bestand **bericht.txt**.
- Zorg ervoor dat het bestand automatisch wordt gesloten na het schrijven.

---

### Oefening 2: Logboek bijwerken

Schrijf een Python-script dat de gebruiker vraagt om een logbericht in te voeren en dit bericht aan het einde van een bestaand bestand **logboek.txt** toevoegt. Als het bestand nog niet bestaat, moet het worden aangemaakt.

**Instructies**:
- Vraag de gebruiker om een logbericht in te voeren.
- Open het bestand **logboek.txt** in de append-modus.
- Voeg het logbericht toe aan het einde van het bestand.

---

#### Oefening 3: Gegevens opslaan in een submap

Schrijf een Python-script dat een bestand **gegevens.txt** maakt in een submap genaamd **data**. In het bestand schrijf je een lijst met gegevens zoals naam, leeftijd en land, waarbij deze informatie door de gebruiker wordt ingevoerd.

**Instructies**:
- Vraag de gebruiker om hun naam, leeftijd en land in te voeren.
- Controleer of de submap **data** bestaat, en maak deze aan als dat niet het geval is.
- Schrijf de gegevens naar **gegevens.txt** in de submap **data**.

---

#### Oefening 4: Cijfers van studenten opslaan

Schrijf een Python-script dat een lijst met studentencijfers naar een bestand **cijfers.txt** schrijft. De cijfers worden handmatig ingevoerd door de gebruiker. Nadat alle cijfers zijn ingevoerd, worden ze opgeslagen in het bestand.

**Instructies**:
- Vraag de gebruiker om meerdere cijfers in te voeren.
- Schrijf de cijfers naar een bestand **cijfers.txt**, elk cijfer op een nieuwe regel.
- Druk een bericht af wanneer alle cijfers zijn opgeslagen.

---

#### Oefening 5: Logboek van activiteiten met datum en tijd

Schrijf een Python-script dat de gebruiker vraagt om hun dagelijkse activiteiten in te voeren, samen met de huidige datum en tijd. Elke activiteit wordt toegevoegd aan een logboekbestand **activiteiten_log.txt**, waarbij de datum en tijd automatisch worden toegevoegd aan elke activiteit.

**Instructies**:
- Gebruik de module `datetime` om de huidige datum en tijd op te halen.
- Vraag de gebruiker om een activiteit in te voeren.
- Voeg de activiteit samen met de datum en tijd toe aan het bestand **activiteiten_log.txt**.