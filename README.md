# Update-of-wCDM-models

Link to the paper: 

In this paper, CLASS and MontePython were used. This repository contains the constant (w0CDM) model, the quadratic model (Jassal-Bagla-Padmanabhan), the logarithmic model (G.Efstathiou), and the oscillatory model proposed by Zhang and Ma. 

Here you find the background.c file where the cases of each model were added in order to be called later on through the param file of MontePython. In this file, you can see the changes that were made for the implementation of the models in lines 745 - 894. This file needs to be exchanged with the original background.c found in the source file of CLASS. 

For the oscillatory model, a numerical integral calculator was required for the computation of the Ci and Si integrals. The library complex.c was added to the source folder of CLASS and a file cisi.c was made containing the numerical integral and was also added to the source folder. Since a new file was added to CLASS, a header file in the include folder of CLASS was required cisi.h. 

To compile CLASS with the newly added file, the Makefile was adjusted to contain the new file. The updated Makefile is included in this repository.
