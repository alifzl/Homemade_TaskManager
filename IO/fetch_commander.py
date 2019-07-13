
import subprocess
import sys

subprocess.Popen(
    ['powershell.exe', r'go_fetch.ps1', "-CSVFilePath", r"Servers.csv",
        "-XMLFilePath", r"PerfmonTemplate.xml", "-DataCollectorName", "sample_data_collector_name"])
