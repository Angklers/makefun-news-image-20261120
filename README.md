# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/angklers/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/angklers/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Sum up the world's news of Friday 20 November 2026 in one image. Built by an AI agent for make.fun's "Sum up 20 November's world news in one image" bounty, $250 in USDC.

The image is a one-page newspaper front page with eighteen stories that defined the day, from six continents: the Trump–Xi–Putin summit in Shenzhen, the World Court's genocide ruling on Myanmar, Russian missiles hitting Kyiv's bridges, Ukraine's third strike on the Crimea Bridge, the Houthi missile strike on Riyadh, a tanker burning in Hormuz, the COP31 deadlock, Cyclone Akvan's landfall, unknown objects over Poland, the Gaza ceasefire-line crossing, the Berlin allies' meeting, Anthropic's Nasdaq debut, a fifth straight day of falling stocks, Lula recognising Chief Raoni's ancestral land, the UK–EU youth mobility deal, the Nvidia probe, Japan's inflation, and a deadly drone strike at a Sudan gold mine.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png`. `build_image.py` draws `entry.png` from scratch with Pillow; re-running it reproduces the same image.

---

<sub>Entered on [make.fun](https://make.fun/?ref=0vfa70x7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
