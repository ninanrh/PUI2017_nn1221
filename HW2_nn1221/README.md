# Homework 2

Homework 2 consists of 3 assignments.

### Assignment 1
First I tried to retrieve the data using API keys from MTA and then followed the code [here](https://github.com/fedhere/PUI2017_fb55/blob/master/Lab2_fb55/APIreadingJson.py.ipynb).
I learn how to manage JSON data from [lynda](https://www.lynda.com/MyPlaylist/Watch/13940798/142550?autoplay=true). With advice from Unisse, I opened JSON file in [jsonformatter](https://jsonformatter.org) to learn the dictionary structure. Vivian (Yukun Wan) helped me to construct the for loop code and explain me about `sys.argv[]`code. I wrote `print` code by following the UCSL module.

### Assignment 2
I did the same code to obtain JSON data as in assignment 1. 
Vivian (Yukun Wan) helped me by explaining `fout` and `fout.write` code for creating the CSV files. I then wrote the code like in the previous assignment using for loop and Vivian also helped me to construct that. I run the python script as in the following format `python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv` and tried that with several bus line. After some experiment, I found `KeyError` when I tried bus line `B44`. Unisse told me that was because I have not put the `N/A` entry on my `bus status` and `bus stop` code and then she helped me to construct the code using `try` and `except KeyError:`.
