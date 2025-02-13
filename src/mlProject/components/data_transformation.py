from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig
import os


class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config


    def data_split(self):
        data = pd.read_csv(self.config.data_path, sep=";")

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Data splitted into train and test sets")
        logger.info(f"Train shape: {train.shape}, Test shape: {test.shape}")
