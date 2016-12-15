##Question: Find risk of accident/death of the people.


###Background: Insurance company especially health insurance company need to analyze how a customer is disease prone. We will try to find the risk based on the customers data.

##Prediction [Will try to predict how a person is prone to disease]

##Class Imbalance
Has high class imbalance <img src="https://raw.githubusercontent.com/md-k-sarker/ML-Analyze-Morality/master/results/classImbalance_scaled.png"></img>


##Feature information: 

###Median and Quartile of each features

<img src="https://raw.githubusercontent.com/md-k-sarker/ML-Analyze-Morality/master/results/featureStatsWithoutFeature17.png"></img>

<ul>
<li>Id (integer primary key) - Main identifier, used for joining with DeathRecordId in EntityAxisConditions and RecordAxisConditions tables. </li>
<li>ResidentStatus (integer) - (e.g. 1 = Residents, 2 = Intrastate resident, etc)</li>
<li>Education1989Revision (integer) - Years of education using the 1989 revision format (e.g. 8 = 8 years of elementary education)</li>
<li>Education2003Revision (integer) - Years of education using the 2003 revision code (e.g. 8 = Doctorate or professional degree)</li>
<li>EducationReportingFlag (integer) - (0 = 1989 revision was used on death certificate, 1 = 2003 revision was used)</li>
<li>MonthOfDeath (integer) - Month of death (e.g. 1 = January, 12 = December)</li>
<li>Sex (text) - (M = Male, F = Female)</li>
<li>AgeType (integer) - Units for the Age column (e.g. 1 = Years, 2 = Months)</li>
<li>Age (integer) - Age at death (in AgeType units)</li>
<li>AgeSubstitutionFlag (integer) - (1 = Calculated age is substituted for reported age)</li>
<li>AgeRecode52 (integer) - Age recoded into 52 bins (e.g. 1 = Under 1 hour)</li>
<li>AgeRecode27 (integer) - Age recoded into 27 bins (e.g. 1 = Under 1 month)</li>
<li>AgeRecode12 (integer) - Age recoded into 12 bins (e.g. 1 = Under 1 year)</li>
<li>InfantAgeRecode22 (integer) - In the event of an infant, Age recoded into 22 bins (e.g. 1 = Under 1 hour)</li>
<li>PlaceOfDeathAndDecedentsStatus (integer) - (e.g. 6 = Nursing home/long term care)</li>
<li>MaritalStatus (text) - (e.g. M = married, D = divorced, W = widowed)</li>
<li>DayOfWeekOfDeath (text) - (e.g. 1 = Sunday, 7 = Saturday)</li>
<li>CurrentDataYear (text) - Year on death record. Always 2014 for this dataset.</li>
<li>InjuryAtWork (text) - Was the person injured at work? (Y = yes, N = no, U = unknown)</li>
<li>MannerOfDeath (integer) - (e.g. 1 = Accident, 2 = Suicides)</li>
<li>MethodOfDisposition (text) - (e.g. B = burial, C = crematio)</li>
</ul>