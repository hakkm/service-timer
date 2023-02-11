from file_manager import FileManager
import config

from dataclasses import dataclass


class ServiceManager:
    """Service class manages: create the service file"""
    def __init__(self, filename: str, command: str, description: str = ''):
        self.filename: str = filename
        # todo: set a default description: title or the first part of filename
        # todo: "title" service
        self.description = description 
        self.command = command
        self.logger = config.logger
        self.logger.info("create an instance of ServiceManager")

    def create_service_file(self):
        """
        Args:
            service_filename (str): with extension
            exec_start (str): command to run
        """
        self.logger.debug("create service file")
        self.file_manager = FileManager(self.filename)
        if not self.file_manager.is_file_exist():
            self.file_manager.create_file(content=self._get_service_text(self.command))
            self.logger.info("created service file")


    def _get_service_text(self, command: str):
        return f"""[Unit]
Description={self.description}


[Service]
ExecStart={command}
"""


if __name__ == "__main__":
    service_manager = ServiceManager(filename="test.service", command="gnome-screensaver-command -l")
    service_manager.create_service_file()