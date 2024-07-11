---
title: String Functies
---

<div class="header1" id="top" markdown = "1"># String Functies
</div>

<div class="header2" markdown = "1">## Intellisense
</div>

Wanneer je in VS Code aan het programmeren bent, kun je eenvoudig de beschikbare functies van een string bekijken. Dit doe je door een punt (`.`) te typen na een string of een stringvariabele. Zodra je dit doet, verschijnt er een lijst met alle methoden die je op die string kunt toepassen. Dit maakt deel uit van *intellisense*, het deel van VS Code dat over je schouder meekijkt en je probeert te helpen.

```python
mijn_string = "Hallo, wereld!"
mijn_string.
```
<div class="note protip">
<p>Gebruik pijltjestoetsen en de `Tab`-toets om een functie uit de lijst te selecteren. Zo bespaar je weer wat toetsaanslagen.</p>
</div>

Zodra je een functie hebt geselecteerd en een haakje opent (`(`), toont VS Code de beschrijving van die functie, inclusief de parameters die de functie verwacht. Dit helpt je om snel te begrijpen hoe je de functie kunt gebruiken.

### Underscores

In Python zijn er ook functies die met dubbele underscores beginnen en eindigen, zoals `__len__()` en `__str__()`. Deze functies worden "speciale methoden" of "dunder-methoden" genoemd en worden meestal niet direct aangeroepen. Ze zijn bedoeld voor interne werking en kunnen worden gebruikt om de standaard functionaliteit van Python objecten aan te passen.

Voor strings gebruik je bijvoorbeeld de functie `len()` in plaats van de speciale methode `__len__()`:

<div class="header2" markdown = "1">## Find
</div>

De `find` functie wordt gebruikt om de index van de eerste keer dat een substring wordt gevonden binnen de string te retourneren. Als de substring niet wordt gevonden, retourneert `find` `-1`.

**Syntax**:
```python
string.find(substring, start, end)
```

- `substring`: De string die je wilt zoeken.
- `start` (optioneel): De positie waar je wilt beginnen met zoeken.
- `end` (optioneel): De positie waar je wilt stoppen met zoeken.

**Voorbeeld**:
```python
tekst = "Hallo, wereld!"
index = tekst.find("wereld")
print(index)  # Output: 7

index = tekst.find("Python")
print(index)  # Output: -1
```

In dit voorbeeld vindt `find` de substring "wereld" beginnend op index 7, en de substring "Python" wordt niet gevonden, dus retourneert de functie `-1`.

<div class="note oefening"><p>Volg de les <a href="https://brilliant.org/courses/programming-python/strings-4/slicing-2/?from_llp=computer-science" target="_blank">String Functions</a> op Brilliant.org</p>
</div>

<div class="header2" markdown = "1">## Replace
</div>

De `replace` functie wordt gebruikt om alle instanties van een substring in een string te vervangen door een andere substring.

**Syntax**:
```python
string.replace(old, new, count)
```

- `old`: De substring die je wilt vervangen.
- `new`: De substring die de oude substring vervangt.
- `count` (optioneel): Het aantal keren dat de vervanging moet plaatsvinden. Als dit niet wordt gespecificeerd, worden alle instanties vervangen.

**Voorbeeld**:
```python
tekst = "Hallo, wereld! Hallo allemaal!"
nieuwe_tekst = tekst.replace("Hallo", "Hi")
print(nieuwe_tekst)  # Output: "Hi, wereld! Hi allemaal!"

beperkte_tekst = tekst.replace("Hallo", "Hi", 1)
print(beperkte_tekst)  # Output: "Hi, wereld! Hallo allemaal!"
```

In dit voorbeeld worden alle instanties van "Hallo" vervangen door "Hi" in `nieuwe_tekst`. In `beperkte_tekst` wordt slechts één voorkom van "Hallo" vervangen.

<div class="note oefening"><p>Volg de les <a href="https://brilliant.org/courses/programming-python/strings-4/string-building-2/?from_llp=computer-science" target="_blank">The Replace Function</a> op Brilliant.org</p>
</div>

<div class="header2" markdown = "1">## Oefeningen
</div>

#### Oefening 1: Zoek naar een Woord

Je programma vraagt om een woord en kijkt of dat woord in de tekst voorkomt. Als dat zo is, dan toon je op welke positie het woord staat. In het andere geval meld je dat het woord niet gevonden werd.

**Code**:
```python
gedicht = """
In the quiet spaces of the mind,
Where thoughts drift like whispers in the wind,
Ideas take shape, then fade away,
In the ebb and flow of night and day.
"""
```

#### Oefening 2: Vervang een Woord

1. Vervang het woord "silence" door "noise".
2. Vervang het woord "forgotten" door "remembered".
3. Toon de nieuwe versie van het gedicht.

**Code**:
```python
gedicht = """
A cacophony of silence fills the air,
Echoes of forgotten dreams linger there,
In the void where memories reside,
A hidden world where truths abide.
"""
```
#### Oefening 3: Deel van een Gedicht Vervangen

