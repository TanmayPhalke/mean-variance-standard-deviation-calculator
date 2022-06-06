import numpy as np

def calculate(list):
  calculations = dict()
  ip_arr = np.array(list)
  try:
    ip_arr = ip_arr.reshape(3,3)
  except ValueError:
    raise ValueError("List must contain nine numbers.")
    
  #Calculating mean for axis=0,1 and flattened list
  mean_a0 = np.mean(ip_arr,axis=0).tolist()
  mean_a1 = np.mean(ip_arr,axis=1).tolist()
  mean_f = np.mean(ip_arr)
  mean_calc = [mean_a0, mean_a1, mean_f]
  #Calculating variance for axis=0,1 and flattened list
  var_a0 = np.var(ip_arr,axis=0).tolist()
  var_a1 = np.var(ip_arr,axis=1).tolist()
  var_f = np.var(ip_arr)
  var_calc = [var_a0, var_a1, var_f]
  #Calcuating sd for axis=0,1 and flattened list
  sd_a0 = np.std(ip_arr,axis=0).tolist()
  sd_a1 = np.std(ip_arr,axis=1).tolist()
  sd_f = np.std(ip_arr)
  sd_calc = [sd_a0, sd_a1, sd_f]
  #max
  max_a0 = np.max(ip_arr, axis=0).tolist()
  max_a1 = np.max(ip_arr, axis=1).tolist()
  max_f = np.max(ip_arr)
  max_calc = [max_a0, max_a1, max_f]
  #min
  min_a0 = np.min(ip_arr, axis=0).tolist()
  min_a1 = np.min(ip_arr, axis=1).tolist()
  min_f = np.min(ip_arr)
  min_calc = [min_a0, min_a1, min_f]
  #sum
  sum_a0 = np.sum(ip_arr, axis=0).tolist()
  sum_a1 = np.sum(ip_arr, axis=1).tolist()
  sum_f = np.sum(ip_arr)
  sum_calc = [sum_a0, sum_a1, sum_f]
  calculations = {
                  'mean':mean_calc,
                  'variance':var_calc,
                  "standard deviation": sd_calc,
                  "max":max_calc,
                  "min":min_calc,
                  "sum":sum_calc
                  }
  return calculations