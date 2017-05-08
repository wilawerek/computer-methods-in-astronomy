#!usr/bin/python
# Emil Wilawer
# 2017-01-30

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


def func1(phase, H, G):
    '''
    V = H -2.5*np.log10((1-G)*phi1 + G*phi2)
    '''
    phase = phase*np.pi/180.0
    w = np.exp(-90.56*np.tan(0.5*phase)**2)
    phi1 = w*(1 - 0.986*np.sin(phase)/(0.119 + 1.341*np.sin(phase) - 0.754*np.sin(phase)**2)) + (1-w)*np.exp(-3.332*np.tan(0.5*phase)**0.631)
    phi2 = w*(1 - 0.238*np.sin(phase)/(0.119 + 1.341*np.sin(phase) - 0.754*np.sin(phase)**2)) + (1-w)*np.exp(-1.862*np.tan(0.5*phase)**1.218)
    return H -2.5*np.log10((1-G)*phi1 + G*phi2)

def func2(phase, a1, a2):
    '''
    10**(-0.4*V) = a1*phi1 + a2*phi2
    '''
    phase = phase*np.pi/180.0
    w = np.exp(-90.56*np.tan(0.5*phase)**2)
    phi1 = w*(1 - 0.986*np.sin(phase)/(0.119 + 1.341*np.sin(phase) - 0.754*np.sin(phase)**2)) + (1-w)*np.exp(-3.332*np.tan(0.5*phase)**0.631)
    phi2 = w*(1 - 0.238*np.sin(phase)/(0.119 + 1.341*np.sin(phase) - 0.754*np.sin(phase)**2)) + (1-w)*np.exp(-1.862*np.tan(0.5*phase)**1.218)
    return a1*phi1 + a2*phi2

# ----------------------------------------------------------------------

file = open("EAR_A_COMPIL_3_MAGPHASE_V1_0/data/magphase.tab", "r")
phase, Vmag = [], []
asteroid_number = 22
records_number = 12
while True:
    line = file.readline().rstrip().split()
    if int(line[0]) == asteroid_number:
        phase.append(float(line[8]))
        Vmag.append(float(line[11]))
    elif int(line[0]) > asteroid_number:
        phase = np.array(phase)
        Vmag = np.array(Vmag)
        print 'Another asteroid\n'
        print 'ASTEROID: %s %s'%(line[0], line[1])
        break
    if len(phase) == records_number:
        phase = np.array(phase)
        Vmag = np.array(Vmag)
        print 'Length limit\n'
        print 'ASTEROID: %s %s'%(line[0], line[1])
        break

file.close()
print '--- PHASE ---\n',phase, '\n--- Vmag ---\n',Vmag

Vmag2 = np.array([10**(-0.4*x) for x in Vmag])
print '--- Vmag2 ---\n', Vmag2

#------------------------------------------------------------------------
print ''
fig, axes = plt.subplots(nrows=2, ncols=1)
ax1, ax2 = axes.flat

# --- func1 ---
popt1, pcov1 = curve_fit(func1, phase, Vmag)
print '--- POPT 1 --- V = H -2.5*np.log10((1-G)*phi1 + G*phi2)\n', popt1
#y1 = func1(phase, popt1[0], popt1[1])

ax1.set_title('%s %s'%(line[0], line[1]))
ax1.set_ylabel('V [mag]', fontsize='16')
ax1.invert_yaxis()
ax1.plot(phase, Vmag, 'o')
ax1.plot(phase, func1(phase, popt1[0], popt1[1]), 'r-')

ax1.axvline(x=0, linewidth=0, label='H = %f\nG = %f'%(popt1[0], popt1[1]))
ax1.legend(frameon=False, loc='best')


# --- func2 ---
popt2, pcov2 = curve_fit(func2, phase, Vmag2)
print '--- POPT 2 --- 10**(-0.4*V) = a1*phi1 + a2*phi2\n', popt2
H = -2.5*np.log10(popt2[0]+popt2[1])
G = popt2[1]/(popt2[0]+popt2[1])
print 'H = {}\nG = {}'.format(H, G)

ax2.set_xlabel('phase', fontsize='16')
ax2.set_ylabel(r'$10^{-0.4V}$ [mag]', fontsize='16')
ax2.plot(phase, Vmag2, 'o')
ax2.plot(phase, func2(phase, popt2[0], popt2[1]), 'r-')

ax2.axvline(x=0, linewidth=0, label='H = %f\nG = %f'%(H, G))
ax2.legend(frameon=False, loc='best')
plt.show()
