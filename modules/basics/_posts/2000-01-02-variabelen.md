---
title: Variabelen
---

<div class="header1" id="top" markdown = "1"># Nummers
</div>

<div class="header2" markdown = "1">## Nummers in Python
</div>

Als je een tekst wil tonen, dan kan je de print instructie gebruiken. Maar je kan met print ook nummers tonen:

```python
print(123)
```

Valt het je op dat er nu geen aanhalingstekens rond het nummer staan? Je had die kunnen toevoegen, maar dan beschouwt Python dat als een tekst waar toevallig enkel cijfers in staan.

Met echte nummers werken heeft het voordeel dat je ermee kan rekenen. Test de volgende code maar eens uit:

```python
print(12+3)
print("12"+"3")
```

Als je het plusteken gebruikt met tekst, dan plak je deze teksten aan mekaar. Dat wordt vaak gebruikt en daar bestaat een woord voor: `concatenate`. Je zal dat later nog tegenkomen.

Als je het plusteken gebruikt met nummers, dan ben je aan het rekenen. Je kan alle standaard wiskundige operatoren gebruiken: `+`, `-`, `*` en `\`.

Maar pas op! Wat gebeurt er als je de vorige getallen (12 + 3) ook nog eens vermenigvuldigt met 10? Test dit uit en controleer of het resultaat klopt.

Als je het goed deed, dan zou het resultaat 150 moeten zijn. Kwam je bij 42 uit? Dan vergat je rekening te houden met de volgorde van bewerkingen. Die blijft net zoals bij wiskunde van toepassing. Vergeet dus geen haakjes te plaatsen!

<div class="header2" markdown = "1">## Tekst en nummers combineren
</div>

```python 
print("Het antwoord is:" + 42)
```

Test de bovenstaande instructie in je python editor. Je krijgt een foutmelding:

```
TypeError: can only concatenate str (not "int") to str
```

Wat concatenate betekent weet je al. String betekent tekst en wordt hier afgekort tot str. Integer betekent (geheel) getal en wordt hier afgekort tot int. Je kan dus geen teksten en nummers aan mekaar plakken.

Wil je toch tekst en nummers combineren in een print instructie, dan doe je dat zo:

```python 
print("Het antwoord is:", 42)
```

Wil je ook nog rekenen op die plaats, dan gebruik je een komma om teksten en nummers te scheiden, en verder operatoren:

```python 
print("Het antwoord is:", 12 + 3 * 10)
```

<div class="note oefening"><p>Volg de les <a href="https://brilliant.org/courses/programming-python/introduction-105/python-data-types/?from_llp=computer-science" target="_blank">Numbers in Python</a> op Brilliant.org</p>
<p>Volg de les <a href="https://brilliant.org/courses/programming-python/introduction-105/practice/pypractice12-v0-set_one/?from_llp=computer-science" target="_blank">Practice Numbers in Python</a> op Brilliant.org</p>
</div>


<div class="header1" markdown = "1"># Variabelen
</div>

Test deze code even uit. Maar in plaats van 1 print instructie zet je er 10 onder mekaar.

```python
print("Hello Goodbye!")
```

Maar de tekst is fout! Het moet eigenlijk zijn: "Hello, goodbye!". Nu moet je de tekst 10 keer aanpassen, wat niet handig is. Als je tekst of nummers meer dan eens wil gebruiken, dan geef je ze best een label. We noemen dat een variabele.

```python
message = "Hello Goodbye!"
print(message)
```

Eens je een variabele hebt, kan je die zo vaak gebruiken als je wil. En dit geldt niet enkel voor teksten, maar ook voor getallen. Welke vorm heeft deze figuur?

```python
import math 

hoogte = 4
breedte = 2
print("Oppervlak: ", hoogte * breedte / 2)
print("Omtrek: ", hoogte + breedte + math.sqrt(hoogte * hoogte + breedte * breedte))
```

Dit kleine programma toont je het gebruik van variabelen met getallen. Daarnaast is er nog iets nieuw. Je gebruikt `import math` om toegang te krijgen tot meer wiskundige mogelijkheden. Sqrt staat voor 'Square Root', vierkantswortel dus. Het programma gebruikt de stelling van Pythagoras om de omtrek van een driehoek te berekenen. (Aangenomen dat het om een rechthoekige driehoek gaat.)

<div class="note oefening"><p>Volg de les <a href="https://brilliant.org/courses/programming-python/introduction-105/variables-and-math/?from_llp=computer-science" target="_blank">Variables in Python</a> op Brilliant.org</p>
<p>Maak de oefening <a href="https://brilliant.org/courses/programming-python/introduction-105/practice/pypractice13-v0-set_one/?from_llp=computer-science" target="_blank">Practice Variables in Python</a> op Brilliant.org</p>
<p>Start de challenge <a href="https://brilliant.org/courses/programming-python/introduction-105/conversion-challenge-2/?from_llp=computer-science" target="_blank">Conversion Challenge</a> op Brilliant.org</p>
</div>

## Oefeningen

**Oefening 1:** maak een tekst

Zet de volgende code in de python editor:

```python
number1 = 10
number2 = 5
number3 = 20
text1 = "apples"
text2 = "bananas"
text3 = "I have"
text4 = "You have"
text5 = "each."
text6 = "Together,"
text7 = "we have"
text8 = "and"
```

Laat je programma de volgende tekst genereren. Maak enkel gebruik van de gegeven variabelen.

`I have 10 apples and 5 bananas. You have 20 apples and 10 bananas. Together, we have 30 apples and 15 bananas each.`

**Oefening 2:** operatoren
Vervolledig de print instructies in de volgende code.

```python
# Given variables
a = 15
b = 7

