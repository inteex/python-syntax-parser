from dotenv import load_dotenv
import os

load_dotenv()

build_directory = os.getenv("BUILD_DIRECTORY")
file_name = os.getenv("FILE_NAME")