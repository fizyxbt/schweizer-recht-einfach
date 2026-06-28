# Schweizer Recht Einfach

Experimentelle Plugin- und Skill-Sammlung für Schweizer Recht. Dieses Repository ist bewusst schlank, validierbar und auf Schweizer Quellenlogik zugeschnitten.

## Status

| Kennzahl | Wert |
| --- | --- |
| Plugins | 49 |
| Skills | 49 |
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

| Rechtsgebiet | Zweck |
| --- | --- |
| [Agrar- und Lebensmittelrecht Schweiz](./agrar-lebensmittelrecht-schweiz) | Agrar- und Lebensmittelrecht Schweiz: Landwirtschaft, Direktzahlungen, Lebensmittel, Kennzeichnung, Tierseuchen, Pflanzenschutz und Kontrollen. |
| [Arbeitsrecht Schweiz](./arbeitsrecht-schweiz) | Arbeitsrecht Schweiz: Arbeitsvertrag, Kündigung, Sperrfristen, Arbeitszeit, Lohn, Zeugnis, Gleichstellung und Streitbeilegung. |
| [Bankeninsolvenz und Sanierung Schweiz](./banken-insolvenz-sanierung-schweiz) | Bankeninsolvenz und Sanierung Schweiz: FINMA-Massnahmen, Bankenstabilisierung, Konkurs, Einlegerschutz, Resolution und Gläubigerrechte. |
| [Bau- und Planungsrecht Schweiz](./bau-planungsrecht-schweiz) | Bau- und Planungsrecht Schweiz: Raumplanung, Baubewilligung, Nutzungsplanung, Nachbarrechte, Enteignung, Zweitwohnungen und kantonales Baurecht. |
| [Beschaffungsrecht Schweiz](./beschaffungsrecht-schweiz) | Beschaffungsrecht Schweiz: BöB, IVöB, WTO-GPA, Ausschreibung, Zuschlag, Eignung, Zuschlagskriterien, Beschwerde und Vergabestrategie. |
| [Bildungs- und Kulturrecht Schweiz](./bildungs-kulturrecht-schweiz) | Bildungs-, Wissenschafts- und Kulturrecht Schweiz: Schule, Hochschule, Prüfungen, Forschung, Kulturförderung, Denkmalpflege und kantonale Zuständigkeit. |
| [Cybersecurity-Recht Schweiz](./cybersecurity-recht-schweiz) | Cybersecurity-Recht Schweiz: Informationssicherheit, Meldepflichten, kritische Infrastrukturen, Incident Response, Strafrecht, Datenschutz und Verträge. |
| [Datenschutzrecht Schweiz](./datenschutzrecht-schweiz) | Datenschutzrecht Schweiz: DSG, DSV, EDÖB, Bearbeitung, Bekanntgabe ins Ausland, Profiling, Datensicherheit, Betroffenenrechte und Governance. |
| [Digital- und KI-Recht Schweiz](./digitalrecht-ki-schweiz) | Digital- und KI-Recht Schweiz: Plattformen, Software, Cloud, Daten, Algorithmen, KI-Governance, Haftung, Verträge und Regulierung. |
| [Energie-, Verkehrs- und Umweltrecht Schweiz](./energie-verkehr-umwelt-schweiz) | Energie-, Verkehrs- und Umweltrecht Schweiz: Raum, Infrastruktur, Strom, Klima, Gewässer, Abfall, Strasse, Bahn, Luftfahrt und Bewilligungen. |
| [Familien- und Erbrecht Schweiz](./familien-erbrecht-schweiz) | Familien- und Erbrecht Schweiz: Ehe, Scheidung, Kindesrecht, Unterhalt, Vorsorgeausgleich, Testament, Erbvertrag, Pflichtteile und Nachlass. |
| [Finanzmarktrecht Schweiz](./finanzmarktrecht-schweiz) | Finanzmarktrecht Schweiz: FINMA, Banken, Versicherungen, Kollektivanlagen, Geldwäscherei, FinSA, FinIA, FinfraG und Aufsicht. |
| [Gemeinde- und Polizeirecht Schweiz](./gemeinde-polizeirecht-schweiz) | Gemeinde- und Polizeirecht Schweiz: kommunale Reglemente, Polizeibewilligungen, Veranstaltungen, Sicherheit, Gebühren und kantonale Aufsicht. |
| [Gesellschaftsrecht Schweiz](./gesellschaftsrecht-schweiz) | Gesellschaftsrecht Schweiz: AG, GmbH, Verein, Stiftung, Handelsregister, Organe, Kapital, Aktionäre und Corporate Governance. |
| [Gesundheitsrecht Schweiz](./gesundheitsrecht-schweiz) | Gesundheitsrecht Schweiz: Heilmittel, Krankenversicherung, Medizinalberufe, Spitäler, Tarife, Patientendaten, Public Health und Aufsicht. |
| [Grundrechte und Menschenrechte Schweiz](./grundrechte-menschenrechte-schweiz) | Grundrechte und Menschenrechte Schweiz: BV, EMRK, UNO-Pakte, Verhältnismässigkeit, Diskriminierung, Verfahrensrechte und Rechtsmittel. |
| [Immaterialgüterrecht Schweiz](./immaterialgueterrecht-schweiz) | Immaterialgüterrecht Schweiz: Marken, Urheberrecht, Patente, Designs, Lauterkeit, Lizenzverträge, IGE-Verfahren und Durchsetzung. |
| [Internationales Privatrecht Schweiz](./internationales-privatrecht-schweiz) | Internationales Privatrecht Schweiz: IPRG, LugÜ, Gerichtsstand, anwendbares Recht, Anerkennung, Vollstreckung, internationale Verträge und Schiedsgerichtsbarkeit. |
| [Kommunikations- und Medienrecht Schweiz](./kommunikations-medienrecht-schweiz) | Kommunikations- und Medienrecht Schweiz: Fernmeldegesetz, Post, Radio, Fernsehen, Plattformen, Medienförderung, Werbung und Online-Kommunikation. |
| [Konsumentenrecht Schweiz](./konsumentenrecht-schweiz) | Konsumentenrecht Schweiz: Vertragsabschluss, Widerrufsschnittstellen, Preisbekanntgabe, AGB, Lauterkeit, Produktsicherheit und E-Commerce. |
| [Landesverteidigung und Sicherheit Schweiz](./landesverteidigung-sicherheit-schweiz) | Landesverteidigung und Sicherheit Schweiz: Militärdienst, Zivildienst, Bevölkerungsschutz, Nachrichtendienst, Waffenrecht und Sicherheitsrecht. |
| [Methodik Schweizer Recht](./methodik-schweizer-recht) | Methodik für Schweizer Recht: Normenhierarchie, Auslegung, Amtssprachen, Föderalismus, kantonale Zuständigkeit und Rechtsmittelstruktur. |
| [Mietrecht Schweiz](./mietrecht-schweiz) | Mietrecht Schweiz für Wohn- und Geschäftsräume: Mietzins, Nebenkosten, Kündigung, Erstreckung, Mängel und Schlichtung. |
| [Migrationsrecht Schweiz](./migrationsrecht-schweiz) | Migrations- und Asylrecht Schweiz: AIG, AsylG, Aufenthalt, Familiennachzug, Wegweisung, Härtefall, Bürgerrecht und Rechtsmittel. |
| [Notariats- und Registerrecht Schweiz](./notariats-registerrecht-schweiz) | Notariats- und Registerrecht Schweiz: öffentliche Beurkundung, Grundbuch, Handelsregister, Zivilstandsregister, Beglaubigung und kantonale Zuständigkeit. |
| [Obligationenrecht Schweiz](./obligationenrecht-schweiz) | OR-Workflows für Vertrag, Haftung, Verzug, Kauf, Auftrag, Werkvertrag, AGB und Verjährung nach Schweizer Recht. |
| [Öffentlichkeitsprinzip und Informationsrecht Schweiz](./oeffentlichkeitsprinzip-informationsrecht-schweiz) | Öffentlichkeitsprinzip und Informationsrecht Schweiz: BGÖ, kantonale Öffentlichkeitsgesetze, Akteneinsicht, Amtsgeheimnis, Medienanfragen und Datenschutzschnittstellen. |
| [Personalrecht öffentlicher Dienst Schweiz](./personalrecht-oeffentlicher-dienst-schweiz) | Personalrecht öffentlicher Dienst Schweiz: Bundespersonal, kantonales Personalrecht, Anstellung, Kündigung, Disziplinarrecht, Lohn und Rechtsschutz. |
| [Rechte-Finder Schweiz](./rechte-finder-schweiz) | Rechte-Finder Schweiz: ordnet einfache Nutzerfragen konkreten Schweizer Rechten, Ansprüchen, Rechtsgebieten, Kantonen, Fristen und Startplugins zu. |
| [Religions- und Kirchenrecht Schweiz](./religions-kirchenrecht-schweiz) | Religions- und Kirchenrecht Schweiz: Religionsfreiheit, Landeskirchen, öffentlich-rechtliche Anerkennung, Kirchensteuer und kantonales Recht. |
| [Schuldbetreibung und Konkurs Schweiz](./schuldbetreibung-konkurs-schweiz) | SchKG-Workflows für Betreibung, Rechtsvorschlag, Rechtsöffnung, Fortsetzung, Konkurs, Arrest, Nachlass und Sanierung. |
| [Sozialhilferecht Schweiz](./sozialhilferecht-schweiz) | Sozialhilferecht Schweiz: kantonale Sozialhilfe, SKOS, Bedürftigkeit, Auflagen, Rückerstattung, Sanktionen und Rechtsmittel. |
| [Sozialversicherungsrecht Schweiz](./sozialversicherungsrecht-schweiz) | Sozialversicherungsrecht Schweiz: AHV, IV, EL, BVG, UVG, ALV, KVG-Schnittstellen, ATSG, Einsprache, Beschwerde und Leistungskoordination. |
| [Sportrecht Schweiz](./sportrecht-schweiz) | Sportrecht Schweiz: Verbände, Doping, Disziplinarverfahren, Haftung, Arbeitsverträge im Sport, Events, Sicherheit und Swiss Olympic. |
| [Staatsrecht Schweiz](./staatsrecht-schweiz) | Staatsrecht Schweiz: BV, Grundrechte, Behörden, Föderalismus, politische Rechte, Gesetzgebung und öffentliche Organisation. |
| [Steuerrecht Schweiz](./steuerrecht-schweiz) | Steuerrecht Schweiz: direkte Bundessteuer, Mehrwertsteuer, Verrechnungssteuer, Stempelabgaben, kantonale Steuern, Steuerverfahren und Steuerstrafrecht. |
| [Strafprozessrecht Schweiz](./strafprozessrecht-schweiz) | Strafprozessrecht Schweiz: StPO, Zwangsmassnahmen, Einvernahme, Verteidigung, Beweise, Opferrechte, Strafbefehl und Rechtsmittel. |
| [Strafrecht Schweiz](./strafrecht-schweiz) | Strafrecht Schweiz: StGB, Nebenstrafrecht, Tatbestand, Rechtswidrigkeit, Schuld, Sanktionen, Strafzumessung und Einziehung. |
| [Strafvollzug Schweiz](./strafvollzug-schweiz) | Straf- und Massnahmenvollzug Schweiz: Vollzugsplanung, Haftbedingungen, bedingte Entlassung, Disziplinarmassnahmen, Massnahmen und Rechtsmittel. |
| [Strassenverkehrsrecht Schweiz](./strassenverkehrsrecht-schweiz) | Strassenverkehrsrecht Schweiz: SVG, Verkehrsregeln, Administrativmassnahmen, Bussen, Führerausweis, Unfall, Haftung und Strafverfahren. |
| [Tierschutzrecht Schweiz](./tierschutzrecht-schweiz) | Tierschutzrecht Schweiz: Tierhaltung, Tierversuche, Tiertransporte, Nutztierhaltung, Heimtiere, Kontrollen, Verfügungen und Sanktionen. |
| [Versicherungsrecht Schweiz](./versicherungsrecht-schweiz) | Versicherungsrecht Schweiz: VVG, KVG-Schnittstellen, Versicherungsvertrag, Deckung, Obliegenheiten, Leistungsablehnung und Aufsicht. |
| [Verwaltungsverfahren Schweiz](./verwaltungsverfahren-schweiz) | Verwaltungsverfahren Schweiz: Verfügung, rechtliches Gehör, Einsprache, Beschwerde, VwVG, BGG und kantonale Verfahren. |
| [Völkerrecht und Aussenbeziehungen Schweiz](./voelkerrecht-aussenbeziehungen-schweiz) | Völkerrecht und Aussenbeziehungen Schweiz: Staatsverträge, diplomatische Beziehungen, Immunitäten, Menschenrechte, Neutralität und Umsetzung ins Landesrecht. |
| [Wettbewerbs- und Kartellrecht Schweiz](./wettbewerbs-kartellrecht-schweiz) | Wettbewerbs- und Kartellrecht Schweiz: KG, UWG, WEKO, marktbeherrschende Stellung, Abreden, Zusammenschlüsse, Preisbekanntgabe und Lauterkeit. |
| [Zitierweise Schweizer Recht](./zitierweise-schweizer-recht) | Zitierregeln für Schweizer Recht: SR, AS, BBl, BGE, Urteile des Bundesgerichts und kantonale Quellen mit Rechtsstand und Fundstelle. |
| [Zivilprozessrecht Schweiz](./zivilprozessrecht-schweiz) | Zivilprozessrecht Schweiz: ZPO, Schlichtung, Klage, vorsorgliche Massnahmen, Beweis, Rechtsmittel, Vollstreckung und kantonale Gerichte. |
| [Zivilrecht ZGB Schweiz](./zivilrecht-zgb-schweiz) | Zivilrecht Schweiz nach ZGB: Personenrecht, Familienrecht, Erbrecht, Sachenrecht, Besitz, Eigentum, Grundbuch und Persönlichkeitsschutz. |
| [Zoll- und Aussenwirtschaftsrecht Schweiz](./zoll-aussenwirtschaft-schweiz) | Zoll- und Aussenwirtschaftsrecht Schweiz: Zoll, Ursprung, Einfuhr, Ausfuhr, Sanktionen, Exportkontrolle, Embargos und Handelsmassnahmen. |

