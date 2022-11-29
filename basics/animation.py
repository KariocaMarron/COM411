import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots() # will default 1 to 1

# ax.pl # if using only one

def animate (frame):  # wnats to know the frame number
    #pass
    ax.clear
    ax.scatter(range(frame), range(frame))
    ax.set_xlm(0, 10)
    ax.set_Ylim(0, 10)

ani = animation.FuncAnimation(fig,animate, frames=10, interval=1000 ) # (z, animate --> tels what function to call
plt.show()