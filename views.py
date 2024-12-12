# views.py
from tasks import run_pipeline

def trigger_pipeline(pipeline_id, delay_seconds):
    # Trigger Celery task
    print(f"Pipeline {pipeline_id} scheduled to run after {delay_seconds} seconds.")
    task = run_pipeline(pipeline_id, int(delay_seconds))


trigger_pipeline(1234, 20)
