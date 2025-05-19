import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
##import th data
data = pd.read_csv("C:/Users/Nikita/OneDrive/Desktop/daad.univarsity/DAAD_data_base_featured.csv")

## clean data 
data.replace(['missing','Unknown','na'],pd.NA,inplace=True)

## Summary Statistics
print('datashape',data.shape)
print('\nfirst 5  row :')
print(data.head)
print('\n colums:',data.columns.tolist())
print('\ndata type:\n',data.dtypes)
print("\nMissing Values:\n", data.isnull().sum())
print("\nTuition Fee Statistics:\n", data['Tuition fees per semester in EUR'].describe())

# Visualization Setup
sns.set(style="whitegrid")
plt.figure(figsize=(5, 5))

# 1.degree distubution 
plt.figure()
degree_course = data[['Master', 'PhD', 'Bachelor']].sum()
degree_course.plot(kind='bar',title='Distribution of Degrees')
plt.xlabel('degree type')
plt.ylabel('count')
plt.show()

# 2. Tuition Fee Distribution
plt.figure
sns.histplot(data['Tuition fees per semester in EUR'],bins=20,kde=True)
plt.title("Tuition Fee Distribution")
plt.xlabel("Tuition Fees (EUR)")
plt.ylabel("Number of Programs")
plt.show()

# 3.Language-wise Course Distribution
plt.figure()
degree_course = data[['English', 'German', 'Other Language']].sum()
degree_course.plot(kind='bar',title='Language-wise Course Distribution')
plt.xlabel('Language')
plt.ylabel('Number of Courses')
plt.show()

# 4. University-wise Course Count
plt.figure()
top_universities = data['University'].value_counts().nlargest(10)
top_universities.plot(kind='barh', title='Top 10 Universities by Number of Courses')
plt.xlabel("Number of Courses")
plt.ylabel("University")
plt.show()

# 5. City-wise Course Availability
plt.figure()
top_cities = data['City'].value_counts().nlargest(10)
top_cities.plot(kind='bar', title='Top 10 Cities by Number of Courses')
plt.xlabel("City")
plt.ylabel("Number of Courses")
plt.xticks(rotation=45)
plt.show()


print("Analysis Completed.")

#save cleaned data 
data.to_csv('cleaned_daad_university_data.csv', index=True)





