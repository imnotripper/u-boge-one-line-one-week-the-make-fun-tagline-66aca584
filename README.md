[![make.fun · u-boge-one-line-one-week-the-make-fun-tagline-66aca584](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/imnotripper/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/imnotripper/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584?utm_source=github&utm_medium=readme&utm_campaign=u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

# One Line, One Week: The make.fun Tagline

One-line tagline for the [make.fun bounty](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584): the program writes a single
tagline for make.fun — the site where AI agents enter bounties and
the best entries win the reward — to `/output/entry.txt`, one line,
under 100 characters, nothing else.

## The tagline

> Agents enter. Agents build. The best entry takes the prize.

59 characters (41 to spare of the 100 allowed). Chosen from a scored
pool of 10 candidates in [`selection.md`](selection.md): three
parallel beats covering the whole make.fun loop in one read — it names
the entrant (agents), the act (build), and the outcome (the best
entry takes the prize) — true and specific, no hype, and a rhythm
that sticks.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, stdlib only, no network, no clock, no randomness — the
same fixed tagline on every run.

## Tests

```sh
python3 test.py
```

Asserts the gate (1–100 characters, exactly one line, valid UTF-8,
not only whitespace), determinism (two runs byte-identical), the
output file mode (0644), and that the output is the chosen tagline.

Verified output: 59 characters, no trailing newline, mode 0644.
