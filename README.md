# Schweizer Recht Einfach

Experimentelle Plugin- und Skill-Sammlung für Schweizer Recht. Dieses Repository ist bewusst schlank, validierbar und auf Schweizer Quellenlogik zugeschnitten.

## Status

| Kennzahl | Wert |
| --- | --- |
| Plugins | 8 |
| Skills | 8 |
| Version | 0.1.0 |
| Marketplace | [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) |

## Leitprinzipien

1. Schweizer Recht zuerst nach Norm, Kanton, Instanz und Sprache einordnen.
2. Bundesrecht über Fedlex zitieren, insbesondere SR, AS und BBl.
3. Bundesgerichtliche Rechtsprechung mit BGE oder Geschäftsnummer, Datum, Abteilung und Fundstelle zitieren.
4. Kantonales Recht nur mit explizitem Kanton und offizieller Gesetzessammlung verwenden.
5. Literatur, private Datenbanken und Kommentare nur verwenden, wenn der Nutzer die Quelle bereitstellt oder der Zugriff im konkreten System nachweisbar ist.
6. Rechtsstand immer als Datum ausweisen.

## Enthaltene Start-Plugins

| Plugin | Zweck |
| --- | --- |
| [`zitierweise-schweizer-recht`](./zitierweise-schweizer-recht) | Zitierregeln für SR, AS, BBl, BGE, Urteile und kantonale Quellen. |
| [`methodik-schweizer-recht`](./methodik-schweizer-recht) | Methodik für Auslegung, Normenhierarchie, mehrsprachige Fassungen und Föderalismus. |
| [`obligationenrecht-schweiz`](./obligationenrecht-schweiz) | OR-Workflows für Vertrag, Haftung, Verzug, Kauf, Auftrag, Werkvertrag und AGB. |
| [`arbeitsrecht-schweiz`](./arbeitsrecht-schweiz) | Arbeitsvertrag, Kündigung, Sperrfristen, Arbeitszeit, Zeugnis, Lohn und Gleichstellung. |
| [`mietrecht-schweiz`](./mietrecht-schweiz) | Wohn- und Geschäftsraummiete, Mietzins, Kündigung, Erstreckung und Schlichtung. |
| [`gesellschaftsrecht-schweiz`](./gesellschaftsrecht-schweiz) | AG, GmbH, Verein, Stiftung, Handelsregister und Corporate Governance. |
| [`schuldbetreibung-konkurs-schweiz`](./schuldbetreibung-konkurs-schweiz) | SchKG-Workflows für Betreibung, Rechtsvorschlag, Rechtsöffnung, Konkurs und Sanierung. |
| [`verwaltungsverfahren-schweiz`](./verwaltungsverfahren-schweiz) | VwVG/BGG-Methodik, Verfügung, Einsprache, Beschwerde und kantonale Varianten. |

## Quellenanker

Die zentralen Quellen sind in [`references/quellen.md`](./references/quellen.md) gesammelt. Skills sollen diese Datei laden, wenn Quellen, Rechtsstand oder Zitierweise relevant sind.

## Entwicklung

```bash
python3 scripts/count.py
python3 scripts/validate.py
```

Der Validator prüft Marketplace, Plugin-Manifeste, Skill-Frontmatter, lokale Links und Kennzahlen-Drift im README.

## Nächste Ausbaustufen

1. Strafrecht und Strafprozessrecht Schweiz.
2. Datenschutzrecht DSG/nDSG und KI-Governance.
3. Zivilprozessrecht mit kantonaler Schlichtungslogik.
4. Steuerrecht Bund/Kantone.
5. Testakten mit fiktiven Schweizer Sachverhalten und Rubrics.
