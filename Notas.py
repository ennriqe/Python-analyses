#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Bachelor = pd.read_excel('/home/erq/Desktop/Documents_Enrique_Barrueco/Bachelor.xlsx')


# In[3]:


Bachelor.sort_values('Grade', ascending=False)


# In[195]:


# Average for the 180 top ECTS credits

Ranked = Bachelor.sort_values('Grade', ascending=False)
Ranked.reset_index(inplace=True)

ECTS_Credits = 0
j = 0
Grade_Sum_Top = 0

while ECTS_Credits < 180:
    ECTS_Credits = Ranked['ECTS'][j] + ECTS_Credits
    Grade_Sum_Top = Ranked['Grade'][j] + Grade_Sum_Top
    j = j + 1
    
Avg_Top = Grade_Sum_Top/j
print("Taking the 32 subjects with the highest grade which sum to", ECTS_Credits,"my average is", Avg_Top, "out of 10" )


# In[5]:


#In total during my degree I have completed 246 credits
Bachelor['ECTS'].sum()


# In[6]:


average = Bachelor['Grade'].sum()/len(Bachelor)
print("My average grade has been", round(average,2),"out of 10, this is an absolute mesasure, not a relative one, it is not compared to the rest of my classmates.")


# In[7]:


# Lets compute the average for each academic year:

First_Year = Bachelor['Academic_Year'] == '2015-16'
Avg_First = Bachelor[First_Year]['Grade'].sum()/len(Bachelor[First_Year])

Second_Year = Bachelor['Academic_Year'] == '2016-17'
Avg_Second = Bachelor[Second_Year]['Grade'].sum()/len(Bachelor[Second_Year])

Third_Year = Bachelor['Academic_Year'] == '2017-18'
Avg_Thrid = Bachelor[Third_Year]['Grade'].sum()/len(Bachelor[Third_Year])

Fourth_Year = Bachelor['Academic_Year'] == '2018-19'
Avg_Fourth = Bachelor[Fourth_Year]['Grade'].sum()/len(Bachelor[Fourth_Year])

Average_per_Course = [Avg_First, Avg_Second, Avg_Thrid, Avg_Fourth]
Average_per_Course


# In[8]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
#To avoid having type plt.show() to show the plot 

import numpy as np


# In[179]:


# Let's plot this result: 

Average_per_Course = [Avg_First, round(Avg_Second, 2), Avg_Thrid, round(Avg_Fourth, 2)]
Average_per_Course

Labels_Average_per_Course = ["First Yeat", "Second Year", "Thrid Year", "Fourth Year"]

y_pos = np.arange(len(Average_per_Course))


plt.figure(figsize=(15,8))

# Create bars
plt.bar(y_pos, Average_per_Course, color=(sns.light_palette("orange",n_colors=4)),alpha=1)
 
# Create names on the x-axis
plt.xticks(y_pos, Labels_Average_per_Course, fontsize=13)

# Insert value on top of each bar

xlocs=[i+1 for i in range(0,10)]
xlabs=[i/2 for i in range(0,10)]

for i, v in enumerate(Average_per_Course):
    plt.text(xlocs[i] - 1.05, v + 0.1, str(v),fontsize=14)

# Title

plt.title("Yearly Average Grade", fontsize=15)


# In[10]:


# I want to classify each subject into a relevant category.

Quant_Econ = []
Mathematics = []
Finance = []
Econ = []
Stats_and_Econometrics = []
Others = []

for Subject in Bachelor['Subject']:
    
    if ('Micro' in Subject) or ('Macro' in Subject) or ('Methods' in Subject) or ('Infor' in Subject):
        Quant_Econ.append(Subject)
        #print(Subject)
        
    elif 'Math' in Subject or 'Opti' in Subject:
        Mathematics.append(Subject)
        #print(Subject)
        
    elif ('Financ' in Subject) or ('Accou' in Subject):
        Finance.append(Subject)
        #print(Subject)
    
    elif 'Econometrics' in Subject or 'Stati' in Subject:
        Stats_and_Econometrics.append(Subject)
        #print(Subject)
    
    elif ('Econ' in Subject) or ('Tax' in Subject) and (Subject not in Quant_Econ):
        Econ.append(Subject)
        #print(Subject)
    
    elif 'Thesis' in Subject:
        Thesis = Subject
        
    else:
        Others.append(Subject)


# In[11]:


Stats_and_Econometrics = Bachelor["Subject"].isin([Stats_and_Econometrics][0])
Stats_and_Econometrics = Bachelor[Stats_and_Econometrics]
Stats_and_Econometrics.sort_values('Grade', ascending=False)


# In[136]:


# Average and number of credits in Statistics and Econometrics

Avg_Stats_and_Econometrics = Stats_and_Econometrics['Grade'].mean()
Mdn_Stats_and_Econometrics = Stats_and_Econometrics['Grade'].median()

print("Average in Statistics and Econometrics is", Avg_Stats_and_Econometrics, "out of 10")
print("Median in Statistics and Econometrics is", Mdn_Stats_and_Econometrics, "out of 10")

print("Total number of Statistics and Econometrics ECTS:", Stats_and_Econometrics['ECTS'].sum())


