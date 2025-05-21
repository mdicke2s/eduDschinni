# Workshop zu KI Assistent (Sekundarstufe 1)

_Titel:_ **Dschinni aus der Wolke - wir bauen unseren eigenen KI Assistent**

_Beschreibung:_

Beschreibe in 2-3 aussagekräftigen Sätzen die möglichen Inhalte. 
Dieser Workshop richtet sich an Gruppen die bereits Programmiererfahrung haben und sich gerne kreativ mit generativer KI auseinandersetzen möchten. Ihr lernt basierend auf der ChatGPT API einen persönlichen Assistenten zu erstellen. Ob Dschinni, Reiseführer, Klassensprecher oder Vokabeltrainer - euer Assistent steht euch zu Diensten.

_Inhalt_
[Workshop](workshop.md)

# Vor der Veranstaltung
 - Laptops (mind. 1 je 2 Teilnehmer)
   - Python 3 und pip installieren
   - IDE (z.B. https://thonny.org/) oder Notepad mit Syntax Highlighting
   - Abhängigkeiten
     - https://docs.python.org/3/library/tkinter.html
     - Module - siehe requirements.txt
 - OpenAI API key erstellen 
   <!--- TODO: Braucht man mehrere Keys? Mehrere OrgIDs?
     ein durchschnittliches Gespräch (3 Wünsche) verbraucht etwa 10.000 token
   -->
   ```
   You have a $5 free trial that begins from when you first opened your OpenAI account, whether that be to use ChatGPT or to directly use API. It expires after three months - and then a bit after that at the end of the month.
   ```
 - Key auf Laptops verteilen (env variable OPENAI_API_KEY)