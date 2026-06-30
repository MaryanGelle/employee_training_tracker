# Employee Training Tracker

The Employee Training Tracker is a userfriendly command-line application developed using Python. It allows
users to manage employee training records stored in Google sheets through an easy to use terminal interface.
The application is designed for HR team and managers to keep track of employees training without having to 
edit the Google Sheets manually.

Users can:
- add new training records
- view all records
- search employee records
- analyse training progress
- delete records

The Empployee Training Tracker program is written using python and is deployed on heroku using Node.js.
Below is an image of the Mock terminal:

![Mockup Terminal](README.images/mockup.png)

# Live Project
**Live application:**  
[Live Application](https://employee-training-tracker-952185589660.herokuapp.com/)


<a id="contents"></a>
## Contents

- [Overview](#overview)
- [User Experience UX](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Project Goals](#project-goals)
- [Features](#features)
  - [Main Menu](#main-menu)
  - [Add Training Record](#add-training-record)
  - [View Records](#view-records)
  - [Search Records](#search-records)
  - [Analyse Records](#analyse-records)
  - [Delete Records](#delete-records)
  - [Input Validation](#input-validation)
  - [Google Sheets Integration](#google-sheets-integration)
- [Data Model](#data-model)
- [Flowchart](#flowchart)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [PEP8 Validation](#pep8-validation)
  - [User Story Testing](#user-story-testing)
  - [Bugs Encountered and Fixes](#bugs-fixes)
  - [Remaining Bugs](#remaining-bugs)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Future Features](#future-features)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Author](#author)


## Overview

The Employee Training Tracker is a command-line application developed in Python to help organisations 
manage employee training records. The application allows users to add, view, search, analyse and delete 
training records, with all data stored in Google Sheets. It was designed to provide a simple and efficient
way of tracking employee training progress.

## User Experience UX

The application was designed with simplicity and ease of use in mind. As a terminal-based application,
users interact through a clear menu system and receive straightforward instructions throughout the programme.

The application focuses on:
- A simple and intuitive menu.
- Clear prompts and confirmation messages.
- Input validation to reduce user errors.
- Easy navigation between features.
- Readable output using consistent formatting.

## Features

The Employee Training Tracker includes the following features:

- **Add Training Record** – Allows users to add a new employee training record to Google Sheets.
- **View Records** – Displays all stored training records.
- **Search Records** – Searches for an employee's training record by name.
- **Analyse Records** – Calculates and displays training statistics and completion percentages.
- **Delete Records** – Removes selected training records from both the application and Google Sheets.
- **Input Validation** – Prevents empty inputs and validates training status before saving data.

## Data Model

The application stores all training records in a Google Sheets spreadsheet using the `gspread` library.

Each record contains four fields:

| Field         |       Description           |
|---------------|-----------------------------|
| Employee Name | The employee's full name. |
| Training Name | The name of the completed or assigned training. |
| Status        | The training status (Completed, In Progress or Not Started). |
| Record Date   | The date and time the record was created. |

Each row in the spreadsheet represents a single training record and is synchronised with the application whenever records are added, viewed, searched or deleted.

## Flow Chart

In the creation of the Empployee Training Tracker program i created a flowchart to show the overall workflow and its programme logic.
Below is an image of the flowchart:


![Flowchart](README.images/flowchart.png)

## Testing

Testing was used to ensure quality and correct coding in order to create a functioning programme for our users experience.
It includes manual testing, PEP8 validation, User story testing and testing for bugs.

Please refer to [**_here_**](TESTING.md) for more information on testing the programme.

[Back to top](#contents)

## Technologies Used

### Programming Language
- Python 3

### Libraries 
- gspread - Used to read, write and delete data.
- google-auth - Used to authenticate the application Google Sheets.
- datetime - Used to automatically record the date and time of each training record that is created.

### APIs
- Google Sheets API

### Development Tools
- Visual Studio Code
- Github
- Git
- Heroku
- Google Clout Platform

### Python Packages
- Autopep8 - Used to format the code according to PEP 8 Guidelines.
- Pylance - Used for code analysi and IntelliSense during development. 

### Validation
- CI Python Linter (PEP8)

### Other

- diagrams.net (flowchart)

[Back to top](#contents)

## Deployment

This project was deployed to Heroku using the following steps:

- Sign in to your Heroku account.
- Select **New** and choose **create new app**.
- Enter a unique application name and select the appropriate region.
- Click **Create app**.
- Open the **Settings** tab.
- Under **Config Vars**, add:
 - 'PORT' with the value '8000'.
 - 'CREDS' with the value content of the 'creds.json' file.
- Under **Buildpacks**, add:
 - Python
 - Node.js
- Open the **Deploy** tab.
- Choose **Github** as the deployment method.
- Connect the Github repository that contains the project.
- Click **Deploy Branch**
- Once the deployment is complete, click **Open App** to launch the application. 

<div align="center">
  <img src="README.images/open.app.png" style="background-color: white" alt="End of Debugging open app">
</div>

![Debugging App](README.images/open.app.png) 


## Future Features

Future improvements that could be added to the application include:
- Edit an existing training record instead of deleting or re-entering the data.
- Filter the training record according by training status.
- Sort records alphabetically order or by training date.
- Generate more detailed statistics or charts to help monitor the data.
- Add user authentication for security reasons so only authorised users can manage the data.

## Credits

Below you will find credit references to my sources for content, media and feedback.

- Code Institute Python Essentials template.
- Code Institute mock terminal template for Heroku deployment.
- Google Sheets API and the gspread python library was used to store, retrieve and manage data.

Others
- diagrams.net (flowchart)


## Acknowledgments 

- My Code Institute mentor for their guidance, encouragement and valuable feedback throughout the project.
- The Code Institute tutors and Student Care for their support during the development of this project.
- My family and friends for testing the application and providing valuable feedback.

## Author
This command-line application was made by Maryan Gelle (Developer) as a Project 2 Python for my FullStack Programme at Code Institute in 2026.

