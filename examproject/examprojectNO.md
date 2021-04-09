# Eksamensprosjekt

- [Eksamensprosjekt](#eksamensprosjekt)
  - [Datoer](#datoer)
  - [Oversikt:](#oversikt)
  - [Rapport](#rapport)
  - [Levering](#levering)
  - [Tillat teknologi](#tillat-teknologi)
      - [Backend:](#backend)
      - [Frontend:](#frontend)
      - [Layout:](#layout)
  - [Funksjonskrav](#funksjonskrav)
    - [SPA og REST API](#spa-og-rest-api)
      - [Alternativer:](#alternativer)
    - [Login](#login)
    - [Data items](#data-items)
    - [Data visning](#data-visning)
    - [Validering](#validering)
    - [Layout/Oppsetts](#layoutoppsetts)
    - [Tilleggsfunksjoner](#tilleggsfunksjoner)
  - [Vurdering](#vurdering)
  - [Hjelp og plagiering](#hjelp-og-plagiering)

## Datoer

| Dato   |        |              |
| ------ | ------ | ------------ |
| 12.04. | start  |              |
| 23.04. | report | **deadline** |
| 04.06. | code   | **deadline** |

## Oversikt:
For eksamensprosjektet må du designe og implementere en komplett webapplikasjon, frontend og backend.

Du kan velge hvilken type applikasjon du implementerer, men begrensninger gjelder for hvilken [teknologi du kan bruke](#tillat-teknologi) og det finnes noe [nødvendig funksjonalitet](#funksjonskrav).

## Rapport
To uker etter prosjektstart, skal du levere en beskrivelse av applikasjonen du vil implementere.
Beskrivelsen skal inneholde:
1. Hva gjør applikasjonen?
2. Hvilke data er lagret i databasen (f.eks. tabellnavn)?
3. Et foreløpig design/layout for siden. Denne kan lages som statisk HTML-side, eller som et bilde (bruk    for eksempel PowerPoint).

Beskrivelsen trenger ikke å inkludere all funksjonalitet, og du kan endre spesifikk funksjonalitet, data og sideoppsett. Men det overordnede temaet for siden er bindende.

## Levering
Ved den endelige leveringen skal du levere inn den fullstendige koden og en README.md markdown fil.
Koden din skal også inneholde en SQLite-databasefil, inkludert applikasjonens database med eksempeldata.

Filen `README.md` skal inneholde følgende seksjoner:
- How to run: e.g. 
    > Start the application by running `app.py` in the application folder.
- Liste av all funksjonalitet: Liste over alle implementerte funksjoner, for å sikre at alt arbeidet ditt blir tatt i betraktning. For eksempel
    * Innstillinger lagres i en cookie og er til stede hvis brukeren besøker siden på nytt.
    * Nye kategorier kan legges til på kategorisidene.
      * Et ikon og en farge kan velges for kategorien.
    * Hvis brukeren prøver å registrere et passord med mindre enn 5 tegn, vises en feilmelding.


## Tillat teknologi
Du kan bare bruke frameworks som er oppført nedenfor. Hvis du er usikker på om noe er tillatt, kan du spørre på Discord.

#### Backend:
Du skal bruke Flask WebServer med en SQLite database.
Du kan bruke plugins som Flask-login, men det er ikke nødvendig. Hvis du gjør det, må du nevne det i README.md.

#### Frontend:
Frontend skal være enten ren JS eller Vue.
Du kan bruke plugins som Vuex eller Vue-router.
Du kan bruke Lodash JS-biblioteket.
Du kan bruke alle buildin JS APIer.
You may use all buildin JS APIs.
Du kan bruke enten Vue versjon 2 eller 3.

Det er ikke lov å bruke et annet JS Framework som, e.g. React.

#### Layout:
Du kan enten bruke vanlig CSS eller Bootstrap.
Hvis du kopierer CSS-filer fra nettet, f.eks. `reset.css` eller` normalize.css`, må du skrive det i README.md. Så vil det ikke telle som plagiering.

Merk at det er spesifikke funksjonskrav når du bruker Bootstrap.

## Funksjonskrav
Følgende funksjonelle kravene gir grunnlaget for vurdering av prosjektet.
Du kan utelate noen funksjoner, men dette vil påvirke karakteren.

### SPA og REST API
Applikasjonen skal være en Single page application (SPA) som kommuniserer med Flask serveren via AJAX kall.

Applikasjonen skal implementeres med Vue.
I tillegg bør applikasjonen omfatte flere routes, gjennom Vue-Router.

Webserveren skal sende den opprinnelige applikasjonen som statiske filer og eksponere applikasjonsdata gjennom et REST API.

For å få full poeng skal applikasjonen være ryddig og fordelt på flere componenter.

#### Alternativer:
**Ren JS:**
I stedet for å bruke Vue kan du også skrive en vanlig JS-applikasjon, lik Assignment 4/ 8.
Poengsummen din blir imidlertid redusert hvis appen din ikke bruker routing.
Du kan implementere en [router i Ren JS] (https://dev.to/aminnairi/a-router-without-a-web-server-in-vanilla-javascript-3bmg).

**Flask Templates:** 
Du kan velge å implementere applikasjonen din ved hjelp av Flask templates, isteden for Vue og AJAX kall.
Dette vil gi en betydelig reduksjon i karakter.
Men hvis du sikter mot bestått  og vil unngå kompleksiteten i Vue og AJAX-kall, kan dette være et godt valg.

### Login
Applikasjonen din skal støtte pålogging og registrering av nye brukere.
Brukere skal lagres i databasen.

### Data items
I tillegg til brukere skal databasen inneholde minst to typer dataobjekter, dvs. two tabeller.
Data skal eksponeres gjennom et REST API som gjør det mulig å spørre, oppdatere, sette inn og slette data.
Noen av disse operasjonene bør kreve spesifikk godkjenning/authentication, for eksempel har ikke alle brukere lov til å slette hvert element.


### Data visning
Frontend må inneholde funksjonelitet for å vise en gruppe (collection) av data elementer.
Det skal være mulig å ** filtrere **, ** sortere ** og ** endre visningen ** av elementene.
*Innstillinger for sortering eller visning skal lagres* slik at de er til stede når brukeren besøker siden på nytt. (Kan lagres i informasjonskapsler, cookies, eller lignende.)

### Validering
Skjemaer for pålogging, registrering, tilføying og oppdatering av dataelementer bør valideres.
Kritiske elementer, som passord og brukernavn, må valideres på server-siden.
Hvis validering mislykkes, skal en meningsfylt feilmelding vises.

### Layout/Oppsetts
Oppsettet til siden din skal være flytende/fluid, dvs. justere til forskjellige nettleservinduestørrelser.

*Bruker du kun CSS, skal oppsettet dit fungere for vindusstørrelser mellom 1800px og 800px.*

*Bruker du Bootstrap, skal oppsettet være responsivt og fungere også på mobileskjermer, f.eks. 375px.*

Oppsettet ditt skal inneholde minst et bilde, e.g bakgrunn eller banner.

### Tilleggsfunksjoner
Det forventes at du implementerer også mer komplekse funksjoner.

Eksempler på mer komplekse funksjoner kan være:
- Lagring og håndtering av bilder lastet opp av brukeren.
- Lagring og håndtering/visning av datoer.


## Vurdering
Karaketeren blir satt hovedsaglig ut ifra koden som er levert.
Men, karakteren blir også justert, basert på i hvilken grad du implementerer det som er beskrevet i rapporten.

Applikasjonen din skal være fungerende og testet ut.
All funksjonalitet skal være feilfri, inkludert JS-kode.
Hvis din applikasjon inkluderer **dysfunksjonell eller ubrukt kode** vil det trekke i karakteren.
Fjern denne koden før du leverer.

For vurdering bruker Firefox, versjon 87.
For å unngå kompatibilitetsfeil anbefales det å teste applikasjonen din i denne nettleseren.

Tabellen nedenfor gir en oversikt over karakterkriteriene.
Merk at det i alle kategorier er mulig å få poeng for ekstra eller mer kompleks funksjonalitet.

| Project report                              | 5%  |
| ------------------------------------------- | --- |
| **Project code**                        | **95%** |
| *Frontend*                                  | 45% |
| - Functional Vue application                |     |
| - Display and sorting of data               |     |
| - Storage of user preferences               |     |
| - Form validation and error display         |     |
| - Clean separation and reuse of components  |     |
| - Use of Vue Router                         |     |
| - Comments and clean code                   |     |
| *Layout*                                    | 10% |
| - Fluid layout                              |     |
| *Database*                                  | 10% |
| - Layout and access functions               |     |
| *Flask backend*                             | 30% |
| - REST API                                  |     |
| - Server side validation and error handling |     |
| - Authentication and access control         |     |
| - Comments and clean code                   |     |


## Hjelp og plagiering
Finner vi kode med betydelige likheter i to innleveringer, blir det en plagieringssak.
Vi vil sjekke dette ved hjelp av en automatisk plagiat sjekker.
Dette inkluderer imidlertid ikke kode kopiert fra eksempler i kurset.

Merk at dette ikke skal hindre dere i å hjelpe hverandre.
Så lenge du ikke skriver kode til medstudentene dine, men hjelper dem med å feilsøke eller designe
en viss funksjonalitet, regnes det ikke som plagiering.

Vi vil også fortsette å tilby hjelp i lab timene.