import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
tweet_output = "/home/subhakr/PycharmProjects/Learning NLTK/twitter_output/"

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    pullData = open(tweet_output + "twitter-out.txt", "r").read()
    lines = pullData.split('\n')
    xar = []
    yar = []
    x, y = 0, 0

    for l in lines[-200:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.plot(xar, yar)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
