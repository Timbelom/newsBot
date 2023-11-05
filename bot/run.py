import subprocess

process1 = subprocess.Popen(["python", "botENG/functions/newsScraper.py"])
process1.wait()  # Wait for the first file to complete

process2 = subprocess.Popen(["python", "botENG/functions/botMessage.py"])
process2.wait()  # Wait for the second file to complete
