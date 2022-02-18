#opens txt file called um-server-01.txt; renamed to log_file
log_file = open("um-server-01.txt")

#function that loops through log_file
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip() #removes whitespace from each line
        day = line[0:3] #slices each line from index 0 to 3 which captures the abbreviation for the day; for example: Tue or Sat

        #if day is Tuesday, then print the line
        if day == "Tue":
            print(line)

#calls the function
sales_reports(log_file)
