from loguru import logger

from aide.jab import Jab
from core.config import initialize_app


initialize_app()


def main():
    logger.info("++++++++")
    logger.info(" live./\\\\I")
    logger.info("++++++++")
    j = Jab()
    print()
    print()
    while True:
        inp = input("ask live.AI anything today ?")
        if inp.lower() == "q":
            logger.info("Bye Bye !")
            break
        print()
        print()
        logger.info("---------------------------")
        logger.info(f" {j.get_response(inp)} <<<")
        logger.info("---------------------------")


if __name__ == "__main__":
    main()
