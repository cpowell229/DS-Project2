# DS-Project2
### DS 4002 Group 4
### Authors: Delaney Brown (Leader), Diya Gupta, Connor Powell
1
## Contents of Repository: 
This repository contains the datasets, scripts, and outputs for our second project for DS 4002, which focuses on analyzing U.S. job posting data from Indeed.com, beginning on February 1st, 2020, until present, and seeks to make predictions for the job market in the next five years, focusing on employability of specific job categories, the most optimal times of year for searching for specific types of jobs, and pandemic influences on these trends [2,4,17]. The License.md file contains the MIT license for our repository. The SCRIPTS folder contains our project’s scripts for our analysis, which are named in the order that they should be run to produce the outputs. The DATA folder contains the original data from the Federal Reserve Bank of St. Louis (FRED) page “Job Postings on Indeed” (2025), which utilize datasets from the Github repository “Indeed Job Postings Index,” that our project’s analysis uses [2,4]. The data on the Github repository “Indeed Job Postings Index” comes from the Indeed Hiring Lab, located at https://www.hiringlab.org/ [17]. Finally, the OUTPUTS folder contains the outputs of our analysis.

## Software and Platform Selection


## Map of Our Documentation
### 1. SCRIPTS Folder: Scripts for our analysis
  * `initial_analysis` - A folder that contains the scripts listed below.
    * `dataAnalysis.py` -  
          * INPUT: `job_postings_by_sector_US.csv`
          * OUTPUT:`sector_summary.png`
    * `dataAnalysis01.py` 
          * INPUTS:`state_job_postings_us.csv` 
                    `job_postings_by_sector_US.csv` 
          * OUTPUTS:`sector_line_6month.png` 
                    `us_map_states.png`
  * `aggregateForecast.py` - Perfroms linear regression to forecast the average monthly number of Indeed job posts over the next five years.
          * INPUT: `aggregate_job_postings_US.csv`
          * OUTPUT:`job_postings_time_series_forecast.png`
  * `metroForecast.py` - Perfroms linear regression to forecast the average monthly number of Indeed job posts over the next five years.
          * INPUT: `metro_job_postings_us.csv`
          * OUTPUT:`metro_forecasts.png`
  * `sectorForecast.py` - Perfroms linear regression to forecast the average monthly number of Indeed job posts over the next 5 years.
          * INPUT: `job_postings_by_sector_US.csv`
          * OUTPUT:`top_sector_forecasts.png`
### 2. DATA Folder: Original datasets from the FRED, which pulls data from the Github repository, “Indeed Job Postings Index” [2,4]
  * `aggregate_job_postings_US.csv` - This dataset contains the data for all job postings on a daily basis, particularly the “indeed_job_postings_index” variable, which is
    calculated in comparison to the starting data collection date (2/01/2020) and is both adjusted and not adjusted for seasons [10].
  * `job_postings_by_sector_US.csv` - This dataset contains posting index data for each specific job sector on a daily basis [8].
  * `metro_job_postings_us.csv` - This dataset contains the posting index data for different metro city areas on a daily basis [9].
  * `state_job_postings_us.csv` - This dataset contains the posting index data for each state on a daily basis [7].
### 3. OUTPUTS Folder: Outputs of our analysis
  * `initial_analysis` - A folder that contains the outputs listed below.
    * `sector_summary.png` - a plot that shows the trendline for indeed job postings for each sector listed in `job_postings_by_sector_US.csv` from 2020 - 2025.
    * `sector_line_6month.png` - a plot that shows the trendline for monthly job postings over the last 6 months for the top 5 sectors in average monthly job posts. It uses the `job_postings_by_sector_US.csv` 
    * `us_map_states.png` - A map of the united states in which each state is colored on a scale of dark to light blue or white. The shade of blue is determined by the average number of indeed job posts in the `state_job_postings_us.csv`, with dark blue repersenting a larger number of posts.
  * `job_postings_time_series_forecast.png` - a plot generated via `aggregateForecast.py` which showcases the historical trendline of monthly job postings on Indeed with a blue line. The graph then displays the predicted 5 year forecast with an orange dashed line and the confidence interval as the orange shaded area. The data comes from `aggregate_job_postings_US.csv`.
  * `metro_forecasts.png` - a plot generated via `metroForecast.py` which showcases the indeed job post trendlines for the top 10 states in job posts based on their metropolitan areas from `metro_job_postings_us.csv`. It also displays the predicted 5 year forecast for each of the 10 states with a dashed line extending from the solid line of historical data.
  * `top_sector_forecasts.png` - a plot generated via `sectorForecast.py` which showcases the indeed job post trendlines for the top 10 sectors over the last 5 years in job posts based on the data from `job_postings_by_sector_US.csv`. It also displays the predicted 5 year forecast for each of the 10 sectors with a dashed line extending from the solid line of historical data.


## Instructions for Reproducing Results
  * Clone this repository and download `requirements.txt` to ensure all of the proper packages are installed in your working enviorment to run the analysis scripts.
  * Run this command in your terminal
      *  (bash) `pip install -r requirements.txt`
  * The Analysis scripts can now be ran to produce the intended outputs and reproduce our results. (Refer Above to which scripts produce which outputs)

