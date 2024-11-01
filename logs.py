import datetime

from colorama import Fore


class Logout:
    LOG_LEVELS = [
        "DEBUG",
        "INFO",
        "WARN",
        "ERROR",
        "FATAL"
    ]
    LOG_COLORS = [
        Fore.WHITE,
        Fore.LIGHTGREEN_EX,
        Fore.YELLOW,
        Fore.RED,
        Fore.LIGHTRED_EX
    ]

    def __init__(self,
                 logout_name: str,
                 min_logs_level: int = 0,
                 log_format: str = "[level] [time] (name): description",
                 logs_file: bool = False,
                 logs_file_path: str = "."):
        """
        :param logout_name: name of logout
        :param min_logs_level: 0 - debug, 1 - info, 2 - warn, 3 - error, 4 - fatal
        :param log_format: level - log level, time - log time, name - logout name, description - description of log
        :param logs_file: if True create log.txt
        :param logs_file_path: log file path
        """
        if logs_file:
            open(f"{logs_file_path}\\logs_{logout_name}_{self.__get_time()}.txt", "w").close()

        self.__name = logout_name
        self.__log_format = log_format
        self.__logs_file = logs_file
        self.__logs_file_path = f"{logs_file_path}\\logs_{logout_name}_{self.__get_time()}.txt"
        self.__min_logs_level = min_logs_level

    @staticmethod
    def __get_time(format_: str = "%Y%m%d%H%M%S") -> str:
        return datetime.datetime.now().strftime(format_)

    @classmethod
    def __get_color(cls, level: int) -> str:
        return cls.LOG_COLORS[level]

    def __create_log(self, level: int, description: str) -> str:
        if level >= self.__min_logs_level:
            log = self.__log_format.replace("level", self.LOG_LEVELS[level]).replace("time",
                  self.__get_time("%Y-%m-%d %H:%M:%S")).replace("name", self.__name).replace("description",
                                                                                             description)
            if self.__logs_file:
                with open(self.__logs_file_path, "a", encoding="utf-8-sig") as file:
                    file.write(log + "\n")
            print(f"{self.__get_color(level)}{log}")
            return log

    def debug(self, description: str) -> str:
        """Creates debugging logs"""
        return self.__create_log(0, description)

    def info(self, description: str) -> str:
        """Creates informative logs"""
        return self.__create_log(1, description)

    def warn(self, description: str) -> str:
        """Creates warning logs"""
        return self.__create_log(2, description)

    def error(self, description: str) -> str:
        """Creates error logs"""
        return self.__create_log(3, description)

    def fatal(self, description: str) -> str:
        """Creates critical error logs"""
        return self.__create_log(4, description)
