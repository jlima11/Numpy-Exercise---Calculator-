import numpy as np

#creating a fuction to give the mean, variance, standard deviation, max, min, and sum in a 3x3 matrix.
def calculate(list): #fuction
  if (len(list) != 9):
    raise ValueError("List must contain nine numbers.")
  else:
    m = np.reshape(list,[3,3])
    
   #média
    me1 = np.average(m, axis=0) 
    me2 = np.average(m, axis=1)
    me3 = np.average(m)
    
    #variância
    v1 = np.var(m,axis =0)
    v2 = np.var(m,axis =1)
    v3 = np.var(m)
    
    #desvio padrão
    dp1 = np.std(m,axis=0)
    dp2 = np.std(m,axis=1)
    dp3 = np.std(m)
    
    
    #max
    ma1 = np.max(m,axis=0)
    ma2 = np.max(m,axis=1)
    ma3 = np.max(m)
    
    #min
    mi1 = np.min(m,axis=0)
    mi2 = np.min(m,axis=1)
    mi3 = np.min(m)
    
    #soma
    s1 = np.sum(m,axis=0)
    s2 = np.sum(m,axis=1)
    s3 = np.sum(m)
    
    #building the dictionary
    dicio = {
      'mean':     
      [me1.tolist(),me2.tolist(),me3],
      'variance': 
      [v1.tolist(),v2.tolist(),v3],
      'standard deviation': 
      [dp1.tolist(),dp2.tolist(),dp3],
      'max':   
      [ma1.tolist(),ma2.tolist(),ma3],
      'min': 
      [mi1.tolist(),mi2.tolist(),mi3],
      'sum': [s1.tolist(),s2.tolist(),s3]
    }
    #especificar numero de elemtos
  
    return dicio
