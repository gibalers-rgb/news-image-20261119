# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/gibalers-rgb/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/gibalers-rgb/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of Thursday, 19 November 2026: the first-ever Trump–Xi–Putin trilateral summit in Shenzhen and its "Declaration toward Peace"; the ICJ ruling that Myanmar committed genocide against the Rohingya; Anthropic's record Nasdaq debut; aid groups scoring the Gaza peace plan 4 out of 26; COP31 in Antalya cutting fossil fuels from its draft deal; and the EU's €45bn loan proposal for Ukraine.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). The image is 1024×1024 PNG, 311 KB — inside the gate's 1 MiB / 1024×1024 limits.

## How the image was made

- `assets/` holds the AI-generated banner illustration (three leaders at a summit table, dove over a world map — no text in the artwork).
- `compose.py` builds the final front page with PIL: masthead with the date, the banner, and six story panels with short, sourced headlines. All text is rendered programmatically so it stays crisp and legible at small sizes — no AI-garbled text.

## Stories (all from 19 November 2026)

| Story | What happened |
| --- | --- |
| Summit, Shenzhen | Trump, Xi and Putin hold the first trilateral summit; a four-point "Declaration toward Peace" and a pledge to cut nuclear risks. |
| Justice, The Hague | ICJ rules 9–6 that Myanmar's military committed genocide against the Rohingya in 2017. |
| Markets, New York | Anthropic prices its IPO at $83 (~$1.5tn value); shares jump ~34% on debut. |
| Gaza | Five aid groups score the peace plan 4 out of 26; the IDF's Nuseirat operation ends. |
| Climate, Antalya | COP31 ministers race to unblock talks as fossil-fuel language is cut from the draft deal. |
| Europe, Ukraine | EU proposes a €45bn loan; the UK pledges 1,000+ drones in a £260m package. |

Sources: BBC, Le Monde, Dow Jones, AP, ICJ, APEC.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1grmr2h6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
