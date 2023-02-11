import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename="log/spam.log", mode="w")
file_handler.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

# formatter = logging.Formatter("%(asctime)s - module:%(module)s -> %(funcName)s -  %(levelname)s - %(message)s")
formatter = logging.Formatter("%(asctime)s  %(module)-20s -> %(funcName)-30s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M")
console.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file_handler)