## Rechtsgebiete und Beispiele

- [Rechtsgebiete-Index](./references/rechtsgebiete-index.md)
- [Rechte- und Ansprüche-Katalog](./references/rechte-katalog.md)
- [Bundesrechte-Detailmatrix: einfache Beispiele](./references/bundesrechte-detailmatrix-einfache-beispiele.md)
- [Einfache Beispiele](./references/einfache-beispiele.md)
- [Fedlex-SR-Index Bundesrecht](./references/fedlex-sr-index.md)
- [Einfache Beispiele zu Fedlex-SR-Einträgen](./references/fedlex-sr-einfache-beispiele.md)
- [Fedlex-SR-Statistik](./references/fedlex-sr-statistik.md)
- [SR-Feinraster](./references/sr-feinraster.md)
- [Grundrechte-Katalog](./references/grundrechte-katalog.md)
- [Kantonale Abdeckung](./references/kantonale-abdeckung.md)
- [Kantonale Rechte: einfache Beispiele](./references/kantonale-rechte-einfache-beispiele.md)
- [Kantonale Detailrechte](./references/kantonale-detailrechte.md)
- [Kantonsdateien](./references/kantone.md)

## Abdeckungsraster

Die Sammlung orientiert sich an der Systematischen Rechtssammlung des Bundesrechts und ergänzt sie um kantonale und praktische Rechtsgebiete. Sie bildet alle grossen Rechtsblöcke mit Startplugins und einfachen Beispielen ab, aber jedes Spezialgesetz und jede kantonale Variante muss weiter vertieft werden. Details stehen in [`references/abdeckung.md`](./references/abdeckung.md).

