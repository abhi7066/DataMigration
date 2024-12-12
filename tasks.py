# tasks.py
from celery import shared_task
import subprocess
import os

@shared_task
def run_pipeline(pipeline_id, delay_seconds):
    cwd = os.getcwd()  # Get the current working directory
    host_logs_path = os.path.join(cwd, "logs")  # Construct the absolute path

    # Trigger Docker container to run pipeline
    subprocess.run([
        "docker", "run", "--rm",
        "-v", f"{host_logs_path}:/app/logs",
        "-e", f"PIPELINE_ID={pipeline_id}",
        "-e", f"DELAY_SECONDS={delay_seconds}",
        "pipeline_image"
    ])


    # subprocess.run([
    #     "docker", "run", "--rm",
    #     "-v /path/on/host:/app/logs",
    #     "-e", f"PIPELINE_ID={pipeline_id}",
    #     "-e", f"DELAY_SECONDS={delay_seconds}",
    #     "pipeline_image"
    # ])
    # return "Pipeline execution completed"
