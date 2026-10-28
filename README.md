# Shopping Cart – Python 

Shopping Cart er et Python-prosjekt som simulerer grunnleggende funksjonalitet i en nettbutikk. Programmet inneholder funksjoner for å håndtere produkter, lagerbeholdning, produktvurderinger og en handlekurv.

Prosjektet er utviklet for å øve på **funksjoner, dictionaries, løkker, betingelser og databehandling** i Python.

## Teknologier

- **Python** – Programmeringsspråket som brukes til å utvikle funksjonaliteten.
- **Dictionaries** – Brukes til å organisere produktinformasjon, lagerstatus og handlekurv.
- **Lister** – Brukes til å lagre produktvurderinger.

## Funksjonalitet

Prosjektet inneholder flere funksjoner som håndterer ulike deler av en enkel nettbutikk:

- **Produktinformasjon** – Viser produktets navn, pris, lagerbeholdning og beskrivelse.
- **Produktvurderinger** – Beregner gjennomsnittlig vurdering basert på tidligere vurderinger.
- **Lageroversikt** – Filtrerer produkter og returnerer kun varer som er på lager.
- **Lagerkontroll** – Kontrollerer om ønsket antall produkter er tilgjengelig.
- **Handlekurv** – Legger til produkter i handlekurven og oppdaterer lagerbeholdningen automatisk.
- **Begrenset lagerbeholdning** – Dersom kunden ønsker flere produkter enn det som er tilgjengelig, legges kun tilgjengelig antall til i handlekurven.
- **Prisberegning** – Beregner totalprisen for handlekurven, inkludert merverdiavgift på 25 % som standard.

## Hvordan programmet fungerer

Programmet er delt opp i separate funksjoner som har ansvar for ulike oppgaver.

`print_ware_information()` skriver ut informasjon om et produkt, inkludert navn, pris, lagerstatus og beskrivelse.

`calculate_average_ware_rating()` beregner gjennomsnittet av produktets vurderinger og runder resultatet til én desimal. Funksjonen håndterer også tilfeller der produktet ikke har noen vurderinger.

`get_all_wares_in_stock()` går gjennom produktene og oppretter en ny dictionary som kun inneholder varer med minst ett produkt på lager.

`is_number_of_ware_in_stock()` undersøker om det ønskede antallet er tilgjengelig.

`add_number_of_ware_to_shopping_cart()` legger produkter til i handlekurven og reduserer lagerbeholdningen tilsvarende. Dersom det ikke finnes nok produkter på lager, legges kun det tilgjengelige antallet til.

`calculate_shopping_cart_price()` beregner den totale prisen basert på produktenes pris og antall i handlekurven. Merverdiavgiften kan justeres gjennom en parameter.

## Hva jeg har lært

Gjennom dette prosjektet har jeg fått praktisk erfaring med flere sentrale konsepter innen Python:

- Oppdeling av kode i mindre, gjenbrukbare funksjoner.
- Bruk av dictionaries og lister for å strukturere data.
- Iterasjon gjennom dictionaries med `.items()`.
- Betingelser og logiske sammenligninger.
- Oppdatering og håndtering av lagerbeholdning.
- Beregning av gjennomsnitt og totalpriser.
- Bruk av standardparametere i funksjoner.
- Enkel feilhåndtering med `try` og `except`.

## Videreutvikling

Prosjektet inneholder grunnleggende funksjoner for en nettbutikk, men har foreløpig ikke et eget brukergrensesnitt.

Mulige forbedringer inkluderer å utvikle et grafisk brukergrensesnitt, legge til muligheten for å fjerne produkter fra handlekurven og lagre produktinformasjon i en database.

Prosjektets hovedfokus har vært å utvikle enkle og gjenbrukbare Python-funksjoner som kan brukes som grunnlag for en større nettbutikkapplikasjon.
