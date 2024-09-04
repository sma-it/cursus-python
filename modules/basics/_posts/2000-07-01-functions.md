---
title: Functies
---

<div class="header1" id="top" markdown = "1"># Functies
</div>



Functies zijn een fundamenteel concept in Python en in veel andere programmeertalen. Ze maken het mogelijk om code op te splitsen in herbruikbare blokken, wat je programma overzichtelijker en onderhoudbaarder maakt. In dit hoofdstuk leer je hoe je functies kunt schrijven en gebruiken in Python, stap voor stap.

Een functie is een blok code dat alleen wordt uitgevoerd wanneer het wordt aangeroepen. Functies helpen om code te organiseren en te vermijden dat je dezelfde code meerdere keren moet schrijven. In Python definieer je een functie met het sleutelwoord `def`, gevolgd door de naam van de functie en een set haakjes `()`.

<div class="header2" markdown = "1">## Functies schrijven
</div>

### Eenvoudige functies

De meest functies voeren een specifieke taak uit, maar doen altijd hetzelfde.

**Voorbeeld**:

```python
def begroeting():
    print("Hallo, welkom bij dit programma!")

# Aanroepen van de functie
begroeting()
```

**Uitleg**:
- **Definitie van de functie**: De functie `begroeting()` wordt gedefinieerd met `def`, gevolgd door de naam `begroeting` en een paar lege haakjes `()`.
- **Functie-inhoud**: De code die binnen de functie wordt uitgevoerd (in dit geval `print("Hallo, welkom bij dit programma!")`) wordt ingesprongen onder de definitie.
- **Aanroepen van de functie**: De functie wordt uitgevoerd door haar naam te typen gevolgd door `()`.

### Functies met Resultaat

Soms wil je dat een functie een waarde teruggeeft nadat ze haar taak heeft uitgevoerd. Dit doe je met het sleutelwoord `return`. De waarde die je wilt teruggeven, wordt aangegeven na `return`.

**Voorbeeld**:

```python
def verkrijg_begroeting():
    return "Hallo, welkom bij dit programma!"

# Aanroepen van de functie en het resultaat opslaan
bericht = verkrijg_begroeting()
print(bericht)
```

**Uitleg**:
- **Definitie van de functie**: De functie `verkrijg_begroeting()` wordt gedefinieerd. In plaats van direct iets af te drukken, geeft deze functie een waarde terug met `return`.
- **Return-waarde**: Wanneer de functie wordt aangeroepen, retourneert deze de string `"Hallo, welkom bij dit programma!"`.
- **Resultaat opslaan**: Het resultaat van de functie wordt opgeslagen in de variabele `bericht`, die vervolgens kan worden gebruikt, zoals bij het afdrukken in dit voorbeeld.

### Functies met Argumenten en Resultaat

Functies worden krachtiger en flexibeler wanneer ze argumenten accepteren. Argumenten zijn waarden die je aan de functie doorgeeft wanneer je deze aanroept. De functie kan deze waarden gebruiken om haar taak uit te voeren en kan vervolgens een resultaat teruggeven.

**Voorbeeld**:

```python
def vermenigvuldig(getal1, getal2):
    resultaat = getal1 * getal2
    return resultaat

# Aanroepen van de functie met argumenten en het resultaat opslaan
uitkomst = vermenigvuldig(5, 3)
print(uitkomst)
```

**Uitleg**:
- **Definitie van de functie met argumenten**: De functie `vermenigvuldig(getal1, getal2)` wordt gedefinieerd met twee parameters: `getal1` en `getal2`. Deze parameters fungeren als plaatsvervangers voor de waarden die je bij het aanroepen van de functie doorgeeft.
- **Berekening en return**: De functie vermenigvuldigt de twee argumenten (`getal1` en `getal2`) en geeft het resultaat terug met `return`.
- **Aanroepen van de functie met argumenten**: Wanneer je `vermenigvuldig(5, 3)` aanroept, worden de waarden `5` en `3` doorgegeven aan de parameters `getal1` en `getal2`, en de functie retourneert het product van deze twee getallen, dat vervolgens wordt opgeslagen in de variabele `uitkomst`.

Python zelf bevat ook functies, zoals `print`. Nu je zelf functies kan toevoegen, kan je python dus uitbreiden met de dingen die je nodig hebt in jou programma.

Je kan trouwens ook functies in functies zetten. Het laatste voorbeeld zou je dus ook zo kunnen schrijven:

```python
print(vermenigvuldig(5, 3))
```

