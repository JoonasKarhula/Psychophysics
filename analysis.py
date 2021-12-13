import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
from os import listdir
from statsmodels.stats.anova import AnovaRM
from scipy.stats import norm, ttest_ind, zscore
import numpy as np

#defining functions that return dPrime and criterion values for later sensitivity analysis
def dPrime(hitRate, FArate):
    return norm.ppf(hitRate) - norm.ppf(FArate)
def criterion(hitRate, FArate):
    return -.5*(norm.ppf(hitRate) + norm.ppf(FArate))

#dPrimevariance calculation based on Macmillan & Creelman, Detection Theory: a user's guide (2005)
#table_values are normal density function values with hit and FA rates (Manually from Detection theory Appendix Table 5.1)
def dPrimevariance(hitRate, FARate, table_value, table_value2):
    return ((hitRate*(1-hitRate))/20*(table_value)**2)+((FARate*(1-FARate))/20*(table_value2)**2)

dataPath = 'data/'
fileList = listdir(dataPath)

#Creating a dataframe for all the information that needs to be gathered from participant results
hits_FAs = pd.DataFrame({'Participant' : [], 'Condition' : [], 'Hits' : [], 'FAs' : [], 'Misses' : [], 'CRs' : [], 'Mean RT' : [], "d'" : [], 'Criterion' : []})
counter = 0

