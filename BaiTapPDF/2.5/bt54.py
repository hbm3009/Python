import numpy as np
n=np.random.choice([0,1],size=1000)
s=np.sum(n==0)
ng=np.sum(n==1)
print(f"Sap: {s} lan ({s/10:.1f}%), Ngua: {ng} lan ({ng/10:.1f}%)")