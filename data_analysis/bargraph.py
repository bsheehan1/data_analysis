import math
import statistics
import numpy as np
import matplotlib.pyplot as plt

import datastruct
import special

class BarStruct:
    def __init__(self,fp,
                 title='Title,
                 x_axis='X',y_axis='Y')
        datastruct.DataStruct.__init__(self, fp)
        self.title = title
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_values = self.keys
        self.y_values = []
        for key in self.keys:
            X = self.dictionary[key]
            self.y_values.append(np.mean(X))
            self.e_values.append(np.std(X))
        for i in range(1,len(self.keys)):
            X1 = self.dictionary[self.keys[0]]
            X2 = self.dictionary[self.keys[1]]
            t, v = tdist.t_test(X1,X2)
       
        

class BarGraph:
    def __init__(self,title,
                 x_axis,y_axis,
                 x_values,y_values,
                 e_values,p_values):
        self.title = title
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_values = x_values
        self.y_values = y_values
        self.e_values = e_values
        self.p_values = p_values
        
        self.x_pos = np.arange(len(x_values))

    
        fig, ax = plt.subplots()
        ax.bar(x_pos, y_values, yerr=error_values,
               align='center', alpha=1.0, color=['0.0','0.5','0.25','0.75'],
               ecolor='black', capsize=10)
        ax.set_title(self.title)
        ax.set_ylabel(self.y_axis)
        ax.set_xlabel(self.x_axis)
        ax.set_xticks(self.x_pos)
        ax.set_xticklabels(self.x_values)
        ax.axhline(1.0, color="black")

        y_max = (max(y_values) + max(error_values))
        y_min = 0
        ax.set_ylim(y_min,y_max*(1+(len(x_cat))/20))

        for i in range(len(self.x_values)-1):
            y = y_max+(i+1)*y_max*0.05
            ax.annotate("", xy=(0, y), xycoords='data',
                       xytext=(i+1, y), textcoords='data',
                       arrowprops=dict(arrowstyle="-", ec='black'))
            ax.text((i+1)/2, y+y*0.01, self.p_symbol(self.p_values[i]),
                   horizontalalignment='center',
                   verticalalignment='center')
        plt.show()

    def p_symbol(self,p):
        if p > 0.05:
            return 'ns'
        elif 0.01 < p <= 0.05:
            return '*'
        elif 0.005 < p <= 0.01:
            return '**'
        elif 0.001 < p <= 0.005:
            return '***'
        else:
            return '#'

if __name__ == '__main__':
    x = BarStruct('./test/data_dict.txt')
    
