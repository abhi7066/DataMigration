# pipeline.py
import os
import time
import snowflake.connector
import logging
from logging.handlers import RotatingFileHandler


def run_pipeline(pipeline_id, delay_seconds):
    # Delay execution based on the provided seconds
    time.sleep(delay_seconds)

    # Set up logging
    Specify the log file path
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=5)
    log_handler.setFormatter(log_formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    # Your pipeline logic here
    logger.info(f"Running pipeline with ID: {pipeline_id}")
    logger.info(f"Loading data to Snowflake")


    # Snowflake connection details
    source_account = 'dummyacc'
    source_user = 'dummyuser'
    source_password = 'dummypass'
    source_database = 'EMPLOYEE'
    source_schema = 'PUBLIC'
    source_table = 'EMPDETAILS'

    target_account = 'dummyacc'
    target_user = 'dummyuser'
    target_password = 'dummypass'
    target_database = 'EMPLOYEE'
    target_schema = 'PUBLIC'

    # Establish connections
    source_conn = snowflake.connector.connect(
        user=source_user,
        password=source_password,
        account=source_account,
        database=source_database,
        schema=source_schema
    )

    target_conn = snowflake.connector.connect(
        user=target_user,
        password=target_password,
        account=target_account,
        database=target_database,
        schema=target_schema
    )

    # Get the schema of the source table
    source_cursor = source_conn.cursor()
    source_cursor.execute(f"DESCRIBE TABLE {source_table}")
    source_table_schema = source_cursor.fetchall()

    # Create the target table schema dynamically
    target_table_schema = ', '.join([f"{col[0]} {col[1]}" for col in source_table_schema])
    target_table_name = 'DEMO'

    # Create the target table dynamically
    target_cursor = target_conn.cursor()
    target_cursor.execute(f"CREATE OR REPLACE TABLE {target_table_name} ({target_table_schema})")

    # Insert data into the target table
    source_cursor.execute(f"SELECT * FROM {source_table}")
    source_data = source_cursor.fetchall()

    placeholders = ', '.join(['%s'] * len(source_table_schema))
    target_cursor.executemany(
        f"INSERT INTO {target_table_name} VALUES ({placeholders})",
        source_data
    )
    logger.info("Data loaded successfully!")
    target_conn.commit()

    # Close connections
    source_conn.close()
    target_conn.close()


    # Perform some operations
    result = "Operation completed successfully."
    logger.info(result)
    return result

if __name__ == "__main__":
    print("Container is running...")
    pipeline_id = os.environ.getlog_file = '/app/logs/pipeline.log'  # ("PIPELINE_ID")
    delay_seconds = int(os.environ.get("DELAY_SECONDS", "0"))
    result = run_pipeline(pipeline_id, delay_seconds)
    print(result)
