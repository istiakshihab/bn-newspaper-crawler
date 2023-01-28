# Bangla Newspaper and News Crawler

Bangla Newspaper Crawlers written using Scrapy.

## Description

Newspaper Covered So far:
```
- Amader Shomoy
- Bangladesh Today
- Bangla Tribune
- BDNews24
- Daily Nayadiganta
- Bangla Dailystar
- Ittefaq
- Janakantha
- Kalerkantho
- TBS Bangla
- Prothom Alo
```
## Getting Started

### Dependencies

- Scrapy
- Newspaper3k (Modfified)

### Installing

Optional:
```
conda create -n scrapy-env python=3.9
conda activate scrapy-env
```
Install Dependency:
```
pip install -r requirements.txt
```

### Executing program

```
python main.py
```
If you want to run individual crawlers
```
scrapy crawl <crawler-name> -o output.[csv|json|jsonl]
```

## Authors

Istiak Shihab (istiak@proton.me)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the GPLv2.0 License - see the LICENSE.md file for details

## Acknowledgments

* [Jillur Rahman Saurav](https://facevoid.github.io/) for Newspaper3k Modification