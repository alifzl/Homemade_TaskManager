# Homemade Task Manager

This repo is mainly about my curiosity about making a fully customized monitoring sytem, based on the real requirements and preference of users.
the project seprated into two major sections: monitoring tools for Windows and Linux operating systems.

## Architecture and pre-requisitions
In below ypu can see the procedure and data flow of the project.
requirements which is required for the Windows version is as follows:


### Windows Users
in the picture below, you can see the procedure of creating a neat monitoring figures in your system.

Requirements | Details
------------ | -------------
Python | Anaconda is prefreble
Used Libraries |  satisfiable with `requirements.txt`. 
Winrm | run `winrm quickconfig` command in your powershell to check the stuff
Redis | confingable with [this](https://redis.io/) link.

### Linux Users
I have no fuckin clue!

## Setup (Installizations, whatever)

### Windows Users

1. Windows ! (winodws 7 and higher, no matter which flavour)
2. run `requirements.txt`. 
3. provide a functional powershell
4. **Winrm** (Windows remote management).
5. Run the `SDC_Implementer.py` in order to create the default monitoring measures which I implemented before. it can be used to send the configuration to the set of servers, using their IP address.
later on, you can go the `Computer Management > Performance > Data Collector Sets > User Defined` and modify it with your personal desire. and surely you can use it as your customized `PerfnomTemplate.xml` by taking an export from the whole data collector.
6. Simply run the main function.

### Linux Users

Under construction dude!



### TO-DO
- [X] Windows
- [ ] Linux
- [ ] WebAPI
- [ ] maybe create some setup file at the end



As Alvin Toffler once said:
> “The illiterate of the 21st century will not be those who cannot read and write, but those who cannot learn, unlearn, and relearn.” 

In the journey of creating this repository, I tried to re-learn lots of stuff. and I suggest that we all should learn the good habit of relearning.

