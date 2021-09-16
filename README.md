## Introduction

This application is used for chess tournament organization with swiss system.

It contains the follwing features:
- database with players and tournaments tables
- creation of a new tournament
- saving at any step of the creation of the tournament
- loading of a existing tournament
- swiss algorithm for defining matches
- creation of new players
- loading and modification of an existing player
- generation of diverse reports

## Prerequisites

You must have Python 3.6 or higher installed in order to execute this code.

## Installation

1 - Clone the github Repository.

```bash
git clone https://github.com/HaroldHaldemann/ChessTournament
```

2 - Create your virtual environment.

```bash
python -m venv name-virtual-env
```

3 - Activate your virtual environment.

On Windows
```windows
name-virtual-env\Scripts\activate.bat #In cmd
name-virtual-env\Scripts\Activate.ps1 #In Powershell
```

NB: If you activate your environment with Powershell, don't forget to enable running script :
```windows
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

On Unix/MacOs
```bash
source tutorial-env/bin/activate
```

4 - Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.

```bash
pip install -r requirements.txt
```

## Usage

To execute this script, you have to enter the following code line:

```python
python ./main.py
```

When executed, the terminal will ask you what you want to do.
Follow the instructions and enter the number of the action you want to do.

When you create a player or a tournament for the first time, a database will be created in your directory folder. This database is named "database.json" and contains the data of your application.

## Export data

To export data into json, select the export menu from the main menu (option 5), then select the data you  want to export.

The data will be stored in a json file into Exports folder.

## Generate flake8 report

To generate a flake8 report, enter the following command
```bash
flake8
```

The report will be stored in the folder named "flake_rapport"

To analyse the report, open the file "index.html" within the folder "flake_rapport"