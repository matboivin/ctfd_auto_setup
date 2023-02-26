"""Configuration settings (must be set in .env file)."""

import os
from dataclasses import dataclass
from typing import Union


@dataclass
class Configuration:
    event_name: str
    event_description: str
    user_mode: int
    admin_username: str
    admin_email: str
    admin_password: str
    theme_name: str
    start_date: str
    start_time: str
    end_date: str
    end_time: str


def get_configuration() -> Configuration:
    """Fill admin information.

    Parameters
    ----------
    logger : VerboseLogger
        The program's logger.
    page : playwright.sync_api.Page
        The page opened in browser.

    Returns
    -------
    Configuration
        The configuration settings as an object.

    Raises
    ------
    RuntimeError
        If some environment variables are missing.

    """
    event_name: Union[str, None] = os.getenv("EVENT_NAME")
    event_description: Union[str, None] = os.getenv("EVENT_DESCRIPTION")
    user_mode: Union[str, None] = os.getenv("USER_MODE")
    admin_username: Union[str, None] = os.getenv("ADMIN_USERNAME")
    admin_email: Union[str, None] = os.getenv("ADMIN_EMAIL")
    admin_password: Union[str, None] = os.getenv("ADMIN_PASSWORD")
    theme_name: Union[str, None] = os.getenv("THEME_NAME", "core")
    start_date: Union[str, None] = os.getenv("START_DATE")
    start_time: Union[str, None] = os.getenv("START_TIME")
    end_date: Union[str, None] = os.getenv("END_DATE")
    end_time: Union[str, None] = os.getenv("END_TIME")

    if not all(
        [
            event_name,
            event_description,
            user_mode,
            admin_username,
            admin_email,
            admin_password,
            theme_name,
            start_date,
            start_time,
            end_date,
            end_time,
        ]
    ):
        raise RuntimeError(
            "Missing informations. Ensure you set every required variables in "
            "the .env file."
        )

    return Configuration(
        event_name,
        event_description,
        int(user_mode),
        admin_username,
        admin_email,
        admin_password,
        theme_name,
        start_date,
        start_time,
        end_date,
        end_time,
    )