<div class="header2" markdown = "1">## Oefeningen
</div>

### Oefening 1: Begroeting zonder Argumenten of Resultaat

Schrijf een functie `begroet()` die de tekst "Goedendag!" afdrukt. Roep de functie daarna drie keer aan.

**Verwachte Output**:
```
Goedendag!
Goedendag!
Goedendag!
```


### Oefening 2: Getal Verdubbelen met Resultaat

Schrijf een functie `verdubbel()` die een getal verdubbelt en het resultaat teruggeeft. Roep de functie aan met het getal 8 en druk het resultaat af.

**Verwachte Output**:
```
16
```

### Oefening 3: Persoonlijk Welkomstbericht met Argumenten

Schrijf een functie `welkom()` die een naam als argument neemt en een persoonlijk welkomstbericht afdrukt in de vorm van "Welkom, [naam]!".

**Verwachte Output** (voorbeeld):
```
Welkom, Alice!
```

### Oefening 4: Omvang van een Rechthoek Berekenen met Argumenten en Resultaat

Schrijf een functie `bereken_oppervlakte()` die de lengte en breedte van een rechthoek als argumenten neemt en de oppervlakte berekent en teruggeeft. Roep de functie aan met lengte 5 en breedte 3, en druk het resultaat af.

**Verwachte Output**:
```
15
```

### Oefening 5: Grootste van Drie Getallen Vinden

Schrijf een functie `vind_grootste()` die drie getallen als argumenten neemt en het grootste getal teruggeeft. Roep de functie aan met de getallen 4, 7 en 2, en druk het resultaat af.

**Verwachte Output**:
```
7
```


### Oefening 6: Som van Kwadraten

Schrijf een functie `som_van_kwadraten()` die een lijst van getallen als argument neemt en de som van de kwadraten van deze getallen teruggeeft. Roep de functie aan met de lijst `[1, 2, 3, 4]` en druk het resultaat af.

**Verwachte Output**:
```
30
```

### Oefening 7: Gemiddelde Berekenen met Numpy

Schrijf een functie `bereken_gemiddelde()` die een Numpy-array als argument neemt en het gemiddelde van de getallen in de array teruggeeft. Roep de functie aan met de array `np.array([10, 20, 30, 40, 50])` en druk het resultaat af.

**Verwachte Output**:
```
30.0
```

### Oefening 8: Standaardafwijking Berekenen

Schrijf een functie `standaardafwijking()` die een lijst van getallen als argument neemt en de standaardafwijking van deze getallen berekent en teruggeeft. Roep de functie aan met de lijst `[4, 8, 6, 5, 3]` en druk het resultaat af.

**Verwachte Output**:
```
1.87 (afgerond tot twee decimalen)
```

### Oefening 9: Matrix Vermenigvuldiging met Numpy

Schrijf een functie `matrix_vermenigvuldiging()` die twee Numpy-matrices als argumenten neemt en hun product teruggeeft. Roep de functie aan met de matrices `[[1, 2], [3, 4]]` en `[[5, 6], [7, 8]]`, en druk het resultaat af.

**Verwachte Output**:
```
[[19 22]
 [43 50]]
```

### Oefening 10: Factorial Berekenen

Schrijf een functie `factorial()` die een geheel getal als argument neemt en de factorial van dat getal berekent en teruggeeft. Roep de functie aan met het getal `5` en druk het resultaat af.

**Verwachte Output**:
```
120
```

### Oefening 11: Een Vierkant Tekenen

Schrijf een functie `teken_vierkant()` die een vierkant tekent met een gegeven zijde lengte. Gebruik de Turtle module om het vierkant te tekenen. Roep de functie meerdere keren aan. De eerste keer met een zijde van 100 pixels, en vervolgens maak je de zijde telkens 10 pixels kleiner. Hoe zorg je ervoor dat het centrum van alle vierkanten hetzelfde is?

### Oefening 12: Een Ster Tekenen

Schrijf een functie `teken_ster()` die een ster tekent met een gegeven aantal punten en een specifieke lengte voor de lijnen. Gebruik de Turtle module om de ster te tekenen. Roep de functie aan met 5 punten en een lijnlengte van 150.


### Oefening 13: Concentrische Cirkels Tekenen

Schrijf een functie `teken_cirkels()` die een reeks concentrische cirkels tekent. De functie moet het aantal cirkels en de toename in straal tussen opeenvolgende cirkels accepteren. Gebruik de Turtle module om de cirkels te tekenen. Roep de functie aan met 5 cirkels en een toename van 20 in straal.