import os

import config
import window

from logs import Logout

if not os.path.exists(".\\logs"):
    os.mkdir(".\\logs")
ML = Logout("main", logs_file=True, logs_file_path=os.getcwd()+"\\logs", min_logs_level=0)


def main():
    try:
        ML.info("Initialize...")

        config.WINDOW = window.Window(ML)
        config.WINDOW.init()
        ML.debug("Config:\n"
                 f"{config.WIDTH=}\n"
                 f"{config.HEIGHT=}\n"
                 f"{config.BG_COLOR=}\n"
                 f"{config.WINDOW=}")

        while True:
            config.WINDOW.main_loop()
            if config.WINDOW.exit:
                break

        ML.info("Closed the window")
    except Exception as e:
        ML.fatal(f"The application was urgently closed by error: {e}")


if __name__ == '__main__':
    main()
