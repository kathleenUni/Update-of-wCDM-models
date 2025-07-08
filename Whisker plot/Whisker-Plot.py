###
# Code obtained from: https://github.com/lucavisinelli/H0TensionRealm
# Repository created by Luca Visinelli
###

import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

black = [0,0,0,0]
red   = [1,0,0,0]
blue  = [0,0,1,0]

#+++++++++++++++++++++++++++++
from matplotlib import rcParams
config = {
	"mathtext.fontset":'dejavusans'
	}
rcParams.update(config)
#+++++++++++++++++++++++++++++

class ErrorLinePloter:
    def __init__(self,data,position):
        self.data = data
        self.position = position

# Horizontal line
        self.hlwidth = 0.8
        self.hlstyle = '-'
        self.hlcolor = red

# Point props
        self.point_size = 0.34
        self.point_color = blue
        self.point_lwidth = 0.8 
        
        self.middle_point_type = 'line'
        self.middle_point_size=self.point_size
        self.middle_point_color=self.point_color

        self.middle_point_lwidth=self.point_lwidth
        self.middle_point_mshape='o'

    def set_props(self,hlwidth,hlstyle,hlcolor,
                    psize,pcolor,pwidth,
                    middle_point_type='line',
                    **lmprop):

        self.hlwidth=hlwidth
        self.hlstyle=hlstyle
        self.hlcolor=hlcolor
        self.point_size = psize
        self.point_color = pcolor
        self.point_lwidth = pwidth
        
        self.middle_point_size = psize
        self.middle_point_color= pcolor
        self.middle_point_type=middle_point_type
        if middle_point_type == 'line':
            if len(lmprop)!=0:
                self.middle_point_size=lmprop['mpsize']
                self.middle_point_color=lmprop['mpcolor']
                self.middle_point_lwidth=lmprop['lwidth']
        elif middle_point_type == 'marker':
            if len(lmprop)!=0:
                self.middle_point_size=lmprop['mpsize']
                self.middle_point_color=lmprop['mpcolor']
                self.middle_point_mshape=lmprop['mshape']

    def plot(self, i, j, xmin, xmax, param, param_sig):
        list_3=[self.data[param]-self.data[param_sig][1],
                self.data[param],
                self.data[param]+self.data[param_sig][0]]
        #print(list_3)
        
        xlen = xmax - xmin
        x_pos_mid = (list_3[1] - xmin)/xlen
        x_pos_left = x_pos_mid - (list_3[1]-list_3[0])/xlen
        x_pos_right = x_pos_mid + (list_3[2]-list_3[1])/xlen

        axes[i][j].axhline(y=self.position,xmin=x_pos_left,
                           xmax=x_pos_right,
                           color=self.hlcolor,ls=self.hlstyle,
                           lw=self.hlwidth)
        #print(axes[i][j])
        if self.middle_point_type == 'line':
            axes[i][j].axvline(x=list_3[1],
                    ymin=self.position-self.middle_point_size/2,
                    ymax=self.position+self.middle_point_size/2,
                    color=self.middle_point_color,
                    ls='-',
                    lw=self.middle_point_lwidth,
                    zorder=3)
            
        elif self.middle_point_type == 'marker':
            axes[i][j].scatter(list_3[1],self.position,
                    s=self.middle_point_size,
                    color=self.middle_point_color,
                    marker=self.middle_point_mshape)
            

### Repository containing the .csv with the dataset
### See README for more info on the structure
fil = 'dataset_PR4&PR3.csv'

### Load the dataset and count the number of data points
nr=1
with open(fil, 'r+') as file:
    reader = csv.reader(file)
    first_line = file.readline()
    next(reader, None)
    for row in reader:
        nr += 1
    nc = first_line.count(',')+1

