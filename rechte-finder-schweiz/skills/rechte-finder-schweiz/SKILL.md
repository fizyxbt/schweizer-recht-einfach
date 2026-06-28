---
name: rechte-finder-schweiz
description: Rechte-Finder für Schweizer Recht. Use when a user asks what rights they have, which Swiss legal claim applies, which legal area is involved, or where to start with a Swiss legal problem. Routes through rights catalogue, SR raster, fundamental rights and cantonal coverage.
---

# Rechte-Finder Schweiz

## Pflichtquellen im Repo

1. `references/rechte-katalog.md` für konkrete Rechte und Ansprüche.
2. `references/sr-feinraster.md` für Rechtsgebiete und Spezialbereiche.
3. `references/grundrechte-katalog.md` für Grundrechte.
4. `references/kantonale-abdeckung.md` und `references/kantone.md` für kantonale Fragen.
5. `references/quellen.md` für Quellenregeln.

## Vorgehen

1. Dokumenttyp bestimmen: Verfügung, Vertrag, Rechnung, Strafbefehl, Entscheid, Kündigung, Verfügung einer Versicherung oder anderes.
2. Kanton, Datum, Behörde/Gegenpartei, Frist und Rechtsmittelbelehrung abfragen.
3. Im Rechte-Katalog den nächsten passenden Anspruch suchen.
4. Bei staatlichem Handeln zusätzlich Grundrechte und Verfahrensrechte prüfen.
5. Bei kantonalem Bezug die Kantonsdatei verwenden.
6. Das passende Startplugin nennen und die nächsten drei Schritte in einfacher Sprache ausgeben.

## Ausgabeformat

- Vermutlich betroffenes Recht: `<Recht oder Anspruch>`
- Quelle: `<BV/OR/ZGB/StPO/ATSG/kantonal/etc.>`
- Einstieg: `<Plugin>`
- Sofort prüfen: Kanton, Datum, Frist, Dokumenttyp
- Nächste drei Schritte: kurz und praktisch

## Sperren

- Keine definitive Fristaussage ohne Datum und Zustellung.
- Keine kantonale Aussage ohne Kanton.
- Keine Rechtsberatung als Gewissheit darstellen, wenn Quelle oder Dokument fehlt.
