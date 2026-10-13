# 🍳 Personal Chef – KI-gestützter Rezeptassistent

**Personal Chef** ist ein lokaler KI-Kochassistent, der dabei hilft, leckere Rezepte aus den Zutaten zu finden, die bereits zu Hause vorhanden sind.

Das Projekt verwendet Python, LangChain und Ollama, um einen lokalen Sprachmodell-Agenten zu erstellen. Mithilfe einer Websuche über ddgs kann der Agent passende Rezepte und Kochideen im Internet recherchieren.

## ✨ Funktionen

- 🥕 **Zutatenbasierte Rezeptsuche:** Rezeptideen auf Basis vorhandener Zutaten.
- 🔎 **Websuche:** Recherche nach passenden Rezepten mit ddgs.
- 🤖 **Lokales Sprachmodell:** Verarbeitung mit Ollama, ohne OpenAI API.
- 📝 **Rezeptanleitungen:** Zutatenlisten und Schritt-für-Schritt-Anleitungen auf Anfrage.
- 💻 **Lokale Ausführung:** Das Sprachmodell läuft auf dem eigenen Computer.

## 🛠️ Verwendete Technologien

- **Python** – Programmiersprache
- **LangChain** – Erstellung und Verwaltung des KI-Agenten
- **Ollama** – Lokale Ausführung des Sprachmodells
- **Qwen 2.5 (0.5B)** – Kleines Sprachmodell für ressourcenärmere Computer
- **python-dotenv** – Verwaltung von Umgebungsvariablen

## 📋 Voraussetzungen

- Python 3.10 oder neuer
- Installiertes [Ollama](https://ollama.com/)
- Eine Internetverbindung für die Websuche
- Ausreichend freier Arbeitsspeicher für das ausgewählte Sprachmodell

## 🚀 Installation

### 1. Repository klonen

```bash
git clone <REPOSITORY-URL>
cd personalchef
```

https://github.com/zramcode/personal_chef

### 2. Virtuelle Umgebung erstellen

```bash
python3 -m venv venv
source venv/bin/activate
```

Unter Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Abhängigkeiten installieren

```bash
pip install -U langchain langchain-ollama ddgs python-dotenv
```

### 4. Ollama installieren und Modell herunterladen

Installiere Ollama über (https://ollama.com/).

Lade anschließend das kleine Sprachmodell herunter:

```bash
ollama pull qwen2.5:0.5b
```

Teste das Modell:

```bash
ollama run qwen2.5:0.5b
```

### 5. Anwendung starten

```bash
python source/personal_chef.py
```

## 🍽️ Beispiel

**Eingabe:**

```text
I have eggs, potatoes, onions and cheese.
What can I cook?
```

**Mögliche Antwort:**

```text
Here are three recipe ideas:

1. Cheesy Potato Omelette
2. Potato and Onion Hash with Eggs
3. Baked Potatoes with Cheese

Each recipe uses ingredients you already have.
Additional ingredients may be required.
```

Die tatsächlichen Ergebnisse hängen vom verwendeten Sprachmodell und den verfügbaren Suchergebnissen ab.

## 🔐 Datenschutz und Kosten

- Es wird keine OpenAI API benötigt.
- Das Sprachmodell wird lokal über Ollama ausgeführt.
- Für die Websuche ist eine Internetverbindung erforderlich.
- Suchanfragen werden an den verwendeten Suchdienst übermittelt.
- Die lokale Modellausführung ist nicht mit API-Nutzungsgebühren verbunden; Stromverbrauch und Hardware-Ressourcen fallen weiterhin an.

## ⚠️ Einschränkungen

- Kleine Sprachmodelle können ungenaue Antworten liefern oder Tool-Aufrufe nicht zuverlässig ausführen.
- Die Qualität der Rezeptvorschläge hängt von den Suchergebnissen ab.
- Die Geschwindigkeit ist von der verfügbaren Hardware abhängig.
- Die Websuche kann durch Netzwerkprobleme oder Einschränkungen des Suchdienstes beeinträchtigt werden.

## 🔮 Zukünftige Verbesserungen

- Unterstützung weiterer lokaler Sprachmodelle
- Filter für vegetarische und vegane Rezepte
- Berücksichtigung von Allergien und Ernährungspräferenzen
- Anzeige von Zubereitungszeit und Schwierigkeitsgrad
- Benutzerfreundliche grafische Oberfläche

**Personal Chef – Weniger Lebensmittel verschwenden, mehr aus vorhandenen Zutaten machen!** 🥗

