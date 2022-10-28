# disruptive-cli
Unofficial Command-Line Interface (CLI) for the Disruptive Technologies (DT) API.

- [DT REST API](https://developer.disruptive-technologies.com/api)
- [DT Python API](https://developer.disruptive-technologies.com/api/libraries/python/)
- [DT Developer Documentation](https://developer.disruptive-technologies.com/docs/)

## Installation
The package is hosted on PyPI and is available through pip.
```bash
pip install --upgrade disruptive-cli
```

Supports Python 3.7+.

## Authentication
Using [Service Account](https://developer.disruptive-technologies.com/docs/service-accounts/introduction-to-service-accounts) credentials, set the following environment variables.
```bash
export DT_SERVICE_ACCOUNT_KEY_ID="<SERVICE_ACCOUNT_KEY_ID>"
export DT_SERVICE_ACCOUNT_SECRET="<SERVICE_ACCOUNT_SECRET>"
export DT_SERVICE_ACCOUNT_EMAIL="<SERVICE_ACCOUNT_EMAIL>"
```

## Usage
Call the `dt` command using a `dt NOUN VERB` syntax.

- List all available projects.
```bash
dt project list
```

- Get a single device.
```bash
dt device get <DEVICE_ID>
```

See `dt -h` for additional commands.

## Formatting
A tabular human readable output is prioritized.

### Headers
Column headers are removed for single columns or if the `--no-header` flag is provided. 

### Filters
A select set of columns are shown per resource. Use the `--full` flag to output all available information.

On the other hand, the `--include` can be used to include only specified columns in output.

### Other Filetypes
The following formats are supported.
- `--json`
- `--csv`
- `--tsv`

## Chaining Commands
Pipes are supported using the `-` symbol to make chaining commands simpler.

The following example lists all projects, then pipes the `project-id` column to the `serviceaccount` command to list all available Service Accounts per project. The output is formatted as `.json` and piped into [jq](https://stedolan.github.io/jq/) for further processing.

```bash
dt project list --include project-id | dt serviceaccount list - --json | jq
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
