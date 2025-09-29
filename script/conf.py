# Set number of core. * will takes all the available cores.
CORE = "3"

# Set Path where data files are located
BASE_PATH = "../data/"

# Input data:
#######################################################
# Set Input File name for raw data step - merged
RAW_FILE_PATH = "MPD_sample_synthetic_kenya_3001subs.csv"

# Define the path to the raw MPD subs records file - In case you have two files that need to be merged, add the files here: 
RAW_SUBS_PATH = "MPD_sample_records.csv"

# Define the path to the raw MPD cells file  - In case you have two files that need to be merged, add the files here: 
RAW_CELLS_PATH = "MPD_sample_cells.csv"

# Set a variable GEOJSON_FILE to the file path "../data/geoBoundaries-KEN-ADM3_simplified.geojson". Please custom this path based on your own adminstrative dataset.
GEOJSON_FILE = "../data/geoBoundaries-KEN-ADM3_simplified.geojson"
MUNICIPALITY_FIELD_NAME = 'shapeName'

# Set configuration for sanity check
#######################################################
SANITY_PATH = "../data/01_RAW"
SANITY_FILE_PATH = RAW_FILE_PATH.replace(".csv","_sanity.jsonl")

# Set configuration for pre-processing
#######################################################

# Define a dictionary containing configuration parameters for filtering
RAW_CONF = {"ROBOT_THRESHOLD": 500, "RANDOM_EVENT_THRESHOLD": 1, "TOURIST_THRESHOLD": 7}

# Define the path to the filtered MPD file in Parquet format
FILTERED_FILE_PATH_PARQUET = "MPD_sample_synthetic_filtered"

# Define the path to the filtered MPD file in CSV format
FILTERED_FILE_PATH_CSV = "MPD_sample_synthetic_csv"

# Set configuration for QA
#######################################################

# Set a variable QA_PATH to the directory path "../data/02_QA/"
QA_PATH = "../data/02_QA/"

# Set Input File name for QA step
QA_FILE_PATH = "MPD_sample_synthetic_filtered"

# define expected distribution with elephant shape. Reference: https://proceedings.stis.ac.id/icdsos/article/view/134
# It's important to note that the diurnal distribution given here is based on general behavior patterns observed in Indonesia.
# However, it's worth noting that this pattern can vary across different cultures and regions.
# Therefore, it's recommended to modify the diurnal distribution according to specific country behavior to better understand how people structure their day and behave in different parts of the world.
DIURNAL_REFERENCE = [
    0.55,
    0.37,
    0.35,
    0.33,
    0.35,
    0.42,
    0.6,
    0.78,
    0.97,
    1.0,
    0.98,
    0.94,
    0.93,
    0.93,
    0.91,
    0.92,
    0.91,
    0.87,
    0.85,
    0.83,
    0.8,
    0.66,
    0.58,
    0.6,
]

# The following code initializes two dictionaries:
# 1. CONF dictionary contains the different thresholds used in the quality assurance (QA) process.
# 2. QA_summary dictionary contains the status and report of each QA test.

# Initialize the CONF dictionary with the given threshold values
QA_CONF = {
    "NULL_MAX_THRESHOLD": 5,
    "SUBS_MIN_THRESHOLD": 0.8,
    "CELL_MIN_THRESHOLD": 0.5,
    "CELL_OOB_MAX_THRESHOLD": 0.05,
    "ACTIVE_DAY_SKEWNESS_THRESHOLD": -0.5,
    "DIURNAL_DISTRIBUTION_REFERENCE": DIURNAL_REFERENCE,
    "DIURNAL_DISTRIBUTION_PVALUE": 0.05,
}

# Initialize the QA_summary dictionary with not run and unknown as the status and report for each QA test
QA_summary = {
    "USER_STATS_REPORT": ("NOT RUN", "UNKNOWN"),
    "NULL_REPORT": ("NOT RUN", "UNKNOWN"),
    "USER_CONSISTENCY_REPORT": ("NOT RUN", "UNKNOWN"),
    "CELL_CONSISTENCY_REPORT": ("NOT RUN", "UNKNOWN"),
    "CELL_LOCATION_REPORT": ("NOT RUN", "UNKNOWN"),
    "ACTIVE_DAY_DISTRIBUTION_REPORT": ("NOT RUN", "UNKNOWN"),
    "DIURNAL_DISTRIBUTION_REPORT": ("NOT RUN", "UNKNOWN"),
}


QA_action_plan = {
    "USER_STATS_REPORT": "Review the subscriber counts and compare them with the expected values.\nEnsure that the counts are accurate and consistent.\nIf any discrepancies or inconsistencies are found, investigate the cause and take corrective measures.",
    "NULL_REPORT": "Investigate the cause of null values and take steps to reduce them.\nThis may involve improving data collection processes, addressing data quality issues, or updating data handling mechanisms.\nSee attached image '2_null_percentages.png' for the visualization.",
    "USER_CONSISTENCY_REPORT": "Investigate the causes behind these inconsistencies, such as data processing errors, data loss, or any other factors.\nReview the data collection and processing procedures to address and rectify these inconsistencies.\nSee attached image '3_number_of_subscribers_daily.png' for the visualization.",
    "CELL_CONSISTENCY_REPORT": "Investigate the reasons behind this instability.\nCheck for any issues related to cell tower coverage, data transmission, or data aggregation.\nCollaborate with the network operations team to rectify any issues and ensure accurate and stable cell counts.\nSee attached image '4_number_of_cells_daily.png' for the visualization.",
    "CELL_LOCATION_REPORT": "Review the cell locations outside the mainland and determine if they are expected or indicate potential issues.\nIf these locations are unexpected or problematic, investigate the causes and take appropriate actions to rectify the situation.\nEnsure that cell location data aligns with the designated coverage area.\nSee attached file '5_cell_administrative_location.csv' for the list of cell location.",
    "ACTIVE_DAY_DISTRIBUTION_REPORT": "Further investigation is required to analyze the aspect of data completion and subscribers filtering.\nExamine the possibility of anomaly subscribers or incomplete data that may have contributed to the observed deviation from the ideal distribution.\nReview the data collection and filtering processes to ensure that only valid and complete data is included in the analysis.\nSee attached image '6_active_day_distribution_of_subscribers.png' for the visualization.",
    "DIURNAL_DISTRIBUTION_REPORT": "Analyze the diurnal distribution patterns from CDR and IPDR data and investigate the reasons for the deviation from the expected elephant shape.\nThis may involve examining user behavior, network usage patterns, or potential issues with data format like incorrect timezone.\nTake appropriate actions to address any discrepancies and ensure accurate diurnal distribution reporting.\nSee attached image '7_diurnal_distribution_of_subscribers_activity.png' for the visualization.",
}

# Set configuration for anchoring
#######################################################

# Set a variable ANCHOR_PATH to the directory path "../data/03_Anchoring/"
ANCHOR_PATH = "../data/03_Anchoring/"

# Initialize the CONF dictionary for setting hour reference for anchoring process
ANCHOR_CONF = {
    "weekday": ["Monday", "Tuesday", "Wednesday", "Thursday"],
    "ANCHOR_1": [0, 5],
    "ANCHOR_2": [5, 8],
    "ANCHOR_3": [21, 24],
}

# Set configuration for indicator
#######################################################

INDICATOR_PATH = "../data/04_Indicator/"

INDICATOR_ZONE_PATH = "MPD_sample_synthetic_zone_kenya.csv"

INDICATOR_CRM_PATH = "MPD_sample_synthetic_CRM_kenya.csv"
