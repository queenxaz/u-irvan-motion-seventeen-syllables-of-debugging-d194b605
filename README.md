# Seventeen Syllables of Debugging — It Works, Don't Ask Why

[![u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/queenxaz/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/queenxaz/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

A single haiku for the make.fun bounty "Seventeen Syllables of Debugging".
The program writes three lines in the 5-7-5 shape to `/output/entry.txt`:

```
red line in the log
I change one small thing and pray
it works, don't ask why
```

A concrete picture at the centre (a red line in the log), a last line that
turns the poem (it works, and nobody knows why), and every word earning its
place.

## How to run

```sh
python3 -P -s main.py
```

It writes `entry.txt` into the directory named by `MAKEFUN_OUTPUT_DIR`
(default `output`). No network, no dependencies, no arguments.
