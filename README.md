## Weather & Solar Dashboard

This initiative is a Weather & Solar Dashboard developed with Streamlit, Pandas, and Plotly. It provides users with the capability to choose a city and a specific date to explore weather and solar data, including solar irradiance, temperature, relative humidity, wind parameters, and module temperatures. Moreover, it incorporates comprehensive data analysis techniques such as correlation studies, data preparation, quality evaluations, histograms, scatter plots, statistical summaries, trend analysis, wind studies, and temperature assessments.

## Highlights

 - City Selection: Pick from an array of cities to access relevant weather and solar information.
 - Date Selection: Choose a specific date to isolate data for analysis.
 - Comprehensive Data Insights:
 - Correlation Analysis: Investigate how weather and solar parameters interact.
 - Data Preparation: Address missing values and anomalies to ensure the dataset is ready for use.
 - Data Validation: Confirm the dataset’s consistency and accuracy.
 - Visualization Tools: Utilize histograms and scatter plots to illustrate distributions and correlations.
 - Descriptive Statistics: Access key metrics like averages, medians, and percentiles.
 - Trend Analysis: Study variations and recurring patterns over time.
 - Wind Assessment: Dive into wind speed, direction, and gust evaluations.
 - Temperature Studies: Detailed exploration of both ambient and module-specific temperatures.
## Interactive Charts:
 - Solar Irradiance Trends: Monitor Global, Direct, and Diffuse Irradiance.
 - Temperature & Humidity Visualization: Examine fluctuations in temperature and relative humidity.
 - Wind Behavior: Analyze speed, gusts, and direction data.
 - Module Temperature Overview: Track the performance of solar modules A and B.
 - Raw Data Display: View the unprocessed dataset in a tabular form, if needed.

## Setup Instructions

  1. Clone the repository:

     git clone https:https://github.com/Kiracr/Optimal-Solar-Investment-Analysis

  2.  Install dependencies:

      pip install -r src/requirements.txt

## How to Run

   Execute the Streamlit app:

      streamlit run scripts/streamlit.py 


## Dataset

The project’s dataset is organized into CSV files stored in the data folder. Each city has a dedicated file containing detailed weather and solar data.

## File Structure

      
├── .github
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── notebooks
│       ├── __init__.py
|       ├── Correlation_analysis.ipynb
|       ├── Data_cleaning.ipynb
|       ├── Data_quality_check.ipynb
|       ├── Histograms_and_bubble_chart.ipynb
|       ├── Summary_statistics.ipynb
|       ├── Time_series_analysis.ipynb
|       ├── Wind_and_temp_analysis.ipynb
|       └── README.md
├── tests
│   ├── __init__.py
├── Src
└── scripts
    ├── __init__.py
    └── README.md


