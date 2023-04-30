from dataclasses import dataclass
# from . import config

import subprocess


@dataclass
class CommandHandler:
    # logger = config.get_logger(__name__)
    # logger.info("create instance of CommandHandler")

    def run_shell_command(self, command: str):
        """ run shell command simple usage"""
        # self.logger.debug("run_shell_command() func is called")
        process = subprocess.run(
            [f"{command}"],
            shell=True,
            capture_output=True,
            encoding="utf-8",
            timeout=6,
        )
        # self.logger.debug(
        #     f"process is created: stdout: {process.stdout} || stderr: {process.stderr}"
        # )
        return process


if __name__ == "__main__":
    ch = CommandHandler()
    print(ch.run_shell_command("sudo mkdir -p /mnt/delete"))
