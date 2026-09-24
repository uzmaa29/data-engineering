# Practical 6 – Setting Up Apache Airflow and Creating a DAG

## Objective
Configure an Apache Airflow DAG to run daily and execute sequential ETL tasks: start the pipeline, run the extraction script, and log successful completion.

## Project Structure
```text
Practical-7-Airflow-DAG/
├── README.md
├── requirements.txt
├── dags/
│   └── data_pipeline_dag.py
└── scripts/
    └── data_extraction.py
```

## Workflow
```text
start_pipeline
      ↓
run_extraction_script
      ↓
log_pipeline_success
```

## Setup
```bash
pip install -r requirements.txt
airflow db migrate
airflow standalone
```

Copy `dags/data_pipeline_dag.py` into your Airflow DAGs directory.

## Important
Update the `bash_command` in the DAG with the actual absolute path to `data_extraction.py` on your computer. The extraction script uses JSONPlaceholder and expects the location CSV file at the path used by the script.

## Expected Result
Airflow displays the `university_etl_orchestration` DAG. When triggered, the three tasks execute in order and the final task logs successful ETL completion.

## Conclusion
This practical demonstrates ETL workflow orchestration using Apache Airflow, DAG scheduling, and task dependencies.
