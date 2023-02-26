"""Automatically fill page's fields."""


from playwright.sync_api import Page
from verboselogs import VerboseLogger

from .configuration import Configuration


def fill_general_page(
    logger: VerboseLogger, configuration: Configuration, page: Page
) -> None:
    """Fill CTF name and description.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    configuration : Configuration
        The information to setup the CTFd instance.
    page : playwright.sync_api.Page
        The page opened in browser.

    """
    logger.info(f"Event name: {configuration.event_name}")
    page.locator("#ctf_name").fill(configuration.event_name)

    logger.info(f"Event description: {configuration.event_description}")
    page.locator("#ctf_description").fill(configuration.event_description)

    page.get_by_role("button", name="Next").click()


def fill_mode_page(
    logger: VerboseLogger, configuration: Configuration, page: Page
) -> None:
    """Select user or team mode.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    configuration : Configuration
        The information to setup the CTFd instance.
    page : playwright.sync_api.Page
        The page opened in browser.

    """
    mode: str = "User Mode" if configuration.user_mode else "Team mode"

    logger.info(f"Mode: {mode}")
    page.click(f"label[for='user_mode-{configuration.user_mode}']")

    page.get_by_role("button", name="Next").click()


def fill_administration_page(
    logger: VerboseLogger, configuration: Configuration, page: Page
) -> None:
    """Fill administrator information.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    configuration : Configuration
        The information to setup the CTFd instance.
    page : playwright.sync_api.Page
        The page opened in browser.

    """
    logger.info(f"Admin username: {configuration.admin_username}")
    page.locator("#name").fill(configuration.admin_username)

    logger.info(f"Admin email address: {configuration.admin_email}")
    page.locator("#email").fill(configuration.admin_email)

    logger.info(f"Admin email password: {configuration.admin_password}")
    page.locator("#password").fill(configuration.admin_password)

    page.locator("#newsletter-checkbox").click()

    page.get_by_role("button", name="Next").click()


def select_ctf_theme(
    logger: VerboseLogger, configuration: Configuration, page: Page
) -> None:
    """Select your CTF theme.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    configuration : Configuration
        The information to setup the CTFd instance.
    page : playwright.sync_api.Page
        The page opened in browser.

    """
    logger.info(f"Theme: {configuration.theme_name}")
    page.locator("#ctf_theme").select_option(configuration.theme_name)

    page.get_by_role("button", name="Next").click()


def set_date_and_time(
    logger: VerboseLogger, configuration: Configuration, page: Page
) -> None:
    """Set start time and end time.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    configuration : Configuration
        The information to setup the CTFd instance.
    page : playwright.sync_api.Page
        The page opened in browser.

    """
    logger.info(
        f"Starts: {configuration.start_date} at {configuration.start_time}"
    )
    page.locator("#start-date").fill(configuration.start_date)
    page.locator("#start-time").fill(configuration.start_time)

    logger.info(f"Ends: {configuration.end_date} at {configuration.end_time}")
    page.locator("#end-date").fill(configuration.end_date)
    page.locator("#end-time").fill(configuration.end_time)

    page.get_by_role("button", name="Next").click()
