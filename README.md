# ✨ ~~Nett~~butikk (Python)

Dette prosjektet er en enkel butikk laget i Python. Du kan kjøpe og selge varer, og lommeboka oppdateres etter hver handel.

I dette prosjektet skal du også lære å teste funksjoner uten å måtte kjøre hele programmet og teste manuelt i terminalen. Ved å importere funksjoner fra andre Python-filer kan du teste dem direkte og kontrollere at de gir forventede resultater ved hjelp av `assert`.

## 🚀 Installasjon

Kjør følgende kommandoer:

```bash
uv sync
uv venv
```

## ▶️ Kjør programmet

```bash
uv run python src/main.py
```

Programmet gir selv instrukser i terminalen for hvordan det brukes.

## 🧪 Testing

I `test_store.py` finner du et eksempel på hvordan du kan importere og teste funksjonene i `store.py` uten å kjøre `main.py`.

Vi bruker `assert` for å kontrollere at funksjonene returnerer forventede verdier.

Kjør testen med:

```bash
uv run python src/test_store.py
```

## 🧪 Oppgaver

Test funksjonene i `store.py` ved å prøve ulike verdier og situasjoner.

- Lag hypoteser om hva du tror skjer når du bruker ulike verdier.
- Bruk `assert` for å teste om hypotesene stemmer.
- Test både vanlige verdier og uvanlige situasjoner, for eksempel null, negative tall eller manglende informasjon.
- Undersøk hvordan funksjonene reagerer på ugyldige verdier, og gjør nødvendige endringer i koden.

### 💪 Vanskelig utfordring

Utvid funksjonaliteten i nettbutikken ved å undersøke problemstillinger som krever større endringer i koden. Du kan for eksempel:

- Tillate desimaltall som priser (Vanskeligere enn du tror, med en løsning som er enklere enn det ser ut til).
- Kjøpe eller selge flere varer samtidig.
- Beregne totalprisen for flere varer.
- Håndtere rabatter eller andre regler for kjøp og salg.

Skriv tester med `assert` som kontrollerer at den nye funksjonaliteten fungerer som forventet.

## 📁 Viktige filer i repoet

- `src/main.py` – starter nettbutikken.
- `src/store.py` – inneholder funksjonene for kjøp og salg.
- `src/test_store.py` – tester funksjonene uten å kjøre hovedprogrammet.
- `.gitignore` – hindrer at uønskede filer legges til i Git.
- `.gitattributes` – sørger for konsistent håndtering av filer på tvers av operativsystemer.