### Load the data points into arrays
w0 = np.zeros(nr)
w0l = np.zeros(nr)
w0p = np.zeros(nr) 
wa = np.zeros(nr)
wal = np.zeros(nr)
wap = np.zeros(nr)
H0 = np.zeros(nr)
Hl = np.zeros(nr)
Hp = np.zeros(nr)
Sigma_8 = np.zeros(nr)
Sigma_8l = np.zeros(nr)
Sigma_8p = np.zeros(nr)
label = ["" for x in range(nr)]

i=0
with open(fil, 'r+') as file:
    reader = csv.reader(file)
    next(reader, None)
    #print(row)
    for row in reader:
        label[i] = row[0]

        w0[i] = float(row[1])
        w0l[i] = float(row[2])
        w0p[i] = float(row[3])
        
        if row[4] == 'None':
            wa[i] = None
            
        if row[5] == 'None':
            wal[i] = None   
            
        if row[6] == 'None':
            wap[i] = None    
        else:    
            wa[i] = float(row[4])
            wal[i] = float(row[5])
            wap[i] = float(row[6])
        
        H0[i] = float(row[7])
        #print(H0[i])
        Hl[i] = float(row[8])
        Hp[i] = float(row[9])

        Sigma_8[i] = float(row[10])
        #print(Sigma_8[i])
        Sigma_8l[i] = float(row[11])
        Sigma_8p[i] = float(row[12])
        i += 1

#---------------------------label-------------------------------------
paras=[]
for i in range(nr):
    if label[i] == "LambdaCDM":
        paras.append("\\Lambda\\mathrm{CDM}")
    elif label[i] == "w0CDM":
        paras.append("w_{0}\\mathrm{CDM}")
    elif label[i] == "CPL":
        paras.append("\\mathrm{CPL}")
    elif label[i] == "JBP":
        paras.append("\\mathrm{JBP}")
    elif label[i] == "GE":
        paras.append("\\mathrm{GE}")
    elif label[i] == "BA":
        paras.append("\\mathrm{BA}")
    elif label[i] == "OSCILL":
        paras.append("\\mathrm{OSCILL}")
    else:
        paras.append("\\mathrm{{\\bf{{{x}}}}}".format(x=label[i]))


#---------------------------data-------------------------------------
data_H0 = []
data_Sigma_8 = []
data_w0 = []
data_wa = []
for i in range(nr):
    data_w0.append({'ml_w0':w0[i],'e1_sig_w0':[w0p[i],w0l[i]]})
    data_wa.append({'ml_wa':wa[i],'e1_sig_wa':[wap[i],wal[i]]})
    data_H0.append({'ml_H0':H0[i],'e1_sig_H0':[Hp[i],Hl[i]]})
    data_Sigma_8.append({'ml_Sigma_8':Sigma_8[i],'e1_sig_Sigma_8':[Sigma_8p[i],Sigma_8l[i]]})

all_data = [data_w0, data_wa, data_H0, data_Sigma_8]
#print(all_data)
#---------------------------style-------------------------------------
#number of rows in excel is saved as nr
#num_pos is the number of models + label + 2 for gap above and gap below
num_pos = 10  #int(((nr+4)/4))+2
#print(num_pos)
positions = []

labels_row1 = []
labels_row2 = []
labels_row3 = []
labels_row4 = []
labels_row5 = []
labels_row6 = []

for i in range(num_pos):
    positions.append(i)
    labels_row1.append('')
    labels_row2.append('')
    labels_row3.append('')
    labels_row4.append('')
    labels_row5.append('')
    labels_row6.append('')

labels=[labels_row1, labels_row2, labels_row3, labels_row4, labels_row5, labels_row6]

#---------------------------plot-------------------------------------#
fig, axes = plt.subplots(nrows=6, ncols=4,figsize=(8.3,11.7))

colours = ["darkviolet","blue","brown", "orange", "black", "darkgreen"]
params = ['ml_w0', 'ml_wa', "ml_H0", "ml_Sigma_8"]
params_sig = ['e1_sig_w0', 'e1_sig_wa', 'e1_sig_H0', 'e1_sig_Sigma_8']
x_mins = [-3, -3, 55, 0.4]
x_maxs = [1, 4, 125, 1.5]

