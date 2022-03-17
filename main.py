import dtcli.cli
import dtcli.config


def main():
    # Parse (or use default) config file.
    dtcli.cfg = dtcli.config._load_config()

    # Launch the click cli.
    dtcli.cli.entry_point()


if __name__ == '__main__':
    main()
