import pandas as pd
#groupby filter: single group->single column , single group->multiple column
heart_data = pd.read_csv('/content/heart.csv')
#fetching data
filtered_data= heart_data[heart_data['ca']==2] 
print(filtered_data)
#single group -> single column
grouped_data = heart_data.groupby('chol').mean()
print(f"The mean of chol is {grouped_data}")
#rename sex to gender
heart_data = heart_data.rename(columns ={ 'sex':'gender'})
print(heart_data)
# set sex 0->female and 1->male
heart_data['gender']= heart_data['gender'].map({0:'female' , 1:'male'})
print(heart_data)
#group by male and female
filter= heart_data.groupby('gender').sum()
print(filter)
#filter male only
filter_male = heart_data[heart_data['gender']=='male']
print(filter_male)