1. Vervang "realm of mystery" door "kingdom of secrets".
2. Vervang "hidden world" door "secret domain".
3. Toon het nieuwe gedicht.

**Code**:
```python
gedicht = """
Beneath the surface of the sea,
Lies a realm of mystery,
With creatures strange and wonders rare,
A hidden world beyond compare.
"""
```

#### Oefening 4: Woorden Vinden en Vervangen in een Gedicht

1. Zoek naar het eerste voorkomen van het woord "Whisper" en vervang het door "Shout". Toon het nieuwe gedicht op het scherm.
2. Vervang alle voorkomens van het woord "Whisper" door "Speak". Toon het nieuwe gedicht op het scherm.
3. Vervang het woord "Whisper" door "Murmur" maar alleen de eerste 3 voorkomens. Toon het nieuwe gedicht op het scherm.

**Code**:
```python
gedicht = """
Whisper to the wind,
Whisper to the trees,
Whisper to the mountains,
Whisper to the seas.

Whisper in the morning,
Whisper late at night,
Whisper when it's dark,
Whisper in the light.
"""
```

<div class="header2" markdown = "1">## Andere functies
</div>

Hier zijn enkele andere string functies die vaak worden gebruikt in Python:

### `split` en `join`

- `split()`: Splitst een string op een opgegeven delimiter en retourneert een lijst van substrings.
  
  **Voorbeeld**:
  ```python
  tekst = "Hallo, wereld!"
  woorden = tekst.split(", ")
  print(woorden)  # Output: ['Hallo', 'wereld!']
  ```

- `join()`: Voegt een lijst van strings samen tot één string, gescheiden door een opgegeven delimiter.
  
  **Voorbeeld**:
  ```python
  woorden = ['Hallo', 'wereld!']
  tekst = ", ".join(woorden)
  print(tekst)  # Output: "Hallo, wereld!"
  ```

### `strip`, `lstrip`, `rstrip`

- `strip()`: Verwijdert witruimte aan beide kanten van de string.
- `lstrip()`: Verwijdert witruimte aan de linkerkant van de string.
- `rstrip()`: Verwijdert witruimte aan de rechterkant van de string.

**Voorbeeld**:
```python
tekst = "  Hallo, wereld!  "
print(tekst.strip())   # Output: "Hallo, wereld!"
print(tekst.lstrip())  # Output: "Hallo, wereld!  "
print(tekst.rstrip())  # Output: "  Hallo, wereld!"
```

### `lower`, `upper`, `title`, `capitalize`

- `lower()`: Converteert alle karakters in de string naar kleine letters.
- `upper()`: Converteert alle karakters in de string naar hoofdletters.
- `title()`: Converteert de eerste letter van elk woord in de string naar een hoofdletter.
- `capitalize()`: Converteert de eerste letter van de string naar een hoofdletter.

**Voorbeeld**:
```python
tekst = "hallo, wereld!"
print(tekst.lower())      # Output: "hallo, wereld!"
print(tekst.upper())      # Output: "HALLO, WERELD!"
print(tekst.title())      # Output: "Hallo, Wereld!"
print(tekst.capitalize()) # Output: "Hallo, wereld!"
```

<div class="header2" markdown = "1">## Oefeningen
</div>

#### Oefening 1: Splitsen en Samenvoegen

1. Splits de haiku in afzonderlijke woorden.
2. Voeg de woorden weer samen met een streepje (`-`) tussen elk woord.

**Code**:
```python
haiku = """
Autumn moonlight—
a worm digs silently
into the chestnut.
"""
```

#### Oefening 2: Verwijderen van Witruimte

1. Verwijder witruimte aan beide zijden van de haiku.
2. Verwijder witruimte aan de linkerzijde van de haiku.
3. Verwijder witruimte aan de rechterzijde van de haiku.

**Code**:
```python
haiku = """
   An old silent pond...
A frog jumps into the pond,
splash! Silence again.
   """
```

#### Oefening 3: Tekst naar Hoofdletters of Kleine Letters Converteren

1. Converteer de haiku naar hoofdletters.
2. Converteer de haiku naar kleine letters.
3. Converteer de haiku naar titelgeval.
4. Converteer de eerste letter van de haiku naar een hoofdletter.

Toon alle conversies op het scherm.

**Code**:
```python
haiku = """
In the cicada's cry
No sign can foretell
How soon it must die.
"""
```

#### Oefening 4: Controle op Cijfers, Letters en Alfanumerieke Tekens

1. Controleer of de haiku alleen cijfers bevat.
2. Controleer of de haiku alleen letters bevat.
3. Controleer of de haiku alleen alfanumerieke tekens bevat.
4. Gebruik maximaal 3 regels code oom te tekst aan te passen, zodat de tweede en derde controle True geven.

**Code**:
```python
haiku = """
Over the wintry
forest, winds howl in rage
with no leaves to blow.
"""
```

#### Oefening 5: Tellen

1. Tel het aantal keren dat het woord "time" voorkomt in de haiku.
2. Tel het aantal keren dat het teken "o" voorkomt in de haiku.

**Code**:
```python
haiku = """
From time to time
The clouds give rest
To the moon-beholders.
"""
```