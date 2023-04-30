import os
# from . import config


SYSTEMD_SYSTEM_DIR = r"/etc/systemd/system"


class FileManager:
    """Class contains methods to manage files in the /etc/systemd/system
    directory"""

    def __init__(self, filename: str):
        # self.logger = config.get_logger(__name__)
        # self.logger.info("create instance of FileManager")

        self.filename = filename

    @property
    def file_full_path(self):
        # todo: try using another folder like systemd/system/salat
        return f"{SYSTEMD_SYSTEM_DIR}/{self.filename}"

    def create_file(self, content):
        """Create a file at /etc/systemd/system/ and add write permission to it

        Args:
            content (string): what to write at /etc/systemd/system/$filename
        """
        # add write permission to /etc/systemd/system

        # create the file
        with open(f"{self.file_full_path}", "w") as service_file:
            service_file.write(content)
            # self.logger.debug("create and fill file")
            # change permission of file to writable

        # change /etc/systemd/system permission to it's origin
        # self.logger.info(f"created {self.file_full_path} successfully")

    def is_file_exist(self):
        if os.path.exists(f"{SYSTEMD_SYSTEM_DIR}/{self.filename}"):
            return True
        else:
            return False


if __name__ == "__main__":
    file_manager = FileManager("ztest.txt")
    file_manager.create_file("hello world")
