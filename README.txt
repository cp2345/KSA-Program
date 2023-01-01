Author - Chris Roseblossom

FILES-
-KSA_App.exe
-README.txt
(folder) resources
	- Abilities.csv
	- Knowledge.csv
	- MOS_toSOC.csv
	- Skills.csv
	- Users_Guide.html

OVERVIEW-

This program utilizes the files in the "resources" folder as a pseudo-database, and will average the values for each Knowledge, Skill, and Ability per MOS automatically. The user can then either  view an MOS's averages, compare two MOS's averages, or build their "ideal fit" for a job and compare that ideal to the established MOS averages, either individually or as a total. 

GUI EXPLAINATION- 

Main Window-

When first running the application, the user is greeted with the main screen. On this screen, the user can choose to build their "ideal fit" for a job, calculate the difference between an MOS and their "ideal fit," view a single MOS's averages, compare MOSs, or calculate the total difference between all MOSs and their "ideal fit." 

Build Window-

Upon clicking the "Go" button in the "Build" box, the user will be presented with the build window. This window allows the user to enter their ideal values for a job. The user can set a default value per table using the default value entries at the top of the window. After the user is finished entering all their values, the "save" and "save and close" buttons at the bottom of the menu are used to save the values.

"MOS vs. Ideal" and " View Single MOS" Windows-

These windows are displayed when comparing a chosen MOS to the ideal fit, or viewing a single MOS. The display will be 3 tables displaying the associated data.

Compare MOSs Window-

This window will display two MOS dropdowns and 3 blank tables. The user will select two MOSs to compare. After clicking the "Compare" button the tables will populate with the values for each MOS as well as the difference between MOS #1 and MOS #2. 

"resources" FILE EXPLAINATION-

The resources file contains all the files needed to execute the program. If you are going to replace or update a file, you MUST name it exactly as it was originally (see above). 

Abilities.csv, Knowledge.csv, and Skills.csv contain data in comma separated value format. These files are derived from the .xlsx files available on O*NET that can be downloaded at the URL: https://www.onetcenter.org/database.html#all-files. The .csv files contain three columns each; column 1: SOC CODE, column 2: Attribute, column 3: value. The value (on a 0-100 scale) is derived from the "importance" value (originally a value 1-5) by the formula:
value = (("orginal value" - 1)/4)*100
When saving these files, remember to delete the headers, so the .csv file contains only the relevant data. You can generate these types of files from an .xls or .xlsx format by "saving as" the .csv format.

The MOS_to_SOC.csv file is a list of each MOS and its associated SOC codes. The format is; column 1: MOS, columns 2-n: SOC codes
This file is not readily available, and if you want to update it, you must search for the MOS on O*NET at the URL: https://www.onetonline.org/crosswalk/MOC/, and then copy and paste the SOC codes into the sheet. 

DO NOT CHANGE THE .CSV FILES DIRECTLY. This will likely mess with the formatting, and the program will not read it correctly. When updating or modifying the .csv files, ensure that you are using Microsoft Excel to make the changes, then saving files in the .csv format.

The Users_Guide.html file contains the users guide to be displayed upon clicking the corresponding button in the top menu bar.


TROUBLESHOOTING-

If you are trying to use the program, and can not get it to open, check that the resource folder is in the same folder as the "KSA_App.exe" file. If this folder is not placed correctly, the application will not run.

The user will not be able to calculate differences, either total or against an individual MOS unless an "ideal fit" is built first. These "ideal fits" are not saved between instances of the application, so it must be built each time the application is run.
