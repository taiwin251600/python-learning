import pandas as pd
data = {'Name': ['Esha','Ahmad','Noor','Maryam','Zahid'],
        'Gender': ['female','male','female','female','male'],
        'SemesterNo': [4,5,2,6,4],'RollNo': [2,3,6,9,1],'Degree': ['CS','Ecommerce','IT','AI','CS']}
df = pd.DataFrame(data)
print(df)
print("After renaming:")
df2=df.rename(columns={'Degree':'EnrolledIn'})
print(df2)
df.info()

print(df.describe())
print()
df.to_csv(r"C:\Users\DeLL\Desktop\my mini project.csv", index=False)
print('csv file saved successfully!')
print("The method of importing file")
df3= pd.read_csv(r"C:\Users\DeLL\Desktop\my mini project.csv")
print(df3)

print()
df4= df[['Name','Degree']] #to select specific columns
print(df4)
print()
print(df.loc[df.Name=='Esha']) # for accessing specific rows
print(df.loc[0:3])
print(df.iloc[1])
print()
print(df.iloc[0:3]) #Select first three rows using iloc
