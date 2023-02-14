import argparse
import boto3

from utils.utils import (
    get_report_dates_from_target_date,
    run_athena_query_using_template,
    output_results_list_to_csv_file,
)

"""
Summary:

Program to test out Athena SQL template for development.

This can be used when adding new metrics. It runs the SQL given the
template parameters on the command line and DOES NOT updated the related
reporting table. See README.md for usage examples.

"""
# import dateutil.parser
# from csv import reader

parser = argparse.ArgumentParser(
    description="Utility script to test out Athena SQL template for development."
)
parser.add_argument(
    "--input-template-file",
    "-i",
    help="The name of the input template file.",
    required=True,
    type=str,
)
parser.add_argument(
    "--region",
    "-r",
    help="The Athena AWS region.",
    default="us-east-1",
    type=str,
)
parser.add_argument(
    "--workgroup",
    "-w",
    help="The AWS Glue table workgroup.",
    default="bb2",
    type=str,
)
parser.add_argument(
    "--database",
    "-d",
    help="The AWS Glue table database.",
    default="bb2",
    type=str,
)
parser.add_argument(
    "--env",
    "-e",
    help="The BB2 environment (prod/impl/test).",
    required=True,
    type=str,
)
parser.add_argument(
    "--target-report-date",
    "-t",
    help="The target report date/week. EX: 2023-01-23",
    required=True,
    type=str,
)
parser.add_argument(
    "--results-output-file",
    "-o",
    help="The output file to write Athena SQL query results to.",
    default="",
    type=str,
)
parser.add_argument(
    "--basename_per_app",
    "-b",
    help="The per-app table basename, if used in query tested.",
    default="global_state_per_app_testing1",
    type=str,
)

args = parser.parse_args()

INPUT_TEMPLATE_FILE = args.input_template_file if args.input_template_file else None
REGION = args.region if args.region else None
WORKGROUP = args.workgroup if args.workgroup else None
DATABASE = args.database if args.database else None
ENV = args.env if args.env else None
TARGET_DATE = args.target_report_date if args.target_report_date else None
OUTPUT_FILE = args.results_output_file if args.results_output_file else None
BASENAME_PER_APP = args.basename_per_app if args.basename_per_app else None

print("--- Running SQL from template in Athena...")
print("---")
print("---Check recent-queries in the AWS console Athena Query Editor for results.")
print("---Or use the -o option to output to a file locally.")
print("---")
print("---Using the following parameters:")
print("---")
print("---  INPUT_TEMPLATE_FILE: ", INPUT_TEMPLATE_FILE)
print("---               REGION: ", REGION)
print("---            WORKGROUP: ", WORKGROUP)
print("---             DATABASE: ", DATABASE)
print("---                  ENV: ", ENV)
print("---          TARGET_DATE: ", TARGET_DATE)
print("---     BASENAME_PER_APP: ", BASENAME_PER_APP)
print("---          OUTPUT_FILE: ", OUTPUT_FILE)
print("---")

session = boto3.Session()

target_week_date = TARGET_DATE
report_dates = get_report_dates_from_target_date(target_week_date)

params = {
    "region": REGION,
    "workgroup": WORKGROUP,
    "database": DATABASE,
    "env": ENV,
    "basename_main": None,
    "basename_per_app": BASENAME_PER_APP,
    "report_dates": report_dates,
}

print("---")
print("---")
print("--- params:  ", params)
print("---")
print("---")

result_list = run_athena_query_using_template(session, params, INPUT_TEMPLATE_FILE)

print("--- Results list items returned:  ", len(result_list))

if OUTPUT_FILE:
    print("---")
    print("--- Writing results to:  ", OUTPUT_FILE)
    output_results_list_to_csv_file(result_list, OUTPUT_FILE)
    print("---")
