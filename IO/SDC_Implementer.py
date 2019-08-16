
import subprocess
import sys
import os


subprocess.Popen(
    ['powershell.exe', os.getcwd()+ '\\' + 'go_fetch.ps1', "-CSVFilePath", os.getcwd()+ '\\' + 'Servers.csv',
        "-XMLFilePath", r"temp.xml", "-DataCollectorName", "sample_data_collector_name"])
