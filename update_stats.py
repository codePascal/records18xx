#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update database stats

Script to read the database tarball and extract number of game transcripts
per game and drop them into JSON files for usage in endpoint badges.
"""
import tarfile
import json
from pathlib import Path
from collections import Counter


def main():
    counts = Counter()
    with tarfile.open('database.tar.gz', 'r:gz') as tf:
        for member in tf.getmembers():
            if not member.isfile():
                continue
            if not member.name.endswith('.txt'):
                continue
            # Assume <game>/<game>_<id>/<game>_<id>.txt
            game = member.name.split('/')[1]
            counts[game] += 1

    for game, num in counts.items():
        badge_data = {
            'schemaVersion': 1,
            'label': f'{game} transcripts',
            'message': str(num),
            'color': 'blue'
        }
        file = Path('badges').joinpath(f'{game}.json')
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(badge_data, f, indent=2)


if __name__ == '__main__':
    main()
