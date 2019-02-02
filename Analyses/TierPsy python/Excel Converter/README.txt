---INSTRUCTIONS FOR USING THE SCRIPT---

1. Right-click on 'hdf_converter'
2. Edit with IDLE > Edit with IDLE 3.6
3. IDLE should open up. Click 'Run' > 'Run Module' (or just press f5)
4. Follow the instructions in the screen that should pop up.
5. It'll save an excel file into the 'Excel Converter' folder.


NOTES:

-If you ask it to get data for more worms then what exist in the HDf file, it'll give you an error, but still make an excel file with the worms that do exist.

-If something's being weird or not working (this will probably happen since I just made the script), send me a text at (206) 484-1563 or shoot me a message on slack and I'll figure out what the issue is.

-I put a lot of notes in the actual script file. Any time you see the symbol '#', it means it's a note that describes what part of the script file is doing in english. Reading them might help understand how the script file works.


------------------------------------------------------------


CHANGING THE SCRIPT TO GET DIFFERENT DATA:

This might be tough, so it's best to ask me. If I'm unavailable, this should work:

0. Background info: 

	'functions' are all the code beneath 'def x___' in the 	script. They are blocks of code that do a specific thing.

	You need to change 3 parts of the script to get some more 	info: the code under 'def make_workbook', the code under 	'def print_to_excel', and the code under 'def 	get_file_info'.

	IF YOU TRY TO MESS WITH ANYTHING, MAKE A BACKUP FILE 	FIRST.

1. Go to 'def make_workbook(excel_name):'. This part of the code adds labels to the columns in the excel file. You should see lines that look like:

	ws['A1'] = 'Worm_Index'

To add a new column, copy the lines and adjust accordingly. For example, if you want to add words to cell H1, make a new line that looks like this: 

	ws['H1'] = 'The stuff I want to put in the cell'


2. Go to 'def print_to_excel(excel_file, dct, i):'. This part of the code is what sticks the actual worm data into the excel file. You should see lines that look like:

	ws['A{}'.format(i)] = str(v[0])

'A{}' means 'Column A, and then whichever row currently being added to'. Make a new line with the same format, but change the green letter, and str(v[#]). For example, if you wanted to add new data to column H, you would make a line that looks like:

	ws['H{}'.format(i)] = str(v[7])


3. Go to 'def get_file_info(file, x):'. This part of the code actually goes into the HDF file and pulls out the data (then that data gets used in the print_to_excel section). You should see lines that look like:

	dct['Worm_index'] = means[x][0]

The [x] is whichever worm we're currently on. The [0] means the first column inside features_means, which is 'Worm_index'. You need to go inside features_means and figure out which column whatever data you want is. Once you do that, make a new line that looks like:

	dct['data_column_name'] = means[x][#]

where [#] is the column number that the data you want is.


IF YOU HAVE DONE THIS ALL PROPERLY, THE CODE SHOULD WORK AND A NEW DATA COLUMN SHOULD APPEAR IN EXCEL. GOOD LUCK.