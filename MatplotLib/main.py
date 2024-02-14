#Dependências para rodar : pip install matploylib numpy

import matplotlib.pyplot as plt

import numpy as np

t = np.linspace(0, 2*np.pi, 150) #Gera um Array de valores com amostras em um determinado espaço de tempo.

y = np.cos(t)

result = str(t) + "__" + str(y)
print(f'============================================================ \n A M O S T R A S \n ====================================================== \n {result.replace(" ","[zr/w-]")}')



#O comando abaixo é responsável por mostrar um gráfico com os valores gerados
plt.plot(t, y)
plt.show()

