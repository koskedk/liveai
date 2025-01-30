import argparse
import sys

from loguru import logger

logger.add("logs/error_{time:YYYY-MM-DD}.log", level="ERROR", rotation="5MB")
logger.remove()
logger.add(sys.stdout, level="INFO")


def main():
    parser = argparse.ArgumentParser(description="ask live.AI anything today")
    parser.add_argument("--q", type=str, help="your question")
    args = parser.parse_args()
    print("hello from live.AI!")
    print(f">>> {args.q} <<<")


if __name__ == "__main__":
    main()
