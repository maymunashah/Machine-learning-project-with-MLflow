from dataclasses import dataclass
from pathlib import Path

# this entity is for my return type, i.e how i want my config infor to be returned as
@dataclass(frozen=True)
class DataIngestionConfig():
    root_dir: Path
    source_URL:str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    unzip_data_dir:Path
    STATUS_FILE:str
    all_schema: dict

    


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir:Path
    data_path:Path

    

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    train_data_path:Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str



@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir:Path
    test_data_path:Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str
