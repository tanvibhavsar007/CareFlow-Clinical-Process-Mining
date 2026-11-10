# CareFlow-Clinical-Process-Mining
Healthcare Analytics Project Using PowerBI to analyse Patient Journeys,clinical workflows, and Potential delays.
# Week 1:
# Day 1 - Project Setup
- Created the GitHub repository.
- Added the project description.
- Prepared the repository for Power BI development.
Status: Project setup completed.
CareFlow: Clinical Process Mining

1. Project Overview

CareFlow is a healthcare analytics project focused on understanding patient journeys and clinical workflows in the Emergency Department (ED). The project uses event-log data to explore how patients move through different hospital activities.

2. Project Objectives

- Analyse patient journeys through hospital activities.
- Understand patient outcomes and discharge patterns.
- Explore potential delays using event timestamps.
- Identify workflow patterns and possible bottlenecks.
- Build an interactive and informative Power BI dashboard.

3. Tools and Technologies

- Microsoft Power BI — dashboard and visualisation
- Power Query — data import and preparation
- DAX — calculations and measures
- CSV — event-log dataset
- GitHub — project documentation and version history

4. Dataset Information

The dataset contains the following columns:

- case_id
- activity
- timestamp
- sequence
- triage_code
- initial_zone
- disposition_code
- disposition_desc
- age
- gender

The dataset is intended for analysing recorded patient activities, event sequences, and outcomes.

5. Day 1 — Project Setup

- Created the GitHub repository.
- Added the project overview and objectives.
- Documented the tools and dataset columns.
- Prepared the repository for Power BI development.
- 
6. Project Status

Day 1: Initial project documentation and repository setup.
Day1: PowerBi Setup
-import the careflow_event_log.csv.xlsx dataset into PowerBI.
-Verfied the dataset table and columns.
-Saved the PowerBI Project file as CareFlow_Clinical_Process_Mining.pbix.
7. Disclaimer

This project is for educational purposes. Event duration does not automatically represent a confirmed clinical delay. Findings will depend on the available dataset and analysis.
# Day 2 - KPI Cards and Slicers
Today, I continued developing my CareFlow - Clinical Process Mining Dashboard using Power BI. I created KPI cards to display important Patient related metrices and added Slicers to make the Dashboard Interactive.
Work Completed:
-Created a Total Patient KPI Card.
-Created an Average Patient Age KPI Card.
-Created a Dishcharge Cases KPI Card.
-Added an Activity Slicer to filter data by activity.
-Added Triage Code Slicer to filter data by triage code.
-Added a Patient Outcome Slicer to filter data by dishcharge outcome.
-Organised the cards and slicer to improve dashboard usability.

Learning :
Learned How to create KPI cards, use slicers, and filter healthcare data interactively in PowerBI.

# Day 3 - Charts and Data Visualization
Today, I continued working on my CareFlow - Clinical Process Mining dashboard by Creating different charts to analyse patient demographics,activities triage codes, and dishcharge outcomes.
Work Completed:
-Created a Clustered Column Chart for Patient Age Distribution.
-Created a Donut Chart for Gender Distribution of Patients.
-Created a Line Chart to analyse Patient Flow Across Activity Sequence.
-Created a Clustered Bar Chart for Patient Activity Distribution.
-Created a Pie CHart for Triage Code Distribution.
-Created a Clustered Column Chart to Analyse Cases by Disposition.
-Arrenged the Visuals to make Patient data easier to understand and Compare.

Learning :
Learned how to use different Power BI charts to analyse patient data, identify patterns, and present healthcare workflow information visually. 

# Week 2:
# Day 1: Streamlit Application Setup
-Created the main app.py file.
-set up the basic Streamlit Application.
-Added the initial application structure.
-successfully tested the application locally.
# Day 2: Dashboard Navigation Setup
-Added basic navigation tabs to the Streamlit application.
-Created the initial Structure for different dashboard section.
-prepared the application for further UI devlopment.
# Day 3: Simulation Engine Setup
-Created the simulation folder.
-created the engine.py file.
-added initial simulation engine code.
-created the requirements.txt file for project dependencies.
# Overall Status
Basic application setup and initial simulation engine development completed.
Further UI development and functionality are pending.

# Week 3:
# Day 1: Google BigQuery Setup and Exploration
-Explored the Google cloud BigQuery.
-Worked on Google Cloud Project setup.
-Explored Google BigQuery console and its Features.
-understood the dataset and table requirements 
-explored BigQuery integration Possibilities.
# Day 2: BigQuery to PowerBI Integration
-connected to Google BigQuery through PowerBI.
-Loaded the CareFlow DataSet from BigQuery to PowerBI.
-Explored import and DirectQuery models.
- Reviewed dataset columns and data types.
- Explored data source credentials and authentication settings.
# Day 3: Dashboard Integration and TroubleShooting
-Worked on TroubleShooting the BigQuery Connection.
-Reviewed authentication and Credential configuration.
-Started Planning  PowerBI Dashboard Integration with the CareFlow Streamlit Application.
-Reviewed the Existing Dashboard and its visuals
Pending Task:
-Resolve the connection/refresh issue.
-integrate the powerBI dashboard into the CareFlow interface.
-Test Dashboard functionality and data Updates.

# Week 4
# Day 1:Google BigQuery Project Setup 
Work Completed -
-Reviewed the CareFlow Dataset in Google BigQuery.
-Checked the existing project, dataset and event log table.
-Verified the availability of the careflow_event_log table.
-Reviewed the dataset structure and Available columns.
# Day 2: PowerBI and BigQuery Integration
work Completed:
-Worked on connecting the Existing PowerBI Dashboard to Google BigQuery.
-Configured the BigQuery data Connection.
-Select the careflow_dataset and careflow_event_log table.
-successfully connected the Dashboard to Google BigQuery.
Tools Used: Google BigQuery, Microsoft PowerBI 
# Day 3: Dashboard Integration and Finalisation
Work Completed :
-Completed the Google BigQuery Integration with the existing PowerBI dashboard.
-Reviewed the Dashboard Visuals and KPI Cards.
-Prepared the final PowerBI dashboard File (.pbix).
-Upload the PowerBI dashboard File to the CareFlow GitHub repository.
-Added Google BigQuery project details to the project documentation.

# Google BigQuery Details:
-Project ID: careflow-clinical-project
-Dataset: careflow_dataset
-Table: carefloe_event_log
# BigQuery Project Link:
https://console.cloud.google.com/bigquery?project=careflow-clinical-project 
Tools Used: Google BigQuery, Microsoft PowerBI,GitHub.

