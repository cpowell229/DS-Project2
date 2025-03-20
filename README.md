# DS-Project2
### DS 4002 Group 4
### Authors: Delaney Brown (Leader), Diya Gupta, Connor Powell

## Contents of Repository: 
This repository contains the datasets, scripts, and outputs for our second project for DS 4002, which focuses on analyzing U.S. job posting data from Indeed.com, beginning on February 1st, 2020, until present, and seeks to make predictions for the job market in the next five years, focusing on employability of specific job categories, the most optimal times of year for searching for specific types of jobs, and pandemic influences on these trends [2,4,17]. The License.md file contains the MIT license for our repository. The SCRIPTS folder contains our project’s scripts for our analysis, which are named in the order that they should be run to produce the outputs. The DATA folder contains the original data from the FRED page “Job Postings on Indeed” (2025), which utilize datasets from the Github repository “Indeed Job Postings Index,” that our project’s analysis uses [2,4]. The data on the Github repository “Indeed Job Postings Index” comes from the Indeed Hiring Lab, located at https://www.hiringlab.org/ [17]. Finally, the OUTPUTS folder contains the outputs of our analysis.

## Software and Platform Selection


## Map of Our Documentation
### 1. SCRIPTS Folder: Scripts for our analysis
  * `dataAnalysis.py` - This file utilizes the `job_postings_by_sector_US.csv` dataset to produce a primary analysis of the posting trends in specific job       sectors over time. The output of this script is seen in `sector_summary.png`.
### 2. DATA Folder: Original datasets from the FRED, which pulls data from the Github repository, “Indeed Job Postings Index” [2,4]
  * `aggregate_job_postings_US.csv` - This dataset contains the data for all job postings on a daily basis, particularly the “indeed_job_postings_index” variable, which is
    calculated in comparison to the starting data collection date (2/01/2020) and is both adjusted and not adjusted for seasons [10].
  * `job_postings_by_sector_US.csv` - This dataset contains posting index data for each specific job sector on a daily basis [8].
  * `metro_job_postings_us.csv` - This dataset contains the posting index data for different metro city areas on a daily basis [9].
  * `state_job_postings_us.csv` - This dataset contains the posting index data for each state on a daily basis [7].
### 3. OUTPUTS Folder: Outputs of our analysis
  * `sector_summary.png` - This graph output demonstrates the growth rate of specific job sectors by their posting indexes from February 1, 2020 until
    about present, utilizing `job_postings_by_sector_US.csv` dataset, in the DATA folder. The script to produce this graph can be found in
    `dataAnalysis.py`, in the SCRIPTS folder.


## Instructions for Reproducing Results
