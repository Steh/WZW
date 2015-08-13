# Wer zahlt was?
## Projekt Beschreibung
A Django Application to track costs in small groups, created in a few weeks for a university project.

## Umzusetzen
* Export
* Import
* Kosten erledigt
* Kosten runden auf:
  * Zwei Stellen nach dem Komma
  * Auf die nächste 5er Stelle auf/abrunden
  * Auf die nächste 10er Stelle auf/abrunden
## Kosten als Erledigt markieren
* neues Modell für Report
  * ID-Kosten
  * ID-Gruppe
  * ID-Besitzer
  * ID-Schuldner
  * [float]Betrag
  * [boolean]bezahlt

* Report
 1. Reports löschen
 2.
