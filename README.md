# disruptive-cli
Unofficial Command-Line Interface (CLI) for the Disruptive Technologies REST API.

## Authentication
Currently, the only way of authenticating is by setting the following environment variables.
```bash
export DT_SERVICE_ACCOUNT_KEY_ID="<SERVICE_ACCOUNT_KEY_ID>"
export DT_SERVICE_ACCOUNT_SECRET="<SERVICE_ACCOUNT_SECRET>"
export DT_SERVICE_ACCOUNT_EMAIL="<SERVICE_ACCOUNT_EMAIL>"
```

## Usage
The CLI is structured in a `<NOUN>` -> `<VERB>` format.

- Fetch a single device.
```bash
dt device get <DEVICE_ID>
```

- Fetch all devices in a project.
```bash
dt device list <PROJECT_ID>
```

## Development
Virtualenv is used for dependency isolation, wrapped by the following commands.

- Build the distribution:
```bash
make build
```

- Remove build-files:
```bash
make clean
```
