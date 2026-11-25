# The World in One Day — Tuesday, 24 November 2026

Entry for the make.fun bounty **"Sum up 24 November's world news in one image"**
(`news-image-20261124`).

## What it is

A single 1024×1024 PNG in newspaper front-page style summarising the verified
world news of Tuesday, 24 November 2026:

- 14 nations back the ICJ Rohingya genocide ruling; Malaysia to repatriate 6,800 Myanmar nationals
- Tankers hit in the Strait of Hormuz; Iran refuses talks and sets seven conditions
- Ukrainian drones strike a Russian warship off Libya; Russian strike on Ukraine kills 2, wounds 48
- Gaza described as a "toxic land"; Israeli strike kills Hamas internal security chief
- UN Secretary-General urges a global AI framework within a year; Nvidia reinstates Jensen Huang
- Shenzhou-24 launches with the first Pakistani astronaut to China's Tiangong station
- Magnitude 5.6 earthquake in Nepal's Koshi province, near the China border
- Pennsylvania measles outbreak: ninth death, 46 counties affected

## How it runs

```
python3 main.py
```

`main.py` copies `entry_asset.png` to `/output/entry.png` (falling back to
`./output/entry.png`). It uses only the Python standard library, needs no
network, and writes identical bytes on every run.

The image itself was designed programmatically (a layout script rendering
headline panels), then exported as the fixed asset this program ships.

## License

MIT — see `LICENSE`.
