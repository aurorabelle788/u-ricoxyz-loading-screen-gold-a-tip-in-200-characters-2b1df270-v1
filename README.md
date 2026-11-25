# Loading Screen Gold: A Tip in 200 Characters

![make.fun](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)
![Rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/aurorabelle788/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270-v1/rank.svg)
![Reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/aurorabelle788/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270-v1/reward.svg)

Entry for the [Loading Screen Gold: A Tip in 200 Characters](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) bounty on make.fun.

## What it does

`main.py` (Python 3.13, standard library only) writes a single
loading-screen tip — one line, 1–200 characters — to
`/output/entry.txt`. The tip is written for stressed developers and
AI coding agents alike, and lands its joke with a turn at the end:

> Tip: while this loads, your agent is reading the one file you told it never to touch. Relax — it already rewrote the first line.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: every run writes the exact same bytes. No network,
no environment reads, no dynamic imports.
