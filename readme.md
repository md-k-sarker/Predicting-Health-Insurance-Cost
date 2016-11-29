##Question: Find risk of accident/death of the people.


###Background: Insurance company especially health insurance company need to analyze how a customer is disease prone. We will try to find the risk based on the customers data.

##Prediction [Will try to predict how a person is prone to disease]


##Feature information: 

<li>
<ul>Id (integer primary key) - Main identifier, used for joining with DeathRecordId in EntityAxisConditions and RecordAxisConditions tables. </ul>
<ul>ResidentStatus (integer) - (e.g. 1 = Residents, 2 = Intrastate resident, etc)</ul>
<ul>Education1989Revision (integer) - Years of education using the 1989 revision format (e.g. 8 = 8 years of elementary education)</ul>
<ul>Education2003Revision (integer) - Years of education using the 2003 revision code (e.g. 8 = Doctorate or professional degree)</ul>
<ul>EducationReportingFlag (integer) - (0 = 1989 revision was used on death certificate, 1 = 2003 revision was used)</ul>
<ul>MonthOfDeath (integer) - Month of death (e.g. 1 = January, 12 = December)</ul>
<ul>Sex (text) - (M = Male, F = Female)</ul>
<ul>AgeType (integer) - Units for the Age column (e.g. 1 = Years, 2 = Months)</ul>
<ul>Age (integer) - Age at death (in AgeType units)</ul>
<ul>AgeSubstitutionFlag (integer) - (1 = Calculated age is substituted for reported age)</ul>
<ul>AgeRecode52 (integer) - Age recoded into 52 bins (e.g. 1 = Under 1 hour)</ul>
<ul>AgeRecode27 (integer) - Age recoded into 27 bins (e.g. 1 = Under 1 month)</ul>
<ul>AgeRecode12 (integer) - Age recoded into 12 bins (e.g. 1 = Under 1 year)</ul>
<ul>InfantAgeRecode22 (integer) - In the event of an infant, Age recoded into 22 bins (e.g. 1 = Under 1 hour)</ul>
<ul>PlaceOfDeathAndDecedentsStatus (integer) - (e.g. 6 = Nursing home/long term care)</ul>
<ul>MaritalStatus (text) - (e.g. M = married, D = divorced, W = widowed)</ul>
<ul>DayOfWeekOfDeath (text) - (e.g. 1 = Sunday, 7 = Saturday)</ul>
<ul>CurrentDataYear (text) - Year on death record. Always 2014 for this dataset.</ul>
<ul>InjuryAtWork (text) - Was the person injured at work? (Y = yes, N = no, U = unknown)</ul>
<ul>MannerOfDeath (integer) - (e.g. 1 = Accident, 2 = Suicides)</ul>
<ul>MethodOfDisposition (text) - (e.g. B = burial, C = crematio)</ul>
</li>