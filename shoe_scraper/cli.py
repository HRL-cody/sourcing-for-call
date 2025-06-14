import asyncio
import csv
import sys
from argparse import ArgumentParser

from .platforms import alibaba, made_in_china, global_sources

PLATFORMS = [alibaba, made_in_china, global_sources]


async def main() -> int:
    parser = ArgumentParser(description="Shoe Scraper")
    parser.add_argument("--query", required=True)
    args = parser.parse_args()

    results = []
    for platform in PLATFORMS:
        results.extend(await platform.search(args.query))

    writer = csv.writer(sys.stdout)
    writer.writerow(["name", "phone", "source", "url"])
    for company in results:
        writer.writerow([company.name, company.phone, company.source, company.url])
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
