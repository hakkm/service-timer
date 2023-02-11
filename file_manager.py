# todo: i want to add a PermissionManager class but it needs more
# todo: customization to _save_origin....
# todo:
import os
from dataclasses import dataclass
from permission_manager import PermissionManager


@dataclass
class FileManager:
    """Class contains methods to manage files in the /etc/systemd/system directory"""

    SYSTEMD_SYSTEM_DIR = r"etc/systemd/system"

    file_name: str  # should be with extension
    # todo: move this permission manager to create_file method
    permission_manager: PermissionManager = PermissionManager()

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
        self.permission_manager.change_path_permissions(self.SYSTEMD_SYSTEM_DIR, "o+w")

        # create the file
        with open(f"{self.file_full_path}", "w") as service_file:
            service_file.write(content)

        # change /etc/systemd/system permission to it's origin
        self.permission_manager.change_path_permissions(
            self.SYSTEMD_SYSTEM_DIR, self.origin_systemd_writable_permission
        )

    def is_file_exist(self):
        if os.path.exists(f"{self.SYSTEMD_SYSTEM_DIR}/{self.file_name}"):
            return True
        else: return False


if __name__ == "__main__":
    file_manager = FileManager("najal.txt")
    file_manager.create_file("hello world")
