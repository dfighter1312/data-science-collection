# Topic 12 - Experiment Tracking and Deployment on MLFlow

## What this repository do?

This is a short practice of MLFlow for experiment tracking and deploying models using MLFlow.

**The problem used for creating models:**
- Prediction of Wild Blueberry Yield (from [Kaggle](https://www.kaggle.com/competitions/playground-series-s3e14)) - using Machine Learning models.
- Electric Power Prediction - using Deep Learning lightweight models.
- Sentiment Analysis - using LLM.

**Functionalities explored with MLFlow:**
1. Experiment Tracking from Notebooks.
2. Serving Models.
3. Setting things up with a docker-compose file (all resources are on local).
4. Setting things up with a docker-compose file (all resources are on AWS).

## How to run this repository?

### Entering the topic folder

```bash
cd "Topic 12 - MLFlow"
```

### Installation

**Install MLFlow**

```bash
conda install mlflow
```

`pip` can be an alternative but I prefer `conda` for this project. Also, you should create a separate environment to run this folder to avoid conflicts by `conda create --name mlflow` then `conda activate mlflow` (install all packages if needed).

### Run the MLFlow UI

```bash
cd notebooks
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

You can log into [http://127.0.0.1:5000](http://127.0.0.1:5000) and see the UI has been set up.

You should see several experiments appear on the UI since I tested and instrumented those experiments. However, you can try to refresh by deleting `/mlruns` folder and `mlflow.db` under `/notebooks` folder, and run either `1-refactored.ipynb` or `2-refactored.ipynb`.

*Note that:*
- `1-refactored.ipynb` is a refactoring version of `1-prediction-of-wild-blueberry-yield.ipynb`.
- `2-refactored.ipynb` is a refactoring version of `2-electric-power-prediction.ipynb`.

The only difference between each pair of notebooks is that appearance of `mlflow` import and function calls relating to this library for logging and storing the model.

### Loading the model

Check out the code from `1-run-model.ipynb` as an example.

### Serving the model

**HTTP-based serving** 

This approach is suitable when you need fine-grained control over the serving implementation, want to customize endpoints, or have specific requirements that go beyond the standard MLflow REST API capabilities.

Run the command

```bash
python 1-serve-model.py
```
*If you have delete all the experiments, make sure to change the model URI in the source file.*

Then make a POST request to `localhost:4444/predict` with the following JSON sample:

```json
{
    "clonesize": 25.0,
    "honeybee": 0.25,
    "bumbles": 0.25,
    "andrena": 0.25,
    "osmia": 0.25,
    "MaxOfUpperTRange": 86.0,
    "MinOfUpperTRange": 52.0,
    "AverageOfUpperTRange": 71.9,
    "MaxOfLowerTRange": 62.0,
    "MinOfLowerTRange": 30.0,
    "AverageOfLowerTRange": 50.8,
    "RainingDays": 24.0,
    "AverageRainingDays": 0.39,
    "fruitset": 0.39936701,
    "fruitmass": 0.408088064,
    "seeds": 31.39456852,
    "fruit_seed": 12.537954960072526
}
```



Then it should return:

```json
{
    "prediction": [
        4288.038079081936
    ]
}
```

**REST API**

REST API serving with MLflow is recommended when you prefer a streamlined deployment process, want to leverage MLflow's model registry and versioning capabilities, and need built-in scalability features.

First, run the command 
```bash
mlflow models serve -m runs:/56c4a92a15b845aa8c1f4b65490ca228/sk_models -p 4444 --no-conda
```
*If you have delete all the experiments, make sure to change the model URI in the command, and custom the port (5000 if `-p` is not set) if you want.*

Then make a POST request to `localhost:5000/invocations` with the following JSON sample:
```bash
{
    "dataframe_records": [
        {
            "clonesize": 25.0,
            "honeybee": 0.25,
            "bumbles": 0.25,
            "andrena": 0.25,
            "osmia": 0.25,
            "MaxOfUpperTRange": 86.0,
            "MinOfUpperTRange": 52.0,
            "AverageOfUpperTRange": 71.9,
            "MaxOfLowerTRange": 62.0,
            "MinOfLowerTRange": 30.0,
            "AverageOfLowerTRange": 50.8,
            "RainingDays": 24.0,
            "AverageRainingDays": 0.39,
            "fruitset": 0.39936701,
            "fruitmass": 0.408088064,
            "seeds": 31.39456852,
            "fruit_seed": 12.537954960072526
        }
    ]
}
```

## Struggle and Derived Tips during implementation

To be updated

## References

- [MLFlow Documentation](https://mlflow.org/docs/latest/index.html).
- [Experiment Tracking by Anton T. Ruberts](https://www.youtube.com/watch?v=RnYa3QsXRAc).
- [Reproducible Experiment by Anton T. Ruberts](https://www.youtube.com/watch?v=l6oZJ8y9M1o).
- [Model Serving](https://towardsdatascience.com/mlflow-model-serving-bcd936d59052).
- [Deploying Large Language Models in Production: LLMOps with MLflow](https://medium.com/infinstor/serve-huggingface-sentiment-analysis-task-pipeline-using-mlflow-serving-dc302ecef130).
- [Deploy MLflow with docker compose](https://towardsdatascience.com/deploy-mlflow-with-docker-compose-8059f16b6039).