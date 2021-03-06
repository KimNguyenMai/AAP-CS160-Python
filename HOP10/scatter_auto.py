import matplotlib.pylab as plt

x_values = range(0,50)
y_values = [x*5 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s = 30)

#set chart tittle and label axes
ax.set_title("Multiple of 5", fontsize = 24)
ax.set_xlabel("Values", fontsize = 14)
ax.set_ylabel("Multi Values", fontsize = 14)

#set size of tick labels
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()