import subprocess

process1 = subprocess.Popen(["python", "functions/newsScraper.py"])
process1.wait()  # Wait for the first file to complete

process2 = subprocess.Popen(["python", "functions/botMessage.py"])
process2.wait()  # Wait for the second file to complete