# Perform and print the results of basic arithmetic operations
print("The sum of a and b is:")
print("The difference when b is subtracted from a is:")
print("The product of a and b is:")
print("The quotient when a is divided by b is:")
print("The remainder when a is divided by b is:")
```

**Oefening 3:** Shopping list
Toon de volledige shopping list op het scherm.

```python
# Given variables
item1 = "apples"
quantity1 = 4
item2 = "bananas"
quantity2 = 6
item3 = "oranges"
quantity3 = 3

# Print the shopping list
print("Shopping List:")
```

**Oefening 4:** Oppervlakte van een rechthoek
Vervolledig het programma
```python
# Given variables
length = 12
width = 5

# Calculate the area
area = 

# Print the result
print("The area of the rectangle is:")
```

<div class="header2" markdown = "1">## Variabelen hergebruiken en bijwerken
</div>

Tot nu toe heb je geleerd hoe je variabelen kunt maken en hun waarden kunt gebruiken. Nu gaan we een stap verder door te laten zien hoe je de waarde van een bestaande variabele kunt wijzigen.

### Waarom variabelen bijwerken?

Het bijwerken van variabelen is een essentiële vaardigheid in programmeren. Het stelt je in staat om de gegevens in je programma te veranderen en dynamisch te houden op basis van de logica en vereisten van je code. Bijvoorbeeld, je kunt tellers bijwerken, sommen berekenen en meer.

## Voorbeelden

### Voorbeeld 1: Een variabele bijwerken

Laten we beginnen met een eenvoudig voorbeeld waarin we de waarde van een variabele bijwerken:

```python
# Beginwaarde toewijzen aan de variabele
a = 10
print("De beginwaarde van a is:", a)

# De waarde van a bijwerken
a = 20
print("De nieuwe waarde van a is:", a)
```

In dit voorbeeld beginnen we met het toewijzen van de waarde `10` aan de variabele `a`. Vervolgens updaten we de waarde van `a` naar `20`.

### Voorbeeld 2: Variabelen Bijwerken met Rekenkundige Operaties

We kunnen ook variabelen bijwerken door rekenkundige operaties te gebruiken. Dit is handig voor tellers, sommen en andere berekeningen:

```python
# Beginwaarde toewijzen aan de variabele
counter = 0
print("Beginwaarde van counter:", counter)

# De waarde van counter verhogen
counter = counter + 1
print("Waarde van counter na verhoging:", counter)

# Een kortere manier om hetzelfde te doen
counter += 2
print("Waarde van counter na verhoging met 2:", counter)

# De waarde van counter verlagen
counter -= 1
print("Waarde van counter na verlaging:", counter)
```

Hier gebruiken we de operator `+=` om de waarde van `counter` met 2 te verhogen en de operator `-=` om de waarde met 1 te verlagen. Dit zijn handige snelkoppelingen om de waarde van een variabele bij te werken.

### Voorbeeld 3: Strings Bijwerken

Je kunt ook stringvariabelen bijwerken:

```python
# Beginwaarde toewijzen aan de variabele
greeting = "Hallo"
print("Beginwaarde van greeting:", greeting)

# De waarde van greeting bijwerken
greeting = greeting + " wereld"
print("Nieuwe waarde van greeting:", greeting)

# Een kortere manier om hetzelfde te doen
greeting += "!"
print("Waarde van greeting na toevoeging:", greeting)
```

In dit voorbeeld beginnen we met de string `"Hallo"` en voegen we `" wereld"` toe. Vervolgens gebruiken we de operator `+=` om een uitroepteken toe te voegen.

<div class="note oefening"><p>Volg de les <a href="https://brilliant.org/courses/programming-python/repetition/variables-and-loops/?from_llp=computer-science" target="_blank">Variable Reuse</a> op Brilliant.org</p>
<p>Maak de oefening <a href="https://brilliant.org/courses/programming-python/repetition/practice/pypractice21-v0-set_one/?from_llp=computer-science" target="_blank">Practice Variable Reuse</a> op Brilliant.org</p>
</div>

## Oefeningen

Probeer nu zelf enkele oefeningen om te oefenen met het bijwerken van variabelen.

**Oefening 1:** Update de waarde van een variabele met een nieuw getal.

```python
# Beginwaarde toewijzen
x = 5
print("Beginwaarde van x:", x)

# Update de waarde van x
# Jouw code hier
print("Nieuwe waarde van x:", x)
```

**Oefening 2:** Gebruik rekenkundige operaties om een variabele bij te werken.

```python
# Beginwaarde toewijzen
y = 10
print("Beginwaarde van y:", y)

# Verhoog de waarde van y met 3
# Jouw code hier
print("Waarde van y na verhoging:", y)

# Verlaag de waarde van y met 5
# Jouw code hier
print("Waarde van y na verlaging:", y)
```

**Oefening 3:** Werk een stringvariabele bij door er tekst aan toe te voegen.

```python
# Beginwaarde toewijzen
message = "Dit is"
print("Beginwaarde van message:", message)

# Voeg tekst toe aan message
# Jouw code hier
print("Nieuwe waarde van message:", message)
```


