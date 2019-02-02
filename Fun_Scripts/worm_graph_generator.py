import numpy as np, matplotlib.pyplot as plt

worms = np.genfromtxt('.txt', delimiter='\t', dtype=float, skip_header=True)


for i in range(worms.shape[0]):
    for j in range(worms.shape[1]):
        if np.isnan(worms[i][j]):
            worms[i][j] = -2


# Keep this line uncommented for population chart.
# Comment it out to see individual worm behavior.

worms = np.sort(-worms, axis=0)#here @ the 0 is where it is organized by column, you can put in 1 and allocate by row.

cmap = plt.cm.viridis
cmap.set_over(color='black', alpha=1)

plt.pcolormesh(worms, cmap='viridis', vmin=-1, vmax=1)

cbar = plt.colorbar(ticks=[-1,0,1], orientation= 'horizontal')
cbar.ax.set_xticklabels(['Forward', 'Stationary', 'Backward'])  # horizontal oriented colorbar

plt.savefig('worm raster.png', bbox_inches='tight', dpi=300)
plt.show()

worms = -worms
backward = 0
pause = 0
forward = 0
other = 0
for i in range(worms.shape[0]):
    for j in range(worms.shape[1]):
        if worms[i][j] == -1:
            backward += 1
        elif worms[i][j] == 0:
            pause += 1 
        elif worms[i][j] == 1:
            forward += 1 
        elif not worms[i][j] == -2:    
            other += 1

Total = backward + forward + pause + other
backward = backward / Total
forward = forward / Total
pause = pause / Total
other = other / Total
print('Backward', round(backward,5))
print('Forward', round(forward, 5))
print('Paused', round(pause, 5))
print('Other', round(other, 5))
'''
worms.shape = (318,3)
depth = worms[:,0]
florescence = worms[:1]-worms[:2]
plt.plot([depth], [florescence])
plt.axis([0, depth, 0, florescence])
plt.show()
