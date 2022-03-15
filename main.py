import dtcli


def main():
    # Parse (or use default) config file.
    dtcli.cfg = dtcli.config._load_config()

    # Launch the click cli.
    dtcli.cli.cli_root()


if __name__ == '__main__':
    main()
