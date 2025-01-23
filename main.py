from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from dotenv import load_dotenv

load_dotenv()


STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f" *********** stage {STAGE_NAME} started  **********")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" *********** stage {STAGE_NAME} completed *********\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"******* stage {STAGE_NAME} started *********")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"******* stage {STAGE_NAME} completed *********\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"******* stage {STAGE_NAME} started *********")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"******* stage {STAGE_NAME} completed *********\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Training Stage"


try:
    logger.info(f"******* stage {STAGE_NAME} started *********")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f"******* stage {STAGE_NAME} completed *********\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"


try:
    logger.info(f"******* stage {STAGE_NAME} started *********")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f"******* stage {STAGE_NAME} completed *********\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e