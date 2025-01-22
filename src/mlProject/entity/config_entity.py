from dataclasses import dataclass
from pathlib import Path

# this entity is for my return type, i.e how i want my config infor to be returned as
@dataclass(frozen=True)
class DataIngestionConfig():
    root_dir: Path
    source_URL:str
    local_data_file: Path
    unzip_dir: Path
