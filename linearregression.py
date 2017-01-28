from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
xs = np.array([1,2,3,4,5,6],dtype=np.float64)
ys = np.array([4,5,6,7,8,9],dtype=np.float64)




def best_fit_slope_intercept(xs,ys):
    m=((mean(xs)*mean(ys))-mean(xs*ys))/(mean(xs)**2 - mean(xs*xs))
    b = mean(ys) - m*mean(xs)
    return m,b

def squared_error(ys_orig,ys_line):
    return sum((ys_orig-ys_line)**2)

def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig,ys_line)
    squared_error_y_mean = squared_error(ys_orig,y_mean_line)
    return 1-(squared_error_regr/squared_error_y_mean)

m,b= best_fit_slope_intercept(xs,ys)

regression_line = [(m*x+b) for x in xs]

predict_x = 8
predict_y = predict_x*m +b
print(predict_y)
print coefficient_of_determination(ys,regression_line)



print(m)
print(b)
