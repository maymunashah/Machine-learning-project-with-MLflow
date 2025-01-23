# Machine-learning-project-with-MLflow


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/maymunashah/Machine-learning-project-with-MLflow
```
### STEP 01- Create an environment after opening the repository

```bash
python3 -m venv MLflowvenv
```

```bash
MLflowvenv\Scripts\activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)


linux
```bash
export MLFLOW_TRACKING_URI = https://dagshub.com/maymunashah/Machine-learning-project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME = 'maymunashah'
export MLFLOW_TRACKING_PASSWORD = 'your dagshub token'

```
on windows

```bash
set MLFLOW_TRACKING_URI = https://dagshub.com/maymunashah/Machine-learning-project-with-MLflow.mlflow

set MLFLOW_TRACKING_USERNAME = 'maymunashah'
set MLFLOW_TRACKING_PASSWORD = 'your dagshub token'
```


## workflows


1. Update config.yaml #done
2. Update schema.yaml 
3. Update params.yaml
4. Update the entity #data ingestion entity added
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py 


Project status

# data ingestion done
# data validation done
# Data Transformation done
# model trainer done
# model evaluation done






