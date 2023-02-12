
# todo: customization to _save_origin....
import config
from permission_manager import PermissionManager

import os
import logging

class FileManager:
    """Class contains methods to manage files in the /etc/systemd/system directory"""

    SYSTEMD_SYSTEM_DIR = r"/etc/systemd/system"
    
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.logger: logging.Logger = config.logger
        self.logger.info("create instance of FileManager")

        self.permission_manager: PermissionManager = PermissionManager()

    @property
    def file_full_path(self):
        return f"{self.SYSTEMD_SYSTEM_DIR}/{self.file_name}"

    def _save_origin_systemd_writable_permission(self):
        """save the origin directory permissions in origin_directory_permission"""
        if os.access(self.SYSTEMD_SYSTEM_DIR, os.W_OK):
            self.origin_systemd_writable_permission = "o+w"
        else:
            self.origin_systemd_writable_permission = "o-w"

    def create_file(self, content):
        """Create a file at /etc/systemd/system/

        Args:
            filename (string): filename with extension
            content (string): what to write at /etc/systemd/system/$filename
        """

        self._save_origin_systemd_writable_permission()

        # add write permission to /etc/systemd/system
        self.logger.debug(f"change permission to writable of {self.SYSTEMD_SYSTEM_DIR}")
        self.permission_manager.change_path_permissions(self.SYSTEMD_SYSTEM_DIR, "o+w")
        self.logger.debug(f"changed permission to writable of {self.SYSTEMD_SYSTEM_DIR}")

        # create the file
        with open(f"{self.file_full_path}", "w") as service_file:
            service_file.write(content)
            self.logger.debug("create and fill file")
            # change permission of file to writable
            self.permission_manager.change_path_permissions(
                self.file_full_path,
                'o+w'
            )

        

        # change /etc/systemd/system permission to it's origin
        self.logger.debug(f"change permission back of {self.SYSTEMD_SYSTEM_DIR}")
        self.permission_manager.change_path_permissions(
            self.SYSTEMD_SYSTEM_DIR, self.origin_systemd_writable_permission
        )
        self.logger.debug(f"changed permission back of {self.SYSTEMD_SYSTEM_DIR}")
        self.logger.info(f"created {self.file_full_path} successfully")

    def is_file_exist(self):
        if os.path.exists(f"{self.SYSTEMD_SYSTEM_DIR}/{self.file_name}"):
            return True
        else: return False


if __name__ == "__main__":
    file_manager = FileManager("najal.txt")
    file_manager.create_file("hello world")
    os.remove(file_manager.file_full_path)