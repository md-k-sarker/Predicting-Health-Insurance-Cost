Question: Find risk of accident/death of the people.


Background: Insurance company especially car insurance company need to analyze how a customer is accident prone. We will try to find the risk based on the customers data.

Input information: 

DeathRecords

Primary table containing a single row per death record with these columns:

Id (integer primary key) - Main identifier, used for joining with DeathRecordId in EntityAxisConditions and RecordAxisConditions tables.
ResidentStatus (integer) - (e.g. 1 = Residents, 2 = Intrastate resident, etc)
Education1989Revision (integer) - Years of education using the 1989 revision format (e.g. 8 = 8 years of elementary education)
Education2003Revision (integer) - Years of education using the 2003 revision code (e.g. 8 = Doctorate or professional degree)
EducationReportingFlag (integer) - (0 = 1989 revision was used on death certificate, 1 = 2003 revision was used)
MonthOfDeath (integer) - Month of death (e.g. 1 = January, 12 = December)
Sex (text) - (M = Male, F = Female)
AgeType (integer) - Units for the Age column (e.g. 1 = Years, 2 = Months)
Age (integer) - Age at death (in AgeType units)
AgeSubstitutionFlag (integer) - (1 = Calculated age is substituted for reported age)
AgeRecode52 (integer) - Age recoded into 52 bins (e.g. 1 = Under 1 hour)
AgeRecode27 (integer) - Age recoded into 27 bins (e.g. 1 = Under 1 month)
AgeRecode12 (integer) - Age recoded into 12 bins (e.g. 1 = Under 1 year)
InfantAgeRecode22 (integer) - In the event of an infant, Age recoded into 22 bins (e.g. 1 = Under 1 hour)
PlaceOfDeathAndDecedentsStatus (integer) - (e.g. 6 = Nursing home/long term care)
MaritalStatus (text) - (e.g. M = married, D = divorced, W = widowed)
DayOfWeekOfDeath (text) - (e.g. 1 = Sunday, 7 = Saturday)
CurrentDataYear (text) - Year on death record. Always 2014 for this dataset.
InjuryAtWork (text) - Was the person injured at work? (Y = yes, N = no, U = unknown)
MannerOfDeath (integer) - (e.g. 1 = Accident, 2 = Suicides)
MethodOfDisposition (text) - (e.g. B = burial, C = crematio