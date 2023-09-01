# B81-Dashboard
This code creates a dashboard of  [BEAT81](https://www.beat81.com) workout results. It shows the sweat and recovery points for each workout over time for those who are interested. New features will be added.

[<img src="https://github.com/m-guseva/B81-Dashboard/assets/63409978/d5b60126-f5c9-4860-b9a8-181611446c99" width="500"/>](image.png)
[<img src="https://github.com/m-guseva/B81-Dashboard/assets/63409978/e8c32144-ae5d-40e4-96bd-0b16a5d838c8" width="500"/>](image.png)

## Prerequisites
- The code is using [Python 3.10](https://www.python.org/downloads/). For this code to run the packages listed in the requirements.txt file need to be installed. If you are new to python, see below for a brief description "how to install packages" from the requirements.txt file.
- You will need to create your **own excel** sheet that contains your workout results. Currently the BEAT81 website does not publish the sweat and recovery points and so for now you need to acquire this data manually. Potentially I'll add a possibility to scrape data directly from the app.

## How to start Dashboard

### Step 1:
Download the contents of this repository, which includes an example dataset `B81.xlsx`, the code file `B81_DB.py` and the `requirements.txt` file. Put all files in the same folder and **do not** rename them.

### Step 2:
Create an excel file with your past Beat81 workout results. It needs to be in the same format as the example dataset `B81.xlsx`:

[<img src="https://github.com/m-guseva/B81-Dashboard/assets/63409978/45107844-249b-419a-b04f-1af8c35b4b71" width="500"/>](image.png)

### Step 3:
Open a terminal window, navigate to the folder where you saved the files and write `streamlit run B81_DB.py`. The dashboard will open in a new window. Have fun!


## How to install packages
1. In terminal, navigate to folder where files are located `cd YOURPATH`
2. Create virtual environment `python -m venv .venv`
3. Activate virtual environment `source .venv/bin/activate`
4. Install packages `pip install -r requirements.txt`