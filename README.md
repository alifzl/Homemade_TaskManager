# Homemade Task Manager

This repo is the result of my curiosity about making a fully customized monitoring system, based on the real preference and requirements of users.
And it was a great experience being skillful in great visualizationing tool of python called [Dash](https://plot.ly/dash).


![Demonstration](https://github.com/AFZL95/Homemade_TaskManager/blob/master/demonstration.gif)

## Architecture and pre-requisitions
In below you can see the procedure and data flow of the project.
requirements which are required for the Windows version is as follows:


### Windows Users
in the picture below, you can see the procedure of creating neat monitoring figures in your system.

Requirements | Details
------------ | -------------
Python | Anaconda is preferable
Used Libraries |  satisfiable with `requirements.txt`. 
Winrm | run `winrm quickconfig` command in your PowerShell to check the stuff
Redis | configurable  with [this](https://redis.io/) link.

### Linux Users
will be issued whenever I have time.

## Setup (Installations, whatever)

### Windows Users

1. Windows! (winodws 7 and higher, no matter which flavor)
2. run `requirements.txt`. 
3. provide a functional PowerShell
4. **Winrm** (Windows remote management).
5. also the ability of executing scripts via the windows powershell should be checked by running `get-executionpolicy `in the powershell. if you faced `Resrticted` result, simply run `Set-ExecutionPolicy RemoteSigned ` and you're good to go.
5. Run the `SDC_Implementer.py` in order to create the default monitoring measures which I implemented before. it can be used to send the configuration to the set of servers, using their IP address (which is defined in server.csv). which also, in this case is only the localhost. but you can add more as you want.
later on, you can go to the `Computer Management > Performance > Data Collector Sets > User Defined` and modify it with your desire. and surely you can use it as your customized `temp***.xml` by taking export from the whole data collector.
6. Simply run the `viz_it.py` and done.

### Linux Users
Under construction.



### TO-DO
- [X] Windows
- [ ] Linux
- [ ] WebAPI
- [ ] maybe create some setup file at the end



As Alvin Toffler once said:
> “The illiterate of the 21st century will not be those who cannot read and write, but those who cannot learn, unlearn, and relearn.” 

In the journey of creating this repository, I tried to re-learn lots of stuff. and I suggest that we all should learn the good habit of relearning.

