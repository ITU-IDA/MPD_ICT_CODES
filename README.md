[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Flowminder/MPD_ICT_CODES?quickstart=1)

# Mobile Positioning Data for Estimating SDGs Indicator: Proportion of the Population Using the Internet
This project aims to estimate the proportion of the population using the internet by leveraging mobile positioning data (MPD). The project consists of several notebooks that process raw MPD, provide quality assurance of MPD, determine home locations of subscribers, and calculate the proportion of the population using the internet.

## Disclaimer
The codes in the Github repo are under the copyright rules of the ITU. Please contact us (indicators@itu.int) before sharing the codes with other users or if there is any interest from other parties in using the codes.

## Introduction 
The Jupyter Notebook series are written in PySpark and serves as a practical guide for statisticians and data scientists on how to prepare and process mobile phone data (CDRs) to calculate one of the information society indicators (proportion of individuals using the Internet). 

There are several Notebooks, each focused on one specific area of the data process. The Notebooks included are:

### 1. Setup instructions:
Instructions on how to setup the technical environment to enable data processing using PySpark. There are instructions available both Windows, Linux/Mac, GitHub Codespaces, and using SageMaker Studio Lab, an AWS cloud environment.
   
### 2. Processing of raw mobile phone data:
This Notebook elaborates on the structure necessary fields required for basic processing of mobile phone data. It also includes basic checks on the data, removing of duplicate records, and performing exploratory data analysis to check consistency and appropriateness of the data, filtering out irrelevant data (like robots or tourists), and ultimately preparing the data for further processing or analysis.

### 3. Quality assurance:
Quality assurance (QA) is a crucial step involved in ensuring the quality of mobile phone data (MPD) before it can be used for generating reliable statistics. The process is meticulously structured into multiple quality gates, starting with an initial assessment of the input or raw data to ensure its consistency and validity.
   
Specific metrics are utilized to evaluate the consistency of the MPD dataset, such as the percentage of null values, the consistency of the number of subscribers per day, and the count of unique cell locations. The aim is to detect any irregularities or discrepancies that could indicate underlying issues like data entry errors or inconsistencies in data collection processes. Another important part of the QA process is analyzing the diurnal distribution of subscribers' activity, which should ideally follow an expected pattern (elephant shape) based on typical user behavior. Deviations from this pattern are flagged for further investigation. 

For any metrics that fail the QA process, detailed action plans are laid out to address and rectify the issues. This could involve deeper analysis of the data collection and processing methods or collaboration with network operators to ensure the accuracy and reliability of the data being analyzed.

### 4. Home algorithm:
This notebook determines a subscriber's 'home' location using mobile phone data, which is critical for mapping mobile phone data with reference data like Local Administrative Units (LAU) and population estimates. There are many methods to calculate a subscriber’s ‘home’ location. The notebook provides a multistep logic built around identification of cellIDs to which the user is connected at different ‘anchor’ times, times during the night, morning and evening when the user is most likely at ‘home’. Once the most used CellIDs have been identified, various steps are used to assign a 'home cell' for each subscriber, e.g. ‘Direct Inference’ assigns the 
most frequent cell during the main nighttime anchor as the user’s ‘home’ location.

### 5. Indicator calculation:
The final Jupyter Notebook calculates SDG indicator 17.8.1, the proportion of individuals using the Internet. The proportion of Internet users is calculated as the number of subscribers using the Internet, meaning they have at least one IPDR event during the period, divided by the total number of individuals in the target population, multiplied by 100%. The Notebook also allows breaking down Internet usage by technology type (2G, 3G, 4G/LTE, 5G) and geography, allowing for a nuanced understanding of digital accessibility across different regions and technology generations. If CRM data are available and can be linked to CDR data, data can also be 
presented by age and gender.

## Contributors
This project is done by the Data and Analytics Division within the International Telecommunication Union (ITU). For any questions or comments, please contact indicators@itu.int. 

## Folders

### Assets
This folder contains all the assets used in the project such as images, etc.

### Data
This folder contains all the data used in the project such as CSV, JSON, or Excel files.

### Notebook
This folder contains all the Jupyter Notebooks used for processing raw MPD, Quality Assurance (QA), Anchoring, and Calculation of the SDGs Indicator.

### Script
This folder contains all the Python scripts used to inside the notebooks. The most important is conf.py which includes configuration of parameters and the names of all files to be used in the notebooks. 

## Target Audience
The target audience for this project includes the International Telecommunication Union (ITU) and National Statistics Offices who are interested in using MPD to estimate the proportion of the population using the internet.

## Technologies Used
This project leverages MPD, Python, and Spark to process and analyze data.

## Installation
To use this project, you'll need to have Python and Spark installed on your machine. You can then clone the repository from GitHub and run the notebooks in a Jupyter environment.

## Usage
To use this project, follow these steps:

1. Clone the repository from GitHub
2. Open the notebooks in a Jupyter environment
3. Follow the instructions in each notebook to process and analyze the MPD

## Known Issues
At this time, there are no known issues or bugs in this project. If you encounter any problems while using the notebooks, please report them to the project maintainers.