# In[13]:


Avg_Econometrics = (8.6+7.6+7)/3

print("Average in Econometrics is", round(Avg_Econometrics, 2), "out of 10")
print("Total number of Econometrics ECTS: 16")


# In[14]:


Quant_Econ = Bachelor["Subject"].isin([Quant_Econ][0])
Quant_Econ = Bachelor[Quant_Econ]
Quant_Econ.sort_values('Grade', ascending=False)


# In[135]:


# Average and number of credits in Quantitative Economics

Avg_Quant_Econ = Quant_Econ['Grade'].mean()
Mdn_Quant_Econ = Quant_Econ['Grade'].median()
print("Average in Quantitative economics is", round(Avg_Quant_Econ, 2), "out of 10")
print("Median in Quantitative economics is", round(Mdn_Quant_Econ, 2), "out of 10")

print("Total number of Quantitative Economics ECTS:", Quant_Econ['ECTS'].sum())


# In[16]:


Mathematics = Bachelor["Subject"].isin([Mathematics][0])
Mathematics = Bachelor[Mathematics]
Mathematics.sort_values('Grade', ascending=False)


# In[137]:


# Average and number of credits in Mathematics

Avg_Mathematics = Mathematics['Grade'].mean()
Mdn_Mathematics = Mathematics['Grade'].median()


print("Average in Mathematics is", Avg_Mathematics, "out of 10")
print("Median in Mathematics is", Mdn_Mathematics, "out of 10")
print("Total number of Mathematics ECTS:", Mathematics['ECTS'].sum())


# In[18]:


Finance = Bachelor["Subject"].isin([Finance][0])
Finance = Bachelor[Finance]
Finance.sort_values('Grade', ascending=False)


# In[145]:


# Average and number of credits in Finance

Avg_Finance = Finance['Grade'].mean()
Mdn_Finance = Finance['Grade'].median()

print("Average in Finance is", round(Avg_Finance,2), "out of 10")
print("Median in Finance is", Mdn_Finance, "out of 10")
print("Total number of Finance ECTS:", Finance['ECTS'].sum())


# In[20]:


Econ = Bachelor["Subject"].isin([Econ][0])
Econ = Bachelor[Econ]
Econ.sort_values('Grade', ascending=False)


# In[146]:


# Average and number of credits in Economics

Avg_Econ = Econ['Grade'].mean()
Mdn_Econ = Econ['Grade'].median()

print("Average in Economics is", round(Avg_Econ, 2), "out of 10")
print("Median in Economics is", round(Mdn_Econ, 2), "out of 10")
print("Total number of Economics ECTS:", Econ['ECTS'].sum())


# In[194]:


# Let's plot how I performed in each category of subjects
Average_Block_Subjcets = [Avg_Stats_and_Econometrics, round(Avg_Finance,2), round(Avg_Quant_Econ, 2), Avg_Mathematics, round(Avg_Econ, 2)]
Labels = ['Statistics and Econometrics','Finance', 'Quantitative Economics', 'Mathematics', 'Economics']

# Create array
y_pos = np.arange(len(Average_Block_Subjcets))

# Size
plt.figure(figsize=(15,8))

# Bars
plt.bar(y_pos, Average_Block_Subjcets, color = (sns.color_palette("Set2")),alpha=0.7 )
 
# Create names on the x-axis
plt.xticks(y_pos, Labels, fontsize=14)

# title
plt.title("Average grade for each category of subjects", fontsize=19)

#Values on top of each bar

xlocs=[i+1 for i in range(0,10)]
xlabs=[i/2 for i in range(0,10)]

for i, v in enumerate(Average_Block_Subjcets):
    plt.text(xlocs[i] - 1.1, v + 0.075, str(v), fontsize=15)


# In[201]:


# Draw Plot
plt.figure(figsize=(16,10), dpi= 80)
sns.kdeplot(Quant_Econ['Grade'], shade=True, color="g", label="Quantitative Economics", alpha=.7)
sns.kdeplot(Finance['Grade'], shade=True, color="yellow", label="Finance", alpha=.7)
sns.kdeplot(Bachelor['Grade'], shade=True, color="blue", label="Average", alpha=1)
sns.kdeplot(Stats_and_Econometrics['Grade'], shade=True, color="red", label="Stats_and_Econometrics", alpha=.7)
sns.kdeplot(Econ['Grade'], shade=True, color="orange", label="Econ", alpha=.35)

# Decoration
plt.title('Density Plot of all categories', fontsize=22)
plt.legend(fontsize=17)
plt.show()


# In[200]:


plt.figure(figsize=(16,10), dpi= 80)

sns.kdeplot(Bachelor['Grade'], shade=True, color="blue", shade_lowest=False, label="Average", alpha=.7)
sns.kdeplot(Stats_and_Econometrics['Grade'], shade=True, color="orange",shade_lowest=False, label="Statistics and Econometrics", alpha=1)
sns.kdeplot(Finance['Grade'], shade=True, color="purple",shade_lowest=False, label="Finance", alpha=0.25)
plt.legend(fontsize=20)

plt.title('Density Plot of Selected Categories ', fontsize=22)

plt.show()

