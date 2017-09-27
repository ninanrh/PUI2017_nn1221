# Homework 2

Homework 2 consists of 3 assignments.

### Assignment 1
#### Overview
This assigment asks for retrieve data using API from MTA NYC and obtain information about number of active buses and their locations in Python script format.
#### Steps
First I tried to retrieve the data using API keys from MTA. It will be used when try to run the script.
To obtain the data using API, I followed the  code [here](https://github.com/fedhere/PUI2017_fb55/blob/master/Lab2_fb55/APIreadingJson.py.ipynb). I changed the API keys on url and bus line variable using `sys.argv[]`code. It will be used to run Python script `python show_bus_locations.py <MTA_API_KEY> <BUS_LINE>`, where `<MTA_API_KEY>` is `sys.argv[1]` and `<BUS_LINE>` is `sys.argv[2]`. After reading the JSON file, I set `noofbus` variable, which directly contains bus information. As the output format asks, I set the printed output in 3 parts. The first one is the name of bus line which use `sys.argv[2]` code. The second one is to print the number of active buses, which I use `len(noofbus)`. The last one is to obtain coordinate information, which use `for i in range(len(noofbus)):`, following by location of the latitude and longitude under the dictionary of JSON data. I the printed it with the following format `print("Bus {} is at latitude {} and longitude {}".format(i, latitude, longitude))`.
#### Credit
I learn how to manage JSON data from [lynda](https://www.lynda.com/MyPlaylist/Watch/13940798/142550?autoplay=true). With advice from Unisse, I opened JSON file in [jsonformatter](https://jsonformatter.org) so it is easier to learn the dictionary structure. Vivian (Yukun Wan) helped me to construct the `for loop` code and explain me about `sys.argv[]`code. I wrote `print` code by following the UCSL module.

### Assignment 2
#### Overview
This assigment asks for retrieve data using API from MTA NYC and export information about specific bus line coordinate, bus stop locations and their status in Python script format.
#### Steps
I did the same code to obtain JSON data as in assignment 1 above which is learned from [here](https://github.com/fedhere/PUI2017_fb55/blob/master/Lab2_fb55/APIreadingJson.py.ipynb). I set the code to open csv file using `fout = open(sys.argv[3], "w")` as the example from [here](https://github.com/fedhere/PUI2017_fb55/blob/master/Lab2_fb55/aSimplePythonThatWritesToCSV.py). The `sys.argv[3]` code is for the name of CSV file. To obtain coordinat, bus stop and bus status, I wrote for loop `for i in noofbus:` code which followed by the location of bus coordinat, bus stop and bus status under the JSON data dictionary. I wrote `fout.write("{},{},{},{}\n".format(longitude,latitude,stop,status))` code that write the csv file. Then if I run the script `python get_bus_info.py <MTA_API_KEY> <BUS_LINE> <BUS_LINE>.csv` it will save new CSV file named `<BUS_LINE>.csv`.
#### Credit
Vivian (Yukun Wan) helped me by explaining `fout` and `fout.write` code for creating the CSV files. I then wrote the code like in the previous assignment using for loop and Vivian also helped me to construct that. I run the python script as in the following format `python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv` and tried it with several bus line. After some experiment, I found `KeyError` on my terminal when I tried bus line no `B44`. Unisse told me that was because I have not put the `N/A` entry on my `bus status` and `bus stop` code and then she helped me to construct the code using `try` and `except KeyError:`.

### Assignment 3
#### Overview
This assignment asks for get the data from environmental variable DFDATA and visualize the data and reduced data using table and plot.
#### Steps
First, I imported `sys`, `os`, `numpy`, `pandas`, and `matplotlib.pylab` library. I looked for data from the environmental variable DFDATA through `dfdata = os.getenv("DFDATA")` and check the location of data using `dfdata` that give result of `/gws/open/NYCOpenData/nycopendata/data'`. I checked on my terminal to find where is the location of csv files under DFDATA using `find . -name "*.csv"` and found bunch of data. I picked it randomly and copied the location to the ipython notebook so Pandas can open it using `df = pd.read_csv(dfdata + '/2iqd-z7vu/1476480727/2iqd-z7vu.csv')` code. I showed the top few rows table df using `df.head()`. To remove unused variable, first I list all of the dictionary keys using `df.keys()`. There are four column that have numerical values which are `Unique Key`, `Incident Zip`, `Latitude`, and `Longitude`. I decided to plot latitude and longitude data, which both of them has numerical values that makes sense. I then removed other variables using `df.drop()` and display again the top few rows table df using `df.head()`. I plotted the data using `df.plot` with `scatter` type of plotting and gave plot axes labels, caption, and title using matplotlib.
#### Credit
I followed the instruction [here](https://github.com/fedhere/PUI2017_fb55/blob/master/Lab2_fb55/inClassFormattingTables.ipynb) and [homework 2 instruction](https://github.com/fedhere/PUI2017_fb55/tree/master/HW2_fb55) to open and format the data. For plot the data, I followed the step on [here](http://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html) and UCSL modules.
