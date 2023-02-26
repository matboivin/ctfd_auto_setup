"""Automatically setup CTFd instance."""

from argparse import Namespace
from typing import Any, Dict

import coloredlogs
from playwright.sync_api import Browser, Page, Playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright
from verboselogs import VerboseLogger

from .configuration import Configuration, get_configuration
from .helpers import parse_args
from .pages import (
    fill_administration_page,
    fill_general_page,
    fill_mode_page,
    select_ctf_theme,
    set_date_and_time,
)


def setup_instance(
    logger: VerboseLogger, configuration: Configuration, page: Page
) -> None:
    """Fill setup's fields automatically.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    configuration : Configuration
        The information to setup the CTFd instance.
    page : playwright.sync_api.Page
        The page opened in browser.

    """
    fill_general_page(logger, configuration, page)
    fill_mode_page(logger, configuration, page)
    fill_administration_page(logger, configuration, page)
    select_ctf_theme(logger, configuration, page)
    set_date_and_time(logger, configuration, page)

    page.get_by_role("button", name="Finish").click()

    logger.info("Done.")


def main(
    logger: VerboseLogger, configuration: Configuration, args: Namespace
) -> None:
    """Open web browser and page.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    configuration : Configuration
        The information to setup the CTFd instance.
    argparse.Namespace
        The program's arguments.

    """
    options: Dict[str, Any] = (
        {"headless": False, "slow_mo": 250} if args.debug else {}
    )

    playwright: Playwright = sync_playwright().start()

    try:
        logger.info("Launching Firefox")
        browser: Browser = playwright.firefox.launch(
            headless=options.get("headless", True),
            slow_mo=options.get("slowmo", 0),
        )

        logger.info(f"Opening: {args.url}")
        page: Page = browser.new_page()
        page.set_default_timeout(args.timeout)
        page.goto(args.url)

        setup_instance(logger, configuration, page)

    except PlaywrightTimeoutError as err:
        logger.error(err)

    finally:
        page.close()
        browser.close()
        playwright.stop()


def entrypoint() -> None:
    """Program's entrypoint."""
    args: Namespace = parse_args()
    logger: VerboseLogger = VerboseLogger("ctfd_setup")

    coloredlogs.install(
        logger=logger,
        level="DEBUG",
        fmt="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
    )

    try:
        configuration: Configuration = get_configuration()

        main(logger, configuration, args)

    except RuntimeError as err:
        logger.error(err)

    except KeyboardInterrupt as err:
        logger.warning(err)


if __name__ == "__main__":
    entrypoint()
