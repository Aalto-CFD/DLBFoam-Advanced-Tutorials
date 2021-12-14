import numpy as np

U  = 49.6       # [m/s] - Velocity at the inlet (experimental, probably based on mass flux)
L  = 7.2e-03    # [m]   - Characteristic length, main jet inlet diameter

###########################################
# Numbers of modes are set according to [1]
###########################################
m_a = 2     # oscillating axisymmetric
m_f = 6     # rotating helical
m_total = m_f + m_a

###################################################
# A [m/s] - amplitude of a mode
# A = kA * u'_in = 0.5 * u'_{in} - according to [1]
###################################################
k_A = 0.5

#########################################################
# alpha [rad] - initial shifts.
# Are set random (according to [1]) in the range [0, 2*pi]
#########################################################
alpha_a = np.random.random(m_a)*2*np.pi
alpha_f = np.random.random(m_f)*2*np.pi

########################################################
# Psi [rad/s] - mode's frequency
# Introducing some randomness (according to [1]),
# so the Strouhal numbers will correspond to the ranges:
# St_a = 0.4-0.7
# St_f = St_a/2 = 0.2-0.35 [2]
# with uniform distribution
########################################################
St_a = ( 0.3*np.random.random(m_a) + 0.4 )       # mean: 0.55
St_f = ( 0.3*np.random.random(m_f) + 0.4 ) / 2   # mean: 0.55/2 = 0.275

Psi_a = 2*np.pi*St_a*U/L
Psi_f = 2*np.pi*St_f*U/L

#####################
# Write values to 0/U
#####################
with open('0/U', 'r') as file :
  filedata = file.read()

alpha = list(alpha_f) + list(alpha_a)
Psi = list(Psi_f) + list(Psi_a)

formatted_alpha = ', '.join(str(k) for k in alpha)
formatted_psi = ', '.join(str(k) for k in Psi)
filedata = filedata.replace('ALPHA_TO_BE_GENERATED_BY_PYTHON_SCRIPT', formatted_alpha)
filedata = filedata.replace('PSI_TO_BE_GENERATED_BY_PYTHON_SCRIPT', formatted_psi)

with open('0/U', 'w') as file:
  file.write(filedata)

########################################
# Print report (!!!TODO!!!: REMOVE ON RELEASE)
########################################
import pandas as pd
print(f"k_A={k_A:.4}")
modes_df = pd.DataFrame(columns = ['m', 'alpha', 'St', 'Psi'])
for i in range(m_f):
    modes_df = modes_df.append({'m':+(i+1), 'alpha':alpha_f[i], 'St':St_f[i], 'Psi':Psi_f[i]}, ignore_index=True)
for i in range(m_a):
    modes_df = modes_df.append({'m':     0, 'alpha':alpha_a[i], 'St':St_a[i], 'Psi':Psi_a[i]}, ignore_index=True)
print(modes_df)


# Bibliography:
# 1. Pitsch, H., & Steiner, H. (2000). Large-eddy simulation of a turbulent piloted methane/air diffusion flame (Sandia flame D). Physics of fluids, 12(10), 2541-2554.
# 2. Danaila, I., & Boersma, B. J. (1998). Mode interaction in a forced homogeneous jet at low Reynolds numbers. In Proceedings of the summer program (pp. 141-158).
# 3. Danaila, I., & Boersma, B. J. (2000). Direct numerical simulation of bifurcating jets. Physics of fluids, 12(5), 1255-1257.
