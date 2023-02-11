from run_command import CommandHandler

import config

import os
import stat


class PermissionManager:
    """class that manages linux file permissions"""
    def __init__(self):
        self.logger = config.logger
        self.logger.info("create an instance of PermissionManager")
        self.command_handler = CommandHandler()

    def change_path_permissions(self, path: str, permissions: str):
        """change a file permission to the desired permission

        Args:
            permissions (str): permission desired like o+w or u-x
            path (str): path to change
        """
        self.logger.debug("change_path_permissions method from PermissionManager is called")
        self.logger.debug(f"permissions before changing: {stat.filemode(os.stat(path).st_mode)}")
        self.command_handler.run_shell_command_as_root(command=f"chmod {permissions} {path}")
        self.logger.debug(f"permissions after changing: {stat.filemode(os.stat(path).st_mode)}")
        self.logger.info(f"changed permission of {path}")

    


if __name__ == "__main__":
    path = "testing/permission_manager.txt"
    with open(path, 'w') as f:
        f.write("hello")
    permission_manager = PermissionManager()
    permission_manager.change_path_permissions(path, "o+w")
    os.remove(path)
        