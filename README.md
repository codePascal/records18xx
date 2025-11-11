18xx Transcript Database
========================

![Endpoint Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/codePascal/records18xx/refs/heads/first_version/badges/1817.json)
![Endpoint Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/codePascal/records18xx/refs/heads/first_version/badges/1830.json)
![Endpoint Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/codePascal/records18xx/refs/heads/first_version/badges/1889.json)

A repository that hosts game transcripts from [18xx.games](https://18xx.games/).

Features
--------

* A growing collection of plain game transcripts of various game variants (e.g.,
  1830, 1889).
* Consistent file structure making it easy to iterate and analyse.

Usage
-----

Download the tarball `database.tar.gz` and extract it on a desired location on
your machine.
Suggested location is `~/.database18xx`.

Database structure
------------------

Each game variant has a corresponding folder, named equal to its 18xx variant.
Within that folder, individual transcripts are saved as .txt files in a folder
called equal to the transcript name.

```
database.tar.gz
├───1817
│   ├───1830_123456
│   │   └───1830_123456.txt
│   └───...
└───1830
    ├───1830_123456
    │   └───1830_123456.txt
    └───...
```

Transcript names follow a consistent naming convention:

```
<game_type>_<game_id>
```

* `game_type`: Abbreviation of the 18xx variant (e.g., 1830, 1889)
* `game_id`: The 6-digit game ID



