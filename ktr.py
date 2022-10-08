from matplotlib import pyplot as plt, patches   

figure, axes = plt.subplots()
Drawing_colored_circle = patches.Circle((0.5, 0.5 ), 0.2, color='red')
axes.set_aspect( 1 )
axes.add_artist( Drawing_colored_circle )
plt.show()
 