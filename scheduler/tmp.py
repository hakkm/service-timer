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