# OTS Discipline Pack

A set of 45 discipline stubs for the [Ontological Type System](https://laytheo.com/instruments/ontological-type-system).

## Contents

Each file is an Obsidian note with subtype `[[Discipline]]`, containing a definition, key people, associations, and a short description. Coverage:

- Theology (13): Theology, Systematic Theology, Biblical Theology, Historical Theology, Practical Theology, Liturgical Theology, Theological Anthropology, Christology, Pneumatology, Soteriology, Ecclesiology, Eschatology, Theology Proper
- Biblical and textual (7): Biblical Studies, Old Testament Studies, New Testament Studies, Patristics, Hermeneutics, Exegesis, Textual Criticism
- Philosophy (12): Philosophy, Metaphysics, Epistemology, Ethics, Logic, Aesthetics, Philosophy of Religion, Philosophy of Mind, Philosophy of Language, Political Philosophy, Philosophy of History, Philosophy of Science
- History (5): History, Classical History, Ancient Near Eastern Studies, Church History, Archaeology
- Linguistic and literary (3): Linguistics, Philology, Literary Criticism
- Social sciences (5): Sociology, Anthropology, Psychology, Political Science, Economics

## Usage

Drop the files into an Obsidian vault. Use them as targets for the `associations` field on other notes.

## Format

Frontmatter:

- `type: "[[Idea]]"`
- `subtype: "[[Discipline]]"`
- `name`
- `definition` (one sentence, quoted)
- `aliases` (list, populated where a recognized alternate name exists)
- `key_people` (list of wikilinks, 2 to 3 figures)
- `state: Stable`
- `created`
- `associations` (list of wikilinks to parent or adjacent disciplines)

Body: one `## Description` paragraph.

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, the author has waived all copyright and related or neighboring rights to this work.
