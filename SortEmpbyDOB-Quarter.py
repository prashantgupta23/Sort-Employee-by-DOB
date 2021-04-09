import pandas as pd

# load excel file using pandas and parse date columns
tmpdf = pd.read_excel('employee__1_.xls', parse_dates=['Date of Birth', 'Date of Joining'])

#print(tmpdf)

# sort rows by column 'Date of Birth'
new_tmpdf = tmpdf.sort_values(by='Date of Birth')

# converting pandas dataframe to dictionary format for iteration
tmpdf_records = new_tmpdf.to_dict(orient='records')

# define dict for final required format 
tmpoutput = {
    'Q1':[],
    'Q2':[],
    'Q3':[],
    'Q4':[]
}

# iterate and parse employee name and add to output dictionary as per respective quarter
for i in range(len(tmpdf_records)):
    emp_name = tmpdf_records[i]['First Name'] + ' ' + tmpdf_records[i]['Last Name']
    print tmpdf_records[i]['Quarter of Joining'], tmpdf_records[i]['Date of Birth'], emp_name 
    tmpoutput[ tmpdf_records[i]['Quarter of Joining'] ].append(emp_name)
    
print("Final Output:")
print(tmpoutput)