#Iterating the data files
for dataFile in fileList:
    #Making a dataframe for accuracy in the experiment
    accuracy = pd.DataFrame({'Participant': ['', ''], 'Condition': ['Unprimed', 'Primed'], 'hits': [0, 0], 'Misses': [0, 0], 'CRs': [0, 0],'FAs': [0, 0]})
    #Counting participant number, and reading the data file, and changing some column names for more convenient ones
    counter += 1
    pNum = 'P' + str(counter)
    rawData = pd.read_csv(dataPath + dataFile)
    expData = pd.DataFrame(rawData, columns = ['correc', 'primcond', 'onstcond', 'Response.corr', 'Response.rt'])
    expData = expData.rename(columns = {'Response.rt' : 'RT', 'Response.corr' : 'Respcorr'})

    #Iterating hits, false alarms, correct rejections and misses
    #Results are split by the to conditions of the experiment
    for index,row in expData.iterrows():
        if row['primcond'] == 'None':
            rowInd = 0
            if row['correc'] != 'None' and row['Respcorr'] == 1:
                accuracy.loc[rowInd, 'hits'] += 1
            elif row['correc'] == 'None' and row['Respcorr'] == 0:
                accuracy.loc[rowInd, 'FAs'] += 1
            elif row['correc'] != 'None' and row['Respcorr'] == 0:
                accuracy.loc[rowInd, 'Misses'] += 1
            elif row['correc'] == 'None' and row['Respcorr'] == 1:
                accuracy.loc[rowInd, 'CRs'] += 1
        if row['primcond'] == 'Oppcol':
            rowInd = 1
            if row['correc'] != 'None' and row['Respcorr'] == 1:
                accuracy.loc[rowInd, 'hits'] += 1
            elif row['correc'] == 'None' and row['Respcorr'] == 0:
                accuracy.loc[rowInd, 'FAs'] += 1
            elif row['correc'] != 'None' and row['Respcorr'] == 0:
                accuracy.loc[rowInd, 'Misses'] += 1
            elif row['correc'] == 'None' and row['Respcorr'] == 1:
                accuracy.loc[rowInd, 'CRs'] += 1
    #Adding participant number to accuracy dataframe
    accuracy.loc[0, 'Participant'] = pNum
    accuracy.loc[1, 'Participant'] = pNum
    #Calculating hitrates and FArates based on the trialnumbers (20).
    hitRateunprimed = accuracy.loc[0, 'hits'] / 20
    FArateunprimed = accuracy.loc[0, 'FAs'] / 20
    hitRateprimed = accuracy.loc[1, 'hits'] / 20
    FArateprimed = accuracy.loc[1, 'FAs'] / 20
    dprimeunprimed = dPrime(hitRateunprimed, FArateunprimed)
    dprimeprimed = dPrime(hitRateprimed, FArateprimed)
    criterionunprimed = criterion(hitRateunprimed, FArateunprimed)
    criterionprimed = criterion(hitRateprimed, FArateprimed)

    #This was used to gather the hitrates and FArates for the d' variance analysis
    print(pNum, 'hitRateunprimed:', hitRateunprimed, 'FArateunprimed:', FArateunprimed, 'hitRateprimed:', hitRateprimed, 'FArateprimed:', FArateprimed)

    #Taking RT values that are not empty, and RT values that are from correct responses
    expData = expData[expData.RT.notnull()]
    rtData = expData[(expData.Respcorr == 1)]
    unprimedRTs = []
    primedRTs = []
    #Iterating through rtData, and removing values under 200msec
    for index, row in rtData.iterrows():
        if row['primcond'] == 'None' and row['RT'] > 0.2:
            unprimedRTs.append(row['RT'])
        elif row['primcond'] == 'Oppcol' and row['RT'] > 0.2:
            primedRTs.append(row['RT'])

    #Using histogram to check the skewness of the distribution
    plt.hist(unprimedRTs, bins=15)
    plt.ylabel('Frequency')
    plt.xlabel('RT (s)')
    plt.title(f'{pNum} Unprimed RTs')
    plt.show()
    plt.hist(primedRTs, bins=15)
    plt.ylabel('Frequency')
    plt.xlabel('RT (s)')
    plt.title(f'{pNum} Primed RTs')
    plt.show()

    #Creating new RT dataframes and removing values more than 3 standard deviations from the mean of the reaction times.
    RT_df_unprimed = pd.DataFrame({'RT unprimed': unprimedRTs})
    RT_df_primed = pd.DataFrame({'RT primed': primedRTs})
    z_scoresunprimed = zscore(RT_df_unprimed)
    z_scoresprimed = zscore(RT_df_primed)
    abs_z_scores_unprimed = np.abs(z_scoresunprimed)
    abs_z_scores_primed = np.abs(z_scoresprimed)
    filtered_entries_unprimed = (abs_z_scores_unprimed < 3).all(axis=1)
    filtered_entries_primed = (abs_z_scores_primed < 3).all(axis=1)
    RT_df_new_unprimed = RT_df_unprimed[filtered_entries_unprimed]
    RT_df_new_primed = RT_df_primed[filtered_entries_primed]

    #Making new RT lists and iterating RT_df_new dataframes for RT values of both conditions without outliers
    filunprimed= []
    filprimed = []
    for index,row in RT_df_new_unprimed.iterrows():
        filunprimed.append(row['RT unprimed'])
    for index,row in RT_df_new_primed.iterrows():
        filprimed.append(row['RT primed'])
    #Printing the number of outliers removed
    print(f'{pNum}: Removed {len(unprimedRTs)-len(filunprimed)} outliers from unprimed RTs and {len(primedRTs)-len(filprimed)} outliers from primed RTs')
    #No outliers found 3 SDs away from mean in any participants data!

    #Scatter plot to see the independent RT values to check outliers
    plt.scatter(range(1, len(filunprimed)+len(filprimed)+1), filunprimed+filprimed)
    plt.ylabel('RT (s)')
    plt.title(f'{pNum} RTs from both conditions')
    plt.show()
    #Box plot to double check outliers
    fig, ax = plt.subplots()
    box = ax.boxplot([filunprimed, filprimed])
    ax.set_ylabel('RT (s)')
    ax.set_title(f'{pNum} reaction times within conditions')
    ax.set_xticklabels(['Unprimed', 'Primed'])
    plt.show()
    print(f'{pNum} RTs t-test results:{ttest_ind(mean(filunprimed), mean(filprimed))} \n')
    #Boxplot shows outliers even though everything outside 3 SD is removed.

    #Calculating means from the conditions, and filling all infromation collected in the for loop to the dataframe created before the loop
    meanRTsList = [mean(filunprimed), mean(filprimed)]
    newLines_unprimed = pd.DataFrame({'Participant': [pNum], 'Condition': ['Unprimed'], 'Hits': [accuracy.loc[0, 'hits']], 'FAs': [accuracy.loc[0, 'FAs']], 'Misses' : [accuracy.loc[0, 'Misses']], 'CRs' : [accuracy.loc[0, 'CRs']], 'Mean RT': [meanRTsList[0]], "d'": [dprimeunprimed], 'Criterion': [criterionunprimed]})
    newLines_primed = pd.DataFrame({'Participant': [pNum], 'Condition': ['Primed'], 'Hits': [accuracy.loc[1, 'hits']], 'FAs': [accuracy.loc[1, 'FAs']], 'Misses' : [accuracy.loc[1, 'Misses']], 'CRs' : [accuracy.loc[1, 'CRs']], 'Mean RT': [meanRTsList[1]], "d'": [dprimeprimed], 'Criterion': [criterionprimed]})
    hits_FAs = hits_FAs.append(newLines_unprimed, ignore_index=True)
    hits_FAs = hits_FAs.append(newLines_primed, ignore_index=True)

#Group analysis of the reaction times
unprimedMeanRTs = hits_FAs[(hits_FAs.Condition) == 'Unprimed']['Mean RT']
primedMeanRTs = hits_FAs[(hits_FAs.Condition) == 'Primed']['Mean RT']
print(f'Experiment-level mean RT for unprimed condition: {mean(unprimedMeanRTs)}')
print(f'Experiment-level mean RT for primed condition: {mean(primedMeanRTs)}')

#Repeated-measures ANOVA to check for statistically significant difference between conditions at group level
model = AnovaRM(data=hits_FAs, depvar='Mean RT', subject='Participant', within=['Condition']).fit()
print(model)

#Plotting the mean RTs of participants as a boxplot
fig, ax = plt.subplots()
box = ax.boxplot([unprimedMeanRTs, primedMeanRTs])
ax.set_ylabel('RT (s)')
ax.set_xticklabels(['Unprimed', 'Primed'])
plt.show()

#Exporting the result table as a csv file and printing it to check it
print(hits_FAs)
hits_FAs.to_csv(r'E:\Yliopisto\MDP in Human Neuroscience\Psychophysics\Allresults.csv', index=False, header=True)

#Comparison of d' of different conditions following Macmillan & Creelman, Detection Theory: a user's guide (2005).
#Done manually, but could have actually added these calculations to the loop!
#Only for the participants who had above zero d prime

dvarunprimed2 = dPrimevariance(0.2, 0.15, 0.2800, 0.2332)
dvarprimed2 = dPrimevariance(0.45, 0.3, 0.3958, 0.3477)
print(f'95% CI of dprime difference between experiment conditions for P2: {(0.3987-0.1948)} +/- {1.96*(dvarunprimed2+dvarprimed2)**0.5}')

dvarunprimed4 = dPrimevariance(0.7, 0.05, 0.3477, 0.1031)
dvarprimed4 = dPrimevariance(0.7, 0.3, 0.3477, 0.3477)
print(f'95% CI of dprime difference between experiment conditions for P4: {(2.1693-1.0488)} +/- {1.96*(dvarunprimed4+dvarprimed4)**0.5}')

dvarunprimed5 = dPrimevariance(0.75, 0.45, 0.3178, 0.3958)
dvarprimed5 = dPrimevariance(0.55, 0.6, 0.3958, 0.3863)
print(f'95% CI of dprime difference between experiment conditions for P5: {(0.8002+0.1277)} +/- {1.96*(dvarunprimed5+dvarprimed5)**0.5}')
