# Automatically setup CTFd instance

Set environment variables. Run the script. Be lazy.

## Requirements

* Python >= 3.9
* [`Poetry`](https://python-poetry.org)

## Installation

1. Clone the repository and change it to your working directory.

2. Install the project:
  ```console
  $ poetry install
  ```
 
3. Activate the virtual environment:
  ```console
  $ poetry shell
  ```

4. Install the web browsers:
  ```console
  $ playwright install
  ```

5. Set the required variables in a `.env` file at the root of the repository.
  ```
  EVENT_NAME=
  EVENT_DESCRIPTION=
  USER_MODE=   # 0 | 1
  ADMIN_USERNAME=
  ADMIN_EMAIL=
  ADMIN_PASSWORD=
  THEME_NAME=  # the only optional parameter, default: "core"
  START_DATE=  # "yyyy-mm-dd"
  START_TIME=  # "hh:mm" in 24hrs format
  END_DATE=    # "yyyy-mm-dd"
  END_TIME=    # "hh:mm" in 24hrs format
  ```

## Usage

```console
ctfd_setup [-h] [-d] [--url URL] [-t TIMEOUT]

Automatically setup CTFd instance.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Run headful browser with a slowmo
  --url URL             URL of the CTFd (default: http://localhost:8000)
  -t TIMEOUT, --timeout TIMEOUT
                        default maximum navigation time in milliseconds (default: 30000)
```

1. Activate the virtual environment:
  ```console
  $ poetry shell
  ```

2. Run the project:

  ```console
  $ ctfd_setup
  ```

# Credits

- [CTFd](https://github.com/CTFd/CTFd) (Logo by Laura Barbera, Theme by Christopher Thompson, Notification Sound by Terrence Martin), under [Apache License
Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
