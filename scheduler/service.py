from file_manager import FileManager
import config

import os

class ServiceManager:
    """Service class manages: create the service file
    Args: 
        filename (string): name of the service file with extension
        command (string): command to run
    """
    def __init__(self, filename: str, command: str, description: str = '', overwrite: bool = False):
        self.filename: str = filename
        # todo: set a default description: title or the first part of filename
        # todo: "title" service
        self.description = description 
        self.command = command
        self.overwrite = overwrite

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
        if self.file_manager.is_file_exist():
            if not os.access(self.file_manager.file_full_path, os.W_OK):
                self.logger.error(f"{self.filename} is a system file. try another service name or title")
                raise PermissionError(f"{self.filename} is a system file. try another service name or title")
            else:
                if self.overwrite:
                    self.file_manager.create_file(content=self._get_service_text())
                    self.logger.info("created service file")
                else:
                    self.logger.error(f"you can't overwrite {self.filename}. try another service filename, or you can overwrite by setting overwrite to True")
                    raise Exception(f"You can't overwrite {self.filename}. Already existed. you can overwrite it by setting overwrite to True.")
        else:
            self.file_manager.create_file(content=self._get_service_text())
            self.logger.info("created service file")

    def _get_service_text(self):
        return f"""[Unit]
Description={self.description}


[Service]
ExecStart={self.command}
"""


if __name__ == "__main__":
    service_manager = ServiceManager(filename="test.service", command="gnome-screensaver-command -l")
    service_manager.create_service_file()