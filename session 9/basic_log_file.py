# write todays date to log.txt
# append "program started"

with open("log.txt", "a") as log:
    log.write("26-02-2026\n")
    log.write("Program started")
    
