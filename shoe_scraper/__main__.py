from .cli import main

if __name__ == "__main__":
    import asyncio

    raise SystemExit(asyncio.run(main()))
