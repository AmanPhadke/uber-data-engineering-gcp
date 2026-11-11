from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    for key, value in data.items():
        table_id = 'project-de87dcc2-655f-4411-b80.uber_data_engineering.{}'.format(key)
    
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )

# # @data_exporter
# # def export_data_to_big_query(data, **kwargs):

# #     print("Data type:", type(data))
# #     print("Data received:", data)

# #     if isinstance(data, dict):
# #         print("Keys:", data.keys())
# #     elif isinstance(data, DataFrame):
# #         print("Columns:", data.columns.tolist())

# from mage_ai.settings.repo import get_repo_path
# from mage_ai.io.bigquery import BigQuery
# from mage_ai.io.config import ConfigFileLoader
# from pandas import DataFrame
# from os import path

# if 'data_exporter' not in globals():
#     from mage_ai.data_preparation.decorators import data_exporter


# @data_exporter
# def export_data_to_big_query(data, **kwargs):

#     print("STEP 1: Exporter started", flush=True)

#     table_id = 'project-de87dcc2-655f-4411-b80.uber_data_engineering.fact_table'

#     print("STEP 2: Preparing DataFrame", flush=True)

#     df = DataFrame(data['fact_table'])

#     print("STEP 3: DataFrame created", flush=True)
#     print("Shape:", df.shape, flush=True)
#     print("Columns:", df.columns.tolist(), flush=True)

#     config_path = path.join(get_repo_path(), 'io_config.yaml')
#     config_profile = 'default'

#     print("STEP 4: Loading BigQuery configuration", flush=True)

#     config = ConfigFileLoader(config_path, config_profile)

#     print("STEP 5: Starting BigQuery export", flush=True)

#     BigQuery.with_config(config).export(
#         df,
#         table_id,
#         if_exists='replace',
#     )

#     print("STEP 6: Export completed!", flush=True)