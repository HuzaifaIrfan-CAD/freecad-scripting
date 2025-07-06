import sys
import os

DEFAULT_FREECAD_LIB_PATH='/home/admi/freecad-squashfs-root/usr/lib/'

# Load the .env file
from dotenv import load_dotenv
load_dotenv(override=True)

FREECAD_LIB_PATH = os.getenv("FREECAD_LIB_PATH", DEFAULT_FREECAD_LIB_PATH)
print(f"FREECAD_LIB_PATH at '{FREECAD_LIB_PATH}'")

sys.path.append(FREECAD_LIB_PATH)
