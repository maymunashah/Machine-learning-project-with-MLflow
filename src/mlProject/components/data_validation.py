from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir, sep=";")
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                
            return validation_status
        
        except Exception as e:
            raise e
        
        
    def validate_all_datatypes(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir, sep=";")
            data_column_types = {col: str(data[col].dtype) for col in data.columns}
            all_schema = self.config.all_schema

            for column in all_schema:
                if (column not in data_column_types) or (data_column_types[column]!=all_schema[column]):
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    return validation_status
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                
            return validation_status
        
        except Exception as e:
            raise e
        


