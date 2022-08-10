import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5,6,7])
y=np.array([1,2,3,5,8,13,20])

print("Q2: Create a one line chart using two arrays. The first array represents x and the second array represents y:\n",x,y,"\n")
#Q3: Create a two lines chart using the same previous arrays.
plt.plot(x,linestyle ="dotted",markersize=10,linewidth=3)
plt.plot(y,linestyle ="--",linewidth=3)
plt.legend(['Normal','Fast'],loc="upper left")
plt.show()
#Q4: Display multiple linear charts in one row using the charts given below.
plt.figure(figsize=[20,10])
plt.suptitle("my data visulaization assignment")
plt.subplot(1,3,1)
plt.title("red")
x_plot1 = np.array([1, 2, 3, 4, 5, 6, 7])
y_plot1 = np.array([1, 1, 2, 3, 5, 8, 13])
plt.plot(x_plot1,y_plot1,c='r')
plt.subplot(1,3,2)
plt.title("blue")
x_plot2 = np.array([0, 1, 2, 3, 4, 5, 6])
y_plot2 = np.array([2, 4, 6, 8, 10, 12, 14])
plt.plot(x_plot2,y_plot2,c='b')

plt.subplot(1,3,3)
plt.title("green")
x_plot3 = np.array([0, 1, 3, 4])
y_plot3 = np.array([4, 6, 3, 4])
plt.plot(x_plot3,y_plot3,c='g')
plt.show()
#Q5: Define an array that has a values of your top three TV series and define another array to hold the rating of the three TV series out of 10.
#    Create a bar chart using the two arrays.

top_tv=['one pice','demon slayer','kingdom']
rating=[10,8,10]
plt.bar(top_tv,rating,color='b',width=0.5)
plt.show()
#Q6: Create a scatter plot using two arrays. The first array represents carAge and the second array represents carSpeed,
#    set a specific color for each dot by using an array of different colors and add labels for the plot
carAge =[5,7,8,7,2,17,2,9,4,11]
carSpeed=[99,86,87,88,111,86,103,87,94,78]
col=["red","blue","green","lightcoral","darkorange","olive","teal","violet","skyblue","black"]
plt.scatter(carAge,carSpeed,c=col,s=350,alpha=0.4)
plt.xlabel("Car Age")
plt.ylabel("Car Speed")
plt.show()
#Q7: Create a pie chart using two arrays.
#    The first array represents python_libraries and the second array represents your skills out of 10 at each library
arr1=['NumPy','Pandas','Matplotlib','Seaborn','Plotly','Scikit-learn']
arr2=[7,8,9,5,5,8]
plt.pie(arr2,labels=arr1,colors=col,shadow=True)
plt.show()
#Q8: Create a histogram with 250 values and 15 bars
x_hist = np.random.randn(250)
plt.hist(x,15)
plt.show()