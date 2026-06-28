# Claude fuer Schweizer Recht

Experimentelle Claude-Plugin- und Skill-Sammlung fuer Schweizer Recht. Dieses Repository ist ein Startgeruest nach dem Muster von `claude-fuer-deutsches-recht`, aber bewusst schlank, validierbar und auf Schweizer Quellenlogik zugeschnitten.

## Status

| Kennzahl | Wert |
| --- | --- |
| Plugins | 8 |
| Skills | 8 |
| Version | 0.1.0 |
| Marketplace | [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json) |

## Leitprinzipien

1. Schweizer Recht zuerst nach Norm, Kanton, Instanz und Sprache einordnen.
2. Bundesrecht ueber Fedlex zitieren, insbesondere SR, AS und BBl.
3. Bundesgerichtliche Rechtsprechung mit BGE oder Geschaeftsnummer, Datum, Abteilung und Fundstelle zitieren.
4. Kantonales Recht nur mit explizitem Kanton und offizieller Gesetzessammlung verwenden.
5. Literatur, private Datenbanken und Kommentare nur verwenden, wenn der Nutzer die Quelle bereitstellt oder der Zugriff im konkreten System nachweisbar ist.
6. Rechtsstand immer als Datum ausweisen.

## Enthaltene Start-Plugins

| Plugin | Zweck |
| --- | --- |
| [`zitierweise-schweizer-recht`](./zitierweise-schweizer-recht) | Zitierregeln fuer SR, AS, BBl, BGE, Urteile und kantonale Quellen. |
| [`methodik-schweizer-recht`](./methodik-schweizer-recht) | Methodik fuer Auslegung, Normenhierarchie, mehrsprachige Fassungen und Foederalismus. |
| [`obligationenrecht-schweiz`](./obligationenrecht-schweiz) | OR-Workflows fuer Vertrag, Haftung, Verzug, Kauf, Auftrag, Werkvertrag und AGB. |
| [`arbeitsrecht-schweiz`](./arbeitsrecht-schweiz) | Arbeitsvertrag, Kuendigung, Sperrfristen, Arbeitszeit, Zeugnis, Lohn und Gleichstellung. |
| [`mietrecht-schweiz`](./mietrecht-schweiz) | Wohn- und Geschaeftsraummiete, Mietzins, Kuendigung, Erstreckung und Schlichtung. |
| [`gesellschaftsrecht-schweiz`](./gesellschaftsrecht-schweiz) | AG, GmbH, Verein, Stiftung, Handelsregister und Corporate Governance. |
| [`schuldbetreibung-konkurs-schweiz`](./schuldbetreibung-konkurs-schweiz) | SchKG-Workflows fuer Betreibung, Rechtsvorschlag, Rechtsöffnung, Konkurs und Sanierung. |
| [`verwaltungsverfahren-schweiz`](./verwaltungsverfahren-schweiz) | VwVG/BGG-Methodik, Verfuegung, Einsprache, Beschwerde und kantonale Varianten. |

## Quellenanker

Die zentralen Quellen sind in [`references/quellen.md`](./references/quellen.md) gesammelt. Skills sollen diese Datei laden, wenn Quellen, Rechtsstand oder Zitierweise relevant sind.

## Entwicklung

```bash
python3 scripts/count.py
python3 scripts/validate.py
```

Der Validator prueft Marketplace, Plugin-Manifeste, Skill-Frontmatter, lokale Links und Kennzahlen-Drift im README.

## Naechste Ausbaustufen

1. Strafrecht und Strafprozessrecht Schweiz.
2. Datenschutzrecht DSG/nDSG und KI-Governance.
3. Zivilprozessrecht mit kantonaler Schlichtungslogik.
4. Steuerrecht Bund/Kantone.
5. Testakten mit fiktiven Schweizer Sachverhalten und Rubrics.
