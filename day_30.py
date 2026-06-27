'''
matplotlib
----------
--> This provides various plots and customization options to make any visualizations more meaningful.\

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[10,20,10,40,50,60]
plt.plot(x,y)
plt.show()

basic structure:
    axis=(X,Y)
    title-(Title)

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[3,19,7,2,15,9]
plt.xlabel('Overs')
plt.ylabel('Score')
plt.plot(x,y)
plt.title('CSK Score')
plt.show()

>>Bar chart/plot :

import matplotlib.pyplot as plt
m=[2500,1500,2200,3000]
st=[2023,2024,2025,2026]
plt.bar(st,m,color='green')
plt.ylabel('No.of Car Sales')
plt.xlabel('year')
plt.title('BMW')
plt.show()

import matplotlib.pyplot as plt
s=['python','SQL','Flask']
st=[20,5,20]
plt.pie(st,labels=s)
plt.title('courses')
plt.legend(st)
plt.show()

'''

import matplotlib.pyplot as plt
marks= [2500, 1500,2208,3000]
stud= [2023, 2824,2025, 2026]
plt.scatter(stud,marks,color='green')
plt.ylabel('No.of Car Sales')
plt.xlabel('Year')
plt.title('BMW')
plt.show()