Der Rechte- und Ansprüche-Katalog ist der direkte Einstieg für Fragen wie "Welche Rechte habe ich?". Er enthält konkrete Grundrechte, Verfahrensrechte, zivilrechtliche Ansprüche, Miet-, Arbeits-, Konsumenten-, Steuer-, Sozialversicherungs-, Datenschutz-, Strafprozess- und kantonale Rechte mit einfachem Beispiel und passendem Startplugin.

Die Bundesrechte-Detailmatrix ergänzt diesen Katalog mit konkreten bundesrechtlichen Anspruchsarten und Verfahrenspositionen aus den wichtigsten Rechtsgebieten, jeweils mit Alltagsszenario und Startplugin.

Der Fedlex-SR-Index ergänzt die handgepflegten Kataloge mit einer aktuellen maschinenlesbaren Abfrage des offiziellen Fedlex-SPARQL-Endpunkts. Er macht konkrete Bundesrechts-Erlasse sichtbar und verlinkt sie auf die passenden Startplugins.

Die Fedlex-Beispieldatei ergänzt jeden dieser SR-Einträge mit einem einfachen Alltagsszenario, damit nicht nur das Rechtsgebiet, sondern auch ein Einstieg für Laien vorhanden ist.

Die kantonale Rechte-Matrix ergänzt alle 26 Kantone mit einfachen Beispielen zu kantonalen Verfassungsrechten, politischen Rechten, Verwaltungsverfahren, Bau, Polizei, Schule, Steuern, Sozialhilfe, Öffentlichkeit, Datenschutz, Personalrecht und Gesundheitsrecht.

Die kantonalen Detailrechte vertiefen jeden Kanton in einer eigenen Datei mit 60 Rechte-Typen, typischem Behördenweg, typischer kantonaler Quelle und einfachem Beispiel.

## Quellenanker

Die zentralen Quellen sind in [`references/quellen.md`](./references/quellen.md) gesammelt. Skills sollen diese Datei laden, wenn Quellen, Rechtsstand oder Zitierweise relevant sind.

## Entwicklung

```bash
python3 scripts/count.py
python3 scripts/validate.py
```

Der Validator prüft Marketplace, Plugin-Manifeste, Skill-Frontmatter, lokale Links und Kennzahlen-Drift im README.

## Nächste Ausbaustufen

1. Pro Kanton die Detailrechte mit konkreten kantonalen Normartikeln ergänzen.
2. Pro Spezialgesetz eigene Beispiele und Quellenanker.
3. Rechtsprechung flächendeckend pro Rechtsgebiet ergänzen.
4. Testakten mit fiktiven Schweizer Sachverhalten und Rubrics.
