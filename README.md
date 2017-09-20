# PUI2017_nn1221

# Homework 1

This homework 1 located under PUI2017_nn1221 directory and consist of 3 assignments.
I received help from Unisse to do this homework, especially to set up GitHub and to type the code/command.

### Assignment 1
The first assignment is to continue the first lab and it is located in the different repository from this one, which is https://github.com/ninanrh/gittest_nn1221 
I fork and mess with Unisse https://github.com/ninanrh/gittest_uc288 repository.
Last, I fix the conflicting merge.

### Assignment 2
The second assignment is to create new directory called `PUI2017_nn1221` and created an environmental variable `PUI2017` that points to the directory and create `pui2017` alias. The step I took for assignment 2 is here:

First, I log on into CUSP compute then I created directory on CUSP compute called PUI2017 using command 
`mkdir PUI2017`

The directory is located on the `/home/cusp/nn1221/PUI2017`

![alt text](https://raw.githubusercontent.com/ninanrh/PUI2017_nn1221/master/directory.png)


I then saved it in .bashrc and created alias using command:
`export PUI2017="/home/cusp/nn1221/PUI2017"`
That export command is for exporting PUI2017 as `/home/cusp/nn1221/PUI2017` directory.

I then created the alias using this command `alias pui2017="cd $PUI2017"`.

![alt text](https://raw.githubusercontent.com/ninanrh/PUI2017_nn1221/master/bashprofile.png)

Whenever I type the alias `pui2017`, the working directory will change to PUI2017

### Assignment 3

1. I give numpy as seed `np.random.seed()` 
2. I generate random distribution with array called `ReprRand` 
3. I generate more random numpy array using `for` loop
4. I plot the random rumber using matplotlib and gave the plot its title, axis labels, and caption.
