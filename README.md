# Concert Program OCR Project

This repository is for the Concert Program OCR Capstone project for Oregon State University and Project Owner Soundbendor Lab.

## Table of Contents
[Project Description](#project_description)

[Repository Navigation](#repository_navigation)

[Design Diagram](#design_diagram)

[How to Run Code](#how_to_run)

[Future Work](#future_work)

[Contributors](#contributors) 

## Project Description
<a name="project_description"/>

### Background

When attending professional symphony orchestra concerts, audiences are often given booklets called programs. They typically contain pages of information pertaining to the composer, performers, and commentary about the pieces audiences are hearing. 

The Concert Program Optical Character Recognition (OCR) project collects historical concert data from the web and organizes it in a convenient repository for users to download the information, filtered by desired attributes. This system will allow this text data to be seamlessly fed to various deep learning algorithms. 
 
### Implementation

Music concert program data is gathered from existing digital archives using web scraping scripts. The first 14,000 programs were gathered from the New York Philharmonic from concerts dating back to the 1840’s. The system connects data collection scripts directly to a Microsoft SQL database on the back-end to facilitate a direct pipeline to the front-end web application that allows users to view, filter, and download datasets. This system enables training large-language models with text extracted from historical concert programs.

### Objective

Collecting, cleaning, and filtering this data is a cumbersome yet essential part of training deep machine learning models. Although information on historical music has been digitized, such data is often inaccessible and inconvenient for immediate use in deep learning experiments. This project aims to provide machine learning researchers a robust source of metadata, OCR text, and supplementary information for classical music concerts. Researchers can use the concert program data to develop deep learning approaches seeking to associate descriptive terms with program attributes that deepen our written and oral understanding of how music affects humans  emotionally. 

## Design Diagram
<a name="design_diagram"/>

![diagram](https://github.com/Soundbendor/concert-program-streamlit/design_diagram.png?raw=true)

## Repository Navigation
<a name="repository_navigation"/>

The repository has three main folders.

### streamlit

To run the app locally, make sure streamlit is installed by typing `pip install streamlit`\
Afterwards, you can use the command `streamlit run streamlit_app.py` to view the app through localhost.

### database

This folder contains the code for connecting to the database server and inserting/recieveing data from the database.

### data collection

This folder contains the code for collecting data from the web (i.e. NYPhilharmonic).

## How to Run Code
<a name="how_to_run"/>

To see how to run each section of code, refer to each of the README.md files within the three main folders listed above. 

To run the project as a whole, follow these steps: 
1. run a microsoft-sql image using docker [Guide to setup server](https://learn.microsoft.com/en-us/azure/azure-sql/database/free-sql-db-free-account-how-to-deploy?view=azuresql)
2. collect data from web *See Data Collection Folder* (i.e. NYPhilharmonic) [Guide for Selenium Web Driver](https://www.selenium.dev/documentation/)
3. insert data to database *See Database Folder* [Guide for pyODBC database queries](https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16)
4. insert data into Streamlit *See Streamlit Folder* [Streamlit Docs](https://docs.streamlit.io/)

## Future Work
<a name="future_work"/>

Future work of this project aligns with the objective. Below are the three most pressing next steps. 

* Load more concert data, including program images and NLP data.
* Automate concert programs loading into database.
* Host database on the cloud

## Contributors
<a name="contributors"/>

Team Members: 
* Jonah Broyer (jonahbroyer.com) 
* Samson DeVol (samsondevol.com)

Project Partner:
* Patrick Donnelly (soundbendor.org)