### Plot each data point with attached label
#rows
for j in range(6):
    #columns
    for k in range(4):
        for i in range(num_pos):
            #the value of i is 1 less the number of num_pos
            if 7-i == 7:
                continue

            elif 7 > 7-i > 1:
                elp = ErrorLinePloter(all_data[k][(j*5)+i-1],position=7-i)
                labels[j][elp.position]=paras[(j*5)+i-1]
                elp.set_props(0.7,'-',colours[j],
                    0.7,colours[j],0.5,
                    'marker',mpsize=5.0,mpcolor=colours[j],mshape='o')
                elp.plot(j,k,x_mins[k],x_maxs[k], params[k], params_sig[k])

            elif 7-i == 1:
                continue

            elif 1 > 7-i > 0:
                elp = ErrorLinePloter(all_data[k][(j*5)+i-1],position=7-i)
                labels[j][elp.position]=paras[(j*5)+i-1]
                elp.set_props(0.7,'-',colours[j],
                    0.7,colours[j],0.7,
                    'marker',mpsize=6.0,mpcolor=colours[j],mshape='o')
                elp.plot(j,k,x_mins[k],x_maxs[k], params[k], params_sig[k])
            else:
                continue


xlims = [[x_mins[0],x_maxs[0]],[x_mins[1],x_maxs[1]],[x_mins[2],x_maxs[2]], [x_mins[3],x_maxs[3]]]
x_ticks = [[i for i in range(-3, 1, 1)],
           [i for i in range(-3, 4, 1)], 
           [i for i in range(50, 120, 10)],
           [ 0.6, 0.8, 1.0, 1.2, 1.4]]

# setting the x axis/ticks for bottom row
#columns
for i in range(4):
    axes[5][i].tick_params(axis='x',labelsize=8)
    axes[5][i].set_xticks(x_ticks[i])
    #print(x_ticks[i])
    axes[5][i].set_xlim(xlims[i])
    #print(axes[2][3])


# setting the x axis/ticks for other (that need to be empty)
#rows-1
for i in range(5):
    #columns
    for j in range(4):
        axes[i][j].set_xticks([])
        axes[i][j].set_xlim(xlims[j])

