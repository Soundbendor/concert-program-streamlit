# Concert Program OCR Project

This repository is for the Concert Program OCR Capstone project for Oregon State University and Project Owner Soundbenor Lab.

## Project Description

### Background

When attending professional symphony orchestra concerts, audiences are often given booklets called programs. They typically contain pages of information pertaining to the composer, performers, and commentary about the pieces audiences are hearing. 

The Concert Program Optical Character Recognition (OCR) project collects historical concert data from the web and organizes it in a convenient repository for users to download the information, filtered by desired attributes. This system will allow this text data to be seamlessly fed to various deep learning algorithms. 
 
### Implementation

Music concert program data is gathered from existing digital archives using web scraping scripts. The first 14,000 programs were gathered from the New York Philharmonic from concerts dating back to the 1840’s. The system connects data collection scripts directly to a Microsoft SQL database on the back-end to facilitate a direct pipeline to the front-end web application that allows users to view, filter, and download datasets. This system enables training large-language models with text extracted from historical concert programs.

### Objective

Collecting, cleaning, and filtering this data is a cumbersome yet essential part of training deep machine learning models. Although information on historical music has been digitized, such data is often inaccessible and inconvenient for immediate use in deep learning experiments. This project aims to provide machine learning researchers a robust source of metadata, OCR text, and supplementary information for classical music concerts. Researchers can use the concert program data to develop deep learning approaches seeking to associate descriptive terms with program attributes that deepen our written and oral understanding of how music affects humans  emotionally. 


## Repository Navigation

The repository has three main folders.

### streamllit

This folder contains the code for hosting the Streamlit page with concert program data available for download as a CSV.

### database

This folder contains the code for connecting to the database server and inserting/recieveing data from the database.

### data collection

This folder contains the code for collecting data from the web (i.e. NYPhilharmonic).

