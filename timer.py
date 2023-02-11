from file_manager import FileManager
from service import ServiceManager
from run_command import CommandHandler 
import config

from datetime import datetime

class TimerManager:
    """_summary_

    Args:
        service_manager (ServiceManager): service manager instance linked to
        to this timer instance
        description (str): timer_description
    """
    def __init__(self, filename:str, on_calendar: str, service_manager: ServiceManager,description: str = '') -> None:
        self.logger = config.logger
        self.logger.info("created instance of TimerManager")

        self.filename = filename
        self.description = description
        self.on_calendar = on_calendar
        self.service_manager: ServiceManager = service_manager

        self.file_manager = FileManager(file_name=self.filename)
        self.command_handler = CommandHandler()


    def create_activate_timer(self):
        self.logger.debug(f"create timer file {self.filename}")
        self.file_manager.create_file(self._get_timer_text())
        self.logger.debug(f"created timer file {self.filename}")


    def _get_timer_text(self):
        return f"""[Unit]
Description={self.description}

[Timer]
OnCalendar={self.on_calendar}
Unit={self.service_manager.filename}

[Install]
WantedBy=multi-user.target
"""

    def start_timer(self):
        # reload daemon process
        self.logger.debug("reload daemon process")
        self.command_handler.run_shell_command_as_root("systemctl daemon-reload")
        # start timer
        self.logger.debug("start timer")
        self.command_handler.run_shell_command_as_root(f"systemctl start {self.filename}")

        self.logger.debug("enable timer")
        self.command_handler.run_shell_command_as_root(f"systemctl enable {self.filename}")

        self.logger.info("timer is set successfully")

if __name__ == '__main__':
    