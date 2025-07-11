# Update-of-wCDM-models

In this paper, CLASS and MontePython were used. This repository contains the constant (w0CDM) model, the quadratic model (Jassal-Bagla-Padmanabhan), the logarithmic model (G.Efstathiou), and the oscillatory model proposed by Zhang and Ma. This work was done in association with the paper 

``` LINK TO THE PAPER ```

Here you find the background.c file where the cases of each model were added in order to be called later on through the param file of MontePython. In this file, you can see the changes that were made for the implementation of the models in lines 745 - 894. This file needs to be exchanged with the original background.c found in the source file of CLASS. 

For the oscillatory model, a numerical integral calculator was required for the computation of the Ci and Si integrals. The library complex.c was added to the source folder of CLASS and a file cisi.c was made containing the numerical integral and was also added to the source folder. Since a new file was added to CLASS, a header file in the include folder of CLASS was required cisi.h. 

To compile CLASS with the newly added file, the Makefile was adjusted to contain the new file. The updated Makefile is included in this repository.

-------------------------------------------------------------------------------------------------------------------

# Whisker Plots

The folder 'Whisker plot' in this repository contains the code for the plotting a whisker plot, as shown in this paper. In the folder, you will find two .csv files: the wCDM_Late-time.csv file includes the values of the four wCDM models using late-time data combinations; and the wCDM_Early-time_and_combinations.csv file holds the values of the models using Early-time data and combinations of Early-time with Late-time data. 

The code generates a whisker plot using the data of wCDM_Late-time.csv, and a whisker plot using wCDM_Early-time_and_combinations.csv. The original code was adapted from Luca Visinelli (Link: https://github.com/lucavisinelli/H0TensionRealm.git), associated with the paper ``` https://doi.org/10.48550/arXiv.2103.01183 ```, and modifications were made to generate the figures presented.

In the .csv files, the columns: w0, wa, H0, and Sigma8 show the mean values of each parameter; w0_m, wa_m, H0_m, and Sigma8_m present the negative uncertainty of each parameter; and w0_p, wa_p, H0_p, and Sigma8_p show the positive uncertainty. 

As for the rows, in the case of wCDM_Early-time_and_combinaitons.csv: rows 2 - 6 contain the values of the standard model and the four wCDM models when ```PR3``` only was used; rows 7 - 11 present the values when ```PR4``` was taken; rows 12 - 16 show the values when ```PR3 + CC + SN+SH0ES``` data combination was used; rows 17 - 21 demonstrate the values when ```PR4 + CC + SN+SH0ES``` data combination was taken; rows 22 - 26 show the values of the models when ```PR3 + CC + SN+SH0ES + DESI``` was considered; and rows 27 - 31 present the shows when ```PR4 + CC + SH0ES + DESI``` was used. 

For wCDM_Late-time.csv: rows 2 - 6 show the values of the LCDM model and the tested models when ```CC + SN+SH0ES``` was taken; rows 7- 11 present the values of the models when ```CC + SN+SH0ES + BAO``` was used; and rows 11 - 16 show the values when ```CC + SN+SH0ES + DESI``` was considered. 

---------------------------------------------------------------------------------------------------------------------------------------
# Software Used 

In this research, CLASS (```CLASS II: Approximation schemes <http://arxiv.org/abs/1104.2933>```) was used to handle the computation of the background and perturbation equations. The link to the CLASS Github can be found https://github.com/lesgourg/class_public . 

MontePython software was used for the Monte Carlo Markov Chain (MCMC) code ```Conservative Constraints on Early Cosmology  https://doi.org/10.48550/arXiv.1210.7183 ```, ``` MontePython 3: boosted MCMC sampler and other features https://doi.org/10.48550/arXiv.1804.07261 ```. The link to the MontePython Github can be found https://github.com/brinckmann/montepython_public . 

GetDist software was also used for the plotting of the triangular plots (```GetDist: a Python package for analysing Monte Carlo samples https://doi.org/10.48550/arXiv.1910.13970 ``` ). The link to the GetDist Github page can be found https://github.com/cmbant/getdist?tab=readme-ov-file

----------------------------------------------------------------------------------------------------------------------------------------------------
# Licence

This work is under the GNU LGPL Licence. You are free to use, modify, and share this work, as an additional clause, when using the code in a scientific publication, you are also required to cite the paper: ```ADD LINK TO PAPER ``` Please read the license terms for more information.

---------------------------------------------------------------------------------------------------------------------------------------------------------
