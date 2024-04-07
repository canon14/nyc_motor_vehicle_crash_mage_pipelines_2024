CREATE OR REPLACE TABLE zoomcamp-final-project.nyc_vc_stg.nyc_vc_2022_2023_partitioned_clustered
PARTITION BY DATE(crash_timestamp)
CLUSTER BY collision_id AS
SELECT * FROM zoomcamp-final-project.nyc_vc_stg.nyc_vc_2022_2023;
