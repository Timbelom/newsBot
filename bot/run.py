import subprocess

process1 = subprocess.Popen(["python", "bot/functions/newsScraper.py"])
process1.wait()  # Wait for the first file to complete

process3 = subprocess.Popen(["python", "bot/functions/summarize.py"])
process3.wait()  # Wait for the second file to complete

process2 = subprocess.Popen(["python", "bot/functions/botMessage.py"])
process2.wait()  # Wait for the second file to complete