x_ticks = [['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)]]
#print(num_pos)
#rows
for i in range(6):
    for j in range(num_pos):#9):
        if labels[i][j] == '':
            #print(i, j)
            x_ticks[i][j] = ''
        else:
            x_ticks[i][j] = "${x}$".format(x=labels[i][j])

# setting the y axis/ticks for first column
dataset_titles = [
    "PR3", "PR4", "PR3+ CC + SN+SH0ES", "PR4 + CC + SN+SH0ES", "PR3+ CC + SN+SH0ES + DESI" , "PR4+CC+SN+SH0ES + DESI"
]
#dataset_titles = [
    #"PR4", "PR4", "PR4"
#]
#dataset_titles_2 = [
    #"+ CC + SN+SH0ES", "+ CC + SN+SH0ES", " + DESI"
#]
for i in range(len(dataset_titles)):
    x_ticks[i][-1]= "$\\mathrm{\\bf{"+str(dataset_titles[i])+"}}$"
    #print(x_ticks[i][-1])
    #if i == 1:
       # x_ticks[i][-1]= "$\\mathrm{\\bf{"+str(dataset_titles[i])+"}}$"
        #x_ticks[i][-2]= "$\\mathrm{\\bf{"+str(dataset_titles_2[i-1])+"}}$"
    #if i == 2:
        #x_ticks[i][-1]= "$\\mathrm{\\bf{"+str(dataset_titles[i])+"}}$"
        #x_ticks[i][-2]= "$\\mathrm{\\bf{"+str(dataset_titles_2[i-1])+"}}$"
        #x_ticks[i][-3]= "$\\mathrm{\\bf{"+str(dataset_titles_2[i])+"}}$"
    
for i in range(6):
    axes[i][0].tick_params(axis='y',labelsize=8)
    axes[i][0].set_yticks(positions,
    [r"{x}".format(x=x_ticks[i][k]) for k in range(num_pos)])
    axes[i][0].set_ylim(0,10)

# setting the y axis/ticks for other (that need to be empty)
for i in range(6):
    for j in range(3):
        axes[i][j+1].set_yticks([])
        axes[i][j+1].set_ylim(0,10)

axes[0][0].set_title(r"$w_{0}$")
axes[0][1].set_title(r"$w_{a}$")
axes[0][2].set_title(r"$H_{0}\;[\mathrm{km\;s^{-1}\;Mpc^{-1}}]$")
axes[0][3].set_title(r"$\sigma_8$")

axes[0][0].set_yticks(positions, 
    [r"{x}".format(x=x_ticks[0][k]) for k in range(num_pos)])


#print(x_ticks[0])
#print the verticle SH0ES and Planck 2018 H0 values with their uncertainty
#this is what the original code has (the one in github)

#Now plt.bar works when you only have one coloumn 
##but it does not when you have multiple 

#plt.bar(73.2, 100, width=2.6, facecolor = 'cyan', alpha = 0.15)
#plt.bar(67.27, 100, width=1.2, facecolor = 'pink', alpha = 0.25)

#This is what I am trying to fix it
for i in range(6):
    #For H0
    axes[i][2].axvspan(73.2 - 1.3, 73.2 + 1.3, color='purple', alpha=0.15)    #SH0ES
    axes[i][2].axvspan(67.4 - 0.5, 67.4 + 0.5, color='green', alpha=0.25)  # Planck 2018
    
    #For sigma8
    #axes[i][3].axvspan(73.2 - 1.3, 73.2 + 1.3, color='cyan', alpha=0.15)    #SH0ES
    axes[i][3].axvspan(0.811  - 0.006, 0.811  + 0.006, color='green', alpha=0.25)  # Planck 2018
    
plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig("wCDM Whisker Plot PR4 & PR3.png", dpi=2500)
plt.savefig("wCDM Whisker Plot PR4 & PR3.pdf", dpi=2500)

########################################################################################################
############################BACK#################################################
### Repository containing the .csv with the dataset
### See README for more info on the structure
fil = 'dataset_BACK.csv'

### Load the dataset and count the number of data points
nr=1
with open(fil, 'r+') as file:
    reader = csv.reader(file)
    first_line = file.readline()
    next(reader, None)
    for row in reader:
        nr += 1
    nc = first_line.count(',')+1

### Load the data points into arrays
w0 = np.zeros(nr)
w0l = np.zeros(nr)
w0p = np.zeros(nr) 
wa = np.zeros(nr)
wal = np.zeros(nr)
wap = np.zeros(nr)
H0 = np.zeros(nr)
Hl = np.zeros(nr)
Hp = np.zeros(nr)
label = ["" for x in range(nr)]

i=0
with open(fil, 'r+') as file:
    reader = csv.reader(file)
    next(reader, None)
    #print(row)
    for row in reader:
        label[i] = row[0]

        w0[i] = float(row[1])
        w0l[i] = float(row[2])
        w0p[i] = float(row[3])
        
        if row[4] == 'None':
            wa[i] = None
            
        if row[5] == 'None':
            wal[i] = None   
            
        if row[6] == 'None':
            wap[i] = None    
        else:    
            wa[i] = float(row[4])
            wal[i] = float(row[5])
            wap[i] = float(row[6])
        
        H0[i] = float(row[7])
        #print(H0[i])
        Hl[i] = float(row[8])
        Hp[i] = float(row[9])
        i += 1

#---------------------------label-------------------------------------
paras=[]
for i in range(nr):
    if label[i] == "LambdaCDM":
        paras.append("\\Lambda\\mathrm{CDM}")
    elif label[i] == "w0CDM":
        paras.append("w_{0}\\mathrm{CDM}")
    elif label[i] == "CPL":
        paras.append("\\mathrm{CPL}")
    elif label[i] == "JBP":
        paras.append("\\mathrm{JBP}")
    elif label[i] == "GE":
        paras.append("\\mathrm{GE}")
    elif label[i] == "BA":
        paras.append("\\mathrm{BA}")
    elif label[i] == "OSCILL":
        paras.append("\\mathrm{OSCILL}")
    else:
        paras.append("\\mathrm{{\\bf{{{x}}}}}".format(x=label[i]))


#---------------------------data-------------------------------------
data_H0 = []
data_w0 = []
data_wa = []
for i in range(nr):
    data_w0.append({'ml_w0':w0[i],'e1_sig_w0':[w0p[i],w0l[i]]})
    data_wa.append({'ml_wa':wa[i],'e1_sig_wa':[wap[i],wal[i]]})
    data_H0.append({'ml_H0':H0[i],'e1_sig_H0':[Hp[i],Hl[i]]})

all_data = [data_w0, data_wa, data_H0]
#print(all_data)
#---------------------------style-------------------------------------
#number of rows in excel is saved as nr
#num_pos is the number of models + label + 2 for gap above and gap below
num_pos = 10  #int(((nr+4)/4))+2
#print(num_pos)
positions = []

labels_row1 = []
labels_row2 = []
labels_row3 = []
labels_row4 = []
labels_row5 = []
labels_row6 = []

for i in range(num_pos):
    positions.append(i)
    labels_row1.append('')
    labels_row2.append('')
    labels_row3.append('')

labels=[labels_row1, labels_row2, labels_row3]

#---------------------------plot-------------------------------------#
fig, axes = plt.subplots(nrows=3, ncols=3,figsize=(8.3,11.7))

colours = ["darkviolet","blue","brown"]
params = ['ml_w0', 'ml_wa', "ml_H0"]
params_sig = ['e1_sig_w0', 'e1_sig_wa', 'e1_sig_H0']
x_mins = [-3, -3, 64]
x_maxs = [1, 3, 80]

### Plot each data point with attached label
#rows
for j in range(3):
    #columns
    for k in range(3):
        for i in range(num_pos):
            #the value of i is 1 less the number of num_pos
            if 7-i == 7:
                continue

            elif 7 > 7-i > 1:
                elp = ErrorLinePloter(all_data[k][(j*5)+i-1],position=7-i)
                labels[j][elp.position]=paras[(j*5)+i-1]
                elp.set_props(0.5,'-',colours[j],
                    0.5,colours[j],0.5,
                    'marker',mpsize=5.0,mpcolor=colours[j],mshape='o')
                elp.plot(j,k,x_mins[k],x_maxs[k], params[k], params_sig[k])

            elif 7-i == 1:
                continue

            elif 1 > 7-i > 0:
                elp = ErrorLinePloter(all_data[k][(j*5)+i-1],position=7-i)
                labels[j][elp.position]=paras[(j*5)+i-1]
                elp.set_props(0.5,'-',colours[j],
                    0.5,colours[j],0.5,
                    'marker',mpsize=5.0,mpcolor=colours[j],mshape='o')
                elp.plot(j,k,x_mins[k],x_maxs[k], params[k], params_sig[k])
            else:
                continue


xlims = [[x_mins[0],x_maxs[0]],[x_mins[1],x_maxs[1]],[x_mins[2],x_maxs[2]]]
x_ticks = [[i for i in range(-3, 1, 1)],
           [i for i in range(-3, 3, 1)], 
           [i for i in range(60, 80, 2)]]


# setting the x axis/ticks for bottom row
#columns
for i in range(3):
    axes[2][i].tick_params(axis='x',labelsize=8)
    axes[2][i].set_xticks(x_ticks[i])
    #print(x_ticks[i])
    axes[2][i].set_xlim(xlims[i])
    #print(axes[2][3])


# setting the x axis/ticks for other (that need to be empty)
#rows-1
for i in range(3):
    #columns
    for j in range(3):
        axes[i][j].set_xticks([])
        axes[i][j].set_xlim(xlims[j])

x_ticks = [['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)],
           ['' for i in range(num_pos)]]
#print(num_pos)
#rows
for i in range(3):
    for j in range(num_pos):#9):
        if labels[i][j] == '':
            #print(i, j)
            x_ticks[i][j] = ''
        else:
            x_ticks[i][j] = "${x}$".format(x=labels[i][j])

# setting the y axis/ticks for first column
dataset_titles = [
    "CC +SN+SH0ES", " CC + SN+SH0ES + BAO", "CC SN+SH0ES + DESI"]
#dataset_titles = [
    #"PR4", "PR4", "PR4"
#]
#dataset_titles_2 = [
    #"+ CC + SN+SH0ES", "+ CC + SN+SH0ES", " + DESI"
#]
for i in range(len(dataset_titles)):
    x_ticks[i][-1]= "$\\mathrm{\\bf{"+str(dataset_titles[i])+"}}$"
    #print(x_ticks[i][-1])
    #if i == 1:
       # x_ticks[i][-1]= "$\\mathrm{\\bf{"+str(dataset_titles[i])+"}}$"
        #x_ticks[i][-2]= "$\\mathrm{\\bf{"+str(dataset_titles_2[i-1])+"}}$"
    #if i == 2:
        #x_ticks[i][-1]= "$\\mathrm{\\bf{"+str(dataset_titles[i])+"}}$"
        #x_ticks[i][-2]= "$\\mathrm{\\bf{"+str(dataset_titles_2[i-1])+"}}$"
        #x_ticks[i][-3]= "$\\mathrm{\\bf{"+str(dataset_titles_2[i])+"}}$"
    
for i in range(3):
    axes[i][0].tick_params(axis='y',labelsize=8)
    axes[i][0].set_yticks(positions,
    [r"{x}".format(x=x_ticks[i][k]) for k in range(num_pos)])
    axes[i][0].set_ylim(0,10)

# setting the y axis/ticks for other (that need to be empty)
for i in range(3):
    for j in range(2):
        axes[i][j+1].set_yticks([])
        axes[i][j+1].set_ylim(0,10)

axes[0][0].set_title(r"$w_{0}$")
axes[0][1].set_title(r"$w_{a}$")
axes[0][2].set_title(r"$H_{0}\;[\mathrm{km\;s^{-1}\;Mpc^{-1}}]$")


axes[0][0].set_yticks(positions, 
    [r"{x}".format(x=x_ticks[0][k]) for k in range(num_pos)])

#print the verticle SH0ES and Planck 2018 H0 values with their uncertainty
#this is what the original code has (the one in github)

#Now plt.bar works when you only have one coloumn 
##but it does not when you have multiple 

#plt.bar(73.2, 100, width=2.6, facecolor = 'cyan', alpha = 0.15)
#plt.bar(67.27, 100, width=1.2, facecolor = 'pink', alpha = 0.25)

#This is what I am trying to fix it
for i in range(3):
    #For H0
    axes[i][2].axvspan(73.2 - 1.3, 73.2 + 1.3, color='purple', alpha=0.15)    #SH0ES
    axes[i][2].axvspan(67.4 - 0.5, 67.4 + 0.5, color='cyan', alpha=0.25)  # Planck 2018
    
#print(x_ticks[0])

plt.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig("wCDM Whisker Plot BACK.png", dpi=2500)
plt.savefig("wCDM Whisker Plot BACK.pdf", dpi=2500)

###############################################