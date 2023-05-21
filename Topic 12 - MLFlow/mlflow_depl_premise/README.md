# Deploying MLFlow on premise

## Architecture

The deployment architecture is equivalent to Scenario 4 from the [MLFlow Documentation](https://mlflow.org/docs/latest/tracking.html).

![Scenario 4](scenario_4.png)

To the best of my knowledge, S3 remote host is used for storing model artifacts, while the remote host is used for storing metadata to display to the tracking UI (metrics, tags, logs, filepath, etc.)

In this folder, we will be using: 
- MinIO S3 as the S3 remote host for storing artifacts
- MySQL as the backend storage remote host (instead of PostgreSQL)

## Reading

Accessing `docker-compose.yml`, you will see the appearance of 4 services: `minio`, `mc`, `db` and `web`.

- `minio` is the service for MinIO storage. You will see the usage of 2 ports: 9000 and 9001. And they are declared in the command as console address and address, respectively. Particularly, the console-address option determines the address and port for accessing the MinIO console interface, while the address option specifies the address and port on which the MinIO server API endpoints are available for programmatic interaction.
- `mc` (MinIO Client) acts as a boto3 client in the above figure, which provides a modern alternative to UNIX commands supporting filesystems and Amazon S3 compatible cloud storage service. You should notice that there is a file `wait-for-it.sh` that wait until MinIO storage is on, if not, this service cannot run.
- `db` is the service for backend storage (MySQL).
- `web` is the service for MLFlow server. You can see the configuration for building image for this service is shown inside the `mlflow` repository. The image only requires to install 4 packages: cryptography, boto3, mlflow, and pymysql.
