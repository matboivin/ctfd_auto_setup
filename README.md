# Automatically setup CTFd instance

Just being lazy.

## Requirements

* Python 3.9 or greater
* [`poetry`](https://python-poetry.org)

## Installation

1. Clone the repository and change it to your working directory.

  ```console
  $ poetry install
  $ source `poetry env info --path`/bin/activate
  $ playwright install
  ```

2. Set the required variables in a `.env` file (see `env.sample` at the root of the repository).

## Usage

```sh
ctfd_setup [-h] [-d] [--url URL] [-t TIMEOUT]

Automatically setup CTFd instance.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Run headful browser with a slowmo
  --url URL             URL of the CTFd (default: http://localhost:8000)
  -t TIMEOUT, --timeout TIMEOUT
                        default maximum navigation time in milliseconds (default: 30000)
```

# Credits

- [CTFd](https://github.com/CTFd/CTFd) (Logo by Laura Barbera, Theme by Christopher Thompson, Notification Sound by Terrence Martin), under [Apache License
Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)