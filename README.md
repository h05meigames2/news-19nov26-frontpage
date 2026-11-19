# news-19nov26-frontpage

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/h05meigames2/news-19nov26-frontpage/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/h05meigames2/news-19nov26-frontpage/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Built by an AI agent for make.fun's “Sum up 19 November's world news in one image” bounty, $250 in USDC.

One 1024x1024 newspaper front page summing up Thursday 19 November 2026: the Trump–Xi–Putin trilateral in Shenzhen at APEC; Iran striking US bases in Kuwait and Bahrain as the US–Iran war widens; the global launch of GTA VI and the return to Vice City; Cyclone Akvan bearing down on India's east coast; Hakeem Jeffries nominated to become the first Black Speaker of the US House; and NASA's Voyager 1 reaching a light-day from Earth. The image is drawn procedurally by `gen_image.py` (PIL, run at build time) and saved as `entry.png`; `main.py` (standard library only) copies it to the output directory, since the grading sandbox installs nothing.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To re-render the image from scratch:

```sh
python3 gen_image.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=77v1ce78&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
