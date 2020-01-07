#Alternate_Tests Calculation_No_SES
#Jeanho Rodriguez.
#Date: 12/26/2019.

import pandas as pd
from functools import reduce
import numpy as np

# set display
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

# increase column width
pd.set_option('display.max_colwidth', 1000)

#df = pd.read_csv('All Valid Tests 2019 V1.csv',header=0, low_memory=False, encoding =
                 #'unicode_escape')


df = pd.read_csv('AVT_2019_V3_01062020.csv', header=0, low_memory=False, encoding = 'unicode_escape')

df.rename(columns={'SES_DistName': 'SES_DistrictName'}, inplace=True)

df_TEMBO_DP = pd.read_csv('TEMBO_Datapoints_Schnumb.csv',header=0, low_memory=False, encoding =
                 'unicode_escape')

df_TEMBO_DP['check'] = 'check'


df = df[['STID','LoGrade','HiGrade','SES_SchoolName','SES_DistrictName','Testname','Subtest','level','SES_LocationCode','SES_DistrictCode','InAccty_District','InAccty_School']]

df['SES_SchNumber'] = (df['SES_DistrictCode'] * 1000) + df['SES_LocationCode']

df.loc[df['HiGrade'] != '12', 'level'] = 'es_ms' # 585280
df.loc[df['HiGrade'] == '12', 'level'] = 'hs' # 203068


# All_NMAPA_NUM
df_num_all = df.copy()
df_num_all = df_num_all.loc[(df_num_all['Testname'] == 'NMAPA')] #5578
df_num_all  = df_num_all.sort_values(['STID'], ascending=[True])
df_num_all = df_num_all.groupby(['STID']).last().reset_index() #2405

# All_NMAPA_NUM_MATH
df_num_all_math = df_num_all.copy()
df_num_all_math = df_num_all_math.loc[(df_num_all_math['Subtest'] == 'MATH')] #1048

# All_NMAPA_NUM_SCI
df_num_all_sci = df_num_all.copy()
df_num_all_sci = df_num_all_sci.loc[(df_num_all_sci['Subtest'] == 'SCI')] #400

# All_NMAPA_NUM_READ
df_num_all_read = df_num_all.copy()
df_num_all_read = df_num_all_read.loc[(df_num_all_read['Subtest'] == 'READ')] #957



# All_NMAPA_State_NUM
df_num_all_state = df_num_all.copy()
df_num_all_state['SES_SchNumber'] = 999999
df_num_all_state['SES_SchoolName'] = 'State'
df_num_all_state = (df_num_all_state.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

# MATH_NMAPA_State_NUM
df_num_all_state_math = df_num_all_math.copy()
df_num_all_state_math['SES_SchNumber'] = 999999
df_num_all_state_math['SES_SchoolName'] = 'State'
df_num_all_state_math = (df_num_all_state_math.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

# SCI_NMAPA_State_NUM
df_num_all_state_sci = df_num_all_sci.copy()
df_num_all_state_sci['SES_SchNumber'] = 999999
df_num_all_state_sci['SES_SchoolName'] = 'State'
df_num_all_state_sci = (df_num_all_state_sci.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

# READ_NMAPA_State_NUM
df_num_all_state_read = df_num_all_read.copy()
df_num_all_state_read['SES_SchNumber'] = 999999
df_num_all_state_read['SES_SchoolName'] = 'State'
df_num_all_state_read = (df_num_all_state_read.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

#MATH_SL_NMAPA_State_NUM
df_num_all_state_math_SL = df_num_all_math.copy()
df_num_all_state_math_SL['SES_SchNumber'] = 999999
df_num_all_state_math_SL['SES_SchoolName'] = 'State'
df_num_all_state_math_SL = (df_num_all_state_math_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#SCI_SL_NMAPA_State_NUM
df_num_all_state_science_SL = df_num_all_sci.copy()
df_num_all_state_science_SL['SES_SchNumber'] = 999999
df_num_all_state_science_SL['SES_SchoolName'] = 'State'
df_num_all_state_science_SL = (df_num_all_state_science_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#READ_SL_NMAPA_State_NUM
df_num_all_state_read_SL = df_num_all_read.copy()
df_num_all_state_read_SL['SES_SchNumber'] = 999999
df_num_all_state_read_SL['SES_SchoolName'] = 'State'
df_num_all_state_read_SL = (df_num_all_state_read_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())


#All_NMAPA_District_NUM
df_num_all_district = df_num_all.copy()
df_num_all_district = (df_num_all_district.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())


#MATH_NMAPA_District_NUM
df_num_all_district_math = df_num_all_math.copy()
df_num_all_district_math = (df_num_all_district_math.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())

#SCI_NMAPA_District_NUM
df_num_all_district_sci = df_num_all_sci.copy()
df_num_all_district_sci = (df_num_all_district_sci.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())

#READ_NMAPA_District_NUM
df_num_all_district_read = df_num_all_read.copy()
df_num_all_district_read = (df_num_all_district_read.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())

#MATH_SL_NMAPA_District_NUM
df_num_all_district_math_SL = df_num_all_math.copy()
df_num_all_district_math_SL = (df_num_all_district_math_SL.groupby(['SES_DistrictCode','SES_DistrictName','Subtest','level'])
                      ['STID'].count().reset_index())

#SCI_SL_NMAPA_District_NUM
df_num_all_district_science_SL = df_num_all_sci.copy()
df_num_all_district_science_SL = (df_num_all_district_science_SL.groupby(['SES_DistrictCode','SES_DistrictName','Subtest','level'])
                      ['STID'].count().reset_index())

#READ_SL_NMAPA_District_NUM
df_num_all_district_read_SL = df_num_all_read.copy()
df_num_all_district_read_SL = (df_num_all_district_read_SL.groupby(['SES_DistrictCode','SES_DistrictName','Subtest','level'])
                      ['STID'].count().reset_index())


#All_NMAPA_School_NUM
df_num_all_school = df_num_all.copy()
df_num_all_school = (df_num_all_school.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

#MATH_NMAPA_School_NUM
df_num_all_school_math = df_num_all_math.copy()
df_num_all_school_math = (df_num_all_school_math.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

#SCI_NMAPA_School_NUM
df_num_all_school_sci = df_num_all_sci.copy()
df_num_all_school_sci = (df_num_all_school_sci.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

#READ_NMAPA_School_NUM
df_num_all_school_read = df_num_all_read.copy()
df_num_all_school_read= (df_num_all_school_read.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())


#ALL_SL_NMAPA_School_NUM
df_num_all_school_SL = df_num_all.copy()
df_num_all_school_SL = (df_num_all_school_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#MATH_SL_NMAPA_School_NUM
df_num_all_school_math_SL = df_num_all_math.copy()
df_num_all_school_math_SL = (df_num_all_school_math_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#SCI_SL_NMAPA_School_NUM
df_num_all_school_science_SL = df_num_all_sci.copy()
df_num_all_school_science_SL = (df_num_all_school_science_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#READ_SL_NMAPA_School_NUM
df_num_all_school_read_SL = df_num_all_read.copy()
df_num_all_school_read_SL = (df_num_all_school_read_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

# All_NMAPA_DENOM
df_denom_all = df.copy()
cond1 = df_denom_all['Testname'] != 'ACCESS'
cond2 = df_denom_all['Testname'] != 'Alt ACCESS'
df_denom_all = df_denom_all[cond1 & cond2]
df_denom_all  = df_denom_all.sort_values(['STID'], ascending=[True])
df_denom_all = df_denom_all.groupby(['STID']).last().reset_index() #307005


# All_NMAPA_DENOM_MATH
df_denom_all_math = df_denom_all.copy()
df_denom_all_math = df_denom_all_math.loc[(df_denom_all_math['Subtest'] == 'MATH')] #100046

# All_NMAPA_DENOM_SCI
df_denom_all_sci = df_denom_all.copy()
df_denom_all_sci = df_denom_all_sci.loc[(df_denom_all_sci['Subtest'] == 'SCI')] #32953

# All_NMAPA_DENOM_READ
df_denom_all_read = df_denom_all.copy()
df_denom_all_read = df_denom_all_read.loc[(df_denom_all_read['Subtest'] == 'READ')] #174006




# All_NMAPA_State_DENOM
df_denom_all_state = df_denom_all.copy()
df_denom_all_state['SES_SchNumber'] = 999999
df_denom_all_state['SES_SchoolName'] = 'State'
df_denom_all_state = (df_denom_all_state.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

# MATH_NMAPA_State_DENOM
df_denom_all_state_math = df_denom_all_math.copy()
df_denom_all_state_math['SES_SchNumber'] = 999999
df_denom_all_state_math['SES_SchoolName'] = 'State'
df_denom_all_state_math = (df_denom_all_state_math.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

# SCI_NMAPA_State_DENOM
df_denom_all_state_sci = df_denom_all_sci.copy()
df_denom_all_state_sci['SES_SchNumber'] = 999999
df_denom_all_state_sci['SES_SchoolName'] = 'State'
df_denom_all_state_sci = (df_denom_all_state_sci.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

# READ_NMAPA_State_DENOM
df_denom_all_state_read = df_denom_all_read.copy()
df_denom_all_state_read['SES_SchNumber'] = 999999
df_denom_all_state_read['SES_SchoolName'] = 'State'
df_denom_all_state_read = (df_denom_all_state_read.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

#MATH_SL_NMAPA_State_DENOM
df_denom_all_state_math_SL = df_denom_all_math.copy()
df_denom_all_state_math_SL['SES_SchNumber'] = 999999
df_denom_all_state_math_SL['SES_SchoolName'] = 'State'
df_denom_all_state_math_SL = (df_denom_all_state_math_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#SCI_SL_NMAPA_State_DENOM
df_denom_all_state_science_SL = df_denom_all_sci.copy()
df_denom_all_state_science_SL['SES_SchNumber'] = 999999
df_denom_all_state_science_SL['SES_SchoolName'] = 'State'
df_denom_all_state_science_SL = (df_denom_all_state_science_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#READ_SL_NMAPA_State_DENOM
df_denom_all_state_read_SL = df_denom_all_read.copy()
df_denom_all_state_read_SL['SES_SchNumber'] = 999999
df_denom_all_state_read_SL['SES_SchoolName'] = 'State'
df_denom_all_state_read_SL = (df_denom_all_state_read_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#All_NMAPA_District_DENOM
df_denom_all_district = df_denom_all.copy()

df_denom_all_district = (df_denom_all_district.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())


#MATH_NMAPA_District_DENOM
df_denom_all_district_math = df_denom_all_math.copy()
df_denom_all_district_math = (df_denom_all_district_math.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())

#SCI_NMAPA_District_DENOM
df_denom_all_district_sci = df_denom_all_sci.copy()
df_denom_all_district_sci = (df_denom_all_district_sci.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())

#READ_NMAPA_District_DENOM
df_denom_all_district_read = df_denom_all_read.copy()
df_denom_all_district_read = (df_denom_all_district_read.groupby(['SES_DistrictCode','SES_DistrictName'])
                      ['STID'].count().reset_index())


#MATH_SL_NMAPA_District_DENOM
df_denom_all_district_math_SL = df_denom_all_math.copy()
df_denom_all_district_math_SL = (df_denom_all_district_math_SL.groupby(['SES_DistrictCode','SES_DistrictName','Subtest','level'])
                      ['STID'].count().reset_index())

#SCI_SL_NMAPA_District_DENOM
df_denom_all_district_science_SL = df_denom_all_sci.copy()
df_denom_all_district_science_SL = (df_denom_all_district_science_SL.groupby(['SES_DistrictCode','SES_DistrictName','Subtest','level'])
                      ['STID'].count().reset_index())

#READ_SL_NMAPA_District_DENOM
df_denom_all_district_read_SL = df_denom_all_read.copy()
df_denom_all_district_read_SL = (df_denom_all_district_read_SL.groupby(['SES_DistrictCode','SES_DistrictName','Subtest','level'])
                      ['STID'].count().reset_index())


#All_NMAPA_School_DENOM
df_denom_all_school = df_denom_all.copy()

df_denom_all_school = (df_denom_all_school.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

df_denom_all_school_math = df_denom_all_math.copy()

df_denom_all_school_math = (df_denom_all_school_math.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

df_denom_all_school_sci = df_denom_all_sci.copy()

df_denom_all_school_sci = (df_denom_all_school_sci.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

df_denom_all_school_read = df_denom_all_read.copy()

df_denom_all_school_read = (df_denom_all_school_read.groupby(['SES_SchNumber','SES_SchoolName'])
                      ['STID'].count().reset_index())

#ALL_SL_NMAPA_School_DENOM
df_denom_all_school_SL = df_denom_all.copy()

df_denom_all_school_SL = (df_denom_all_school_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

#ALL_SL_NMAPA_School_DENOM
df_denom_all_school_SL = df_denom_all.copy()

df_denom_all_school_SL = (df_denom_all_school_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

df_denom_all_school_math_SL = df_denom_all_math.copy()

df_denom_all_school_math_SL = (df_denom_all_school_math_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

df_denom_all_school_sci_SL = df_denom_all_sci.copy()

df_denom_all_school_sci_SL = (df_denom_all_school_sci_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())

df_denom_all_school_read_SL = df_denom_all_read.copy()

df_denom_all_school_read_SL = (df_denom_all_school_read_SL.groupby(['SES_SchNumber','SES_SchoolName','Subtest','level'])
                      ['STID'].count().reset_index())


# Change df_num_all_district name and number to concatenate to school level and state level
df_num_all_district.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_num_all_district.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_denom_all_district.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_denom_all_district.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_num_all_district_math.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_num_all_district_math.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_denom_all_district_math.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_denom_all_district_math.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_num_all_district_sci.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_num_all_district_sci.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_denom_all_district_sci.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_denom_all_district_sci.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_num_all_district_read.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_num_all_district_read.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_denom_all_district_read.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_denom_all_district_read.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_num_all_district_math_SL.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_num_all_district_math_SL.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_denom_all_district_math_SL.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_denom_all_district_math_SL.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_num_all_district_science_SL.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_num_all_district_science_SL.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_denom_all_district_science_SL.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_denom_all_district_science_SL.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_num_all_district_read_SL.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_num_all_district_read_SL.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)
df_denom_all_district_read_SL.rename(columns={'SES_DistrictName': 'SES_SchoolName'}, inplace=True)
df_denom_all_district_read_SL.rename(columns={'SES_DistrictCode': 'SES_SchNumber'}, inplace=True)



# concatenate and rename
Stack_All_Num = pd.concat([df_num_all_state,df_num_all_district,df_num_all_school])
Stack_All_Num.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Num.rename(columns={'STID': 'STID_ALL_NUM'}, inplace=True)

Stack_All_Denom = pd.concat([df_denom_all_state,df_denom_all_district,df_denom_all_school])
Stack_All_Denom.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Denom.rename(columns={'STID': 'STID_ALL_DENOM'}, inplace=True)

# concatenate math
Stack_All_Num_Math = pd.concat([df_num_all_state_math,df_num_all_district_math,df_num_all_school_math])
Stack_All_Num_Math.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Num_Math.rename(columns={'STID': 'STID_ALL_NUM'}, inplace=True)

Stack_All_Denom_Math = pd.concat([df_denom_all_state_math,df_denom_all_district_math,df_denom_all_school_math])
Stack_All_Denom_Math.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Denom_Math.rename(columns={'STID': 'STID_ALL_DENOM'}, inplace=True)

# concatenate sci
Stack_All_Num_Sci = pd.concat([df_num_all_state_sci,df_num_all_district_sci,df_num_all_school_sci])
Stack_All_Num_Sci.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Num_Sci.rename(columns={'STID': 'STID_ALL_NUM'}, inplace=True)

Stack_All_Denom_Sci = pd.concat([df_denom_all_state_sci,df_denom_all_district_sci,df_denom_all_school_sci])
Stack_All_Denom_Sci.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Denom_Sci.rename(columns={'STID': 'STID_ALL_DENOM'}, inplace=True)

# concatenate read
Stack_All_Num_Read = pd.concat([df_num_all_state_read,df_num_all_district_read,df_num_all_school_read])
Stack_All_Num_Read.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Num_Read.rename(columns={'STID': 'STID_ALL_NUM'}, inplace=True)

Stack_All_Denom_Read = pd.concat([df_denom_all_state_read,df_denom_all_district_read,df_denom_all_school_read])
Stack_All_Denom_Read.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Denom_Read.rename(columns={'STID': 'STID_ALL_DENOM'}, inplace=True)

# concatenate math SL
Stack_All_Num_Math_SL = pd.concat([df_num_all_state_math_SL,df_num_all_district_math_SL,df_num_all_school_math_SL])
Stack_All_Num_Math_SL.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Num_Math_SL.rename(columns={'STID': 'STID_ALL_NUM'}, inplace=True)

Stack_All_Denom_Math_SL = pd.concat([df_denom_all_state_math_SL,df_denom_all_district_math_SL,df_denom_all_school_math_SL])
Stack_All_Denom_Math_SL.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Denom_Math_SL.rename(columns={'STID': 'STID_ALL_DENOM'}, inplace=True)

# concatenate sci SL
Stack_All_Num_Sci_SL = pd.concat([df_num_all_state_science_SL,df_num_all_district_science_SL,df_num_all_school_science_SL])
Stack_All_Num_Sci_SL.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Num_Sci_SL.rename(columns={'STID': 'STID_ALL_NUM'}, inplace=True)

Stack_All_Denom_Sci_SL = pd.concat([df_denom_all_state_science_SL,df_denom_all_district_science_SL,df_denom_all_school_sci_SL])
Stack_All_Denom_Sci_SL.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Denom_Sci_SL.rename(columns={'STID': 'STID_ALL_DENOM'}, inplace=True)

# concatenate read SL
Stack_All_Num_Read_SL = pd.concat([df_num_all_state_read_SL,df_num_all_district_read_SL,df_num_all_school_read_SL])
Stack_All_Num_Read_SL.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Num_Read_SL.rename(columns={'STID': 'STID_ALL_NUM'}, inplace=True)

Stack_All_Denom_Read_SL = pd.concat([df_denom_all_state_read_SL,df_denom_all_district_read_SL,df_denom_all_school_read_SL])
Stack_All_Denom_Read_SL.rename(columns={'SES_SchNumber': 'schnumb'}, inplace=True)
Stack_All_Denom_Read_SL.rename(columns={'STID': 'STID_ALL_DENOM'}, inplace=True)

# Join All
df_All = [Stack_All_Num, Stack_All_Denom] # Join Numerator and Denominator ALL
df_All_Merge = reduce(lambda left,right: pd.merge(left,right,on=['schnumb','SES_SchoolName'], how='outer'), df_All)
df_All_TEMBO = [df_TEMBO_DP,df_All_Merge]
df_All_Merge_TEMBO = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_All_TEMBO)
df_All_Merge_TEMBO = df_All_Merge_TEMBO.dropna(subset=['check'])

# Join Math
df_All_Math = [Stack_All_Num_Math, Stack_All_Denom_Math] # Join Numerator and Denominator ALL
df_All_Merge_Math = reduce(lambda left,right: pd.merge(left,right,on=['schnumb','SES_SchoolName'], how='outer'), df_All_Math)
df_All_TEMBO_Math = [df_TEMBO_DP,df_All_Merge_Math]
df_All_Merge_TEMBO_Math = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_All_TEMBO_Math)
df_All_Merge_TEMBO_Math = df_All_Merge_TEMBO_Math.dropna(subset=['check'])

# Join Sci
df_All_Sci = [Stack_All_Num_Sci, Stack_All_Denom_Sci] # Join Numerator and Denominator ALL
df_All_Merge_Sci = reduce(lambda left,right: pd.merge(left,right,on=['schnumb','SES_SchoolName'], how='outer'), df_All_Sci)
df_All_TEMBO_Sci = [df_TEMBO_DP,df_All_Merge_Sci]
df_All_Merge_TEMBO_Sci = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_All_TEMBO_Sci)
df_All_Merge_TEMBO_Sci = df_All_Merge_TEMBO_Sci.dropna(subset=['check'])

# Join Read
df_All_Read = [Stack_All_Num_Read, Stack_All_Denom_Read] # Join Numerator and Denominator ALL
df_All_Merge_Read = reduce(lambda left,right: pd.merge(left,right,on=['schnumb','SES_SchoolName'], how='outer'), df_All_Read)
df_All_TEMBO_Read = [df_TEMBO_DP,df_All_Merge_Read]
df_All_Merge_TEMBO_Read = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_All_TEMBO_Read)
df_All_Merge_TEMBO_Read = df_All_Merge_TEMBO_Read.dropna(subset=['check'])


# Join Math SL
df_All_Math_SL = [Stack_All_Num_Math_SL, Stack_All_Denom_Math_SL] # Join Numerator and Denominator ALL
df_All_Merge_Math_SL = reduce(lambda left,right: pd.merge(left,right,on=['schnumb','SES_SchoolName','Subtest','level'], how='outer'), df_All_Math_SL)
df_All_TEMBO_Math_SL = [df_TEMBO_DP,df_All_Merge_Math_SL]
df_All_Merge_TEMBO_Math_SL = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_All_TEMBO_Math_SL)
df_All_Merge_TEMBO_Math_SL = df_All_Merge_TEMBO_Math_SL.dropna(subset=['check'])

# Join Sci SL
df_All_Sci_SL = [Stack_All_Num_Sci_SL, Stack_All_Denom_Sci_SL] # Join Numerator and Denominator ALL
df_All_Merge_Sci_SL = reduce(lambda left,right: pd.merge(left,right,on=['schnumb','SES_SchoolName','Subtest','level'], how='outer'), df_All_Sci_SL)
df_All_TEMBO_Sci_SL = [df_TEMBO_DP,df_All_Merge_Sci_SL]
df_All_Merge_TEMBO_Sci_SL = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_All_TEMBO_Sci_SL)
df_All_Merge_TEMBO_Sci_SL = df_All_Merge_TEMBO_Sci_SL.dropna(subset=['check'])

# Join Read SL
df_All_Read_SL = [Stack_All_Num_Read_SL, Stack_All_Denom_Read_SL] # Join Numerator and Denominator ALL
df_All_Merge_Read_SL = reduce(lambda left,right: pd.merge(left,right,on=['schnumb','SES_SchoolName','Subtest','level'], how='outer'), df_All_Read_SL)
df_All_TEMBO_Read_SL = [df_TEMBO_DP,df_All_Merge_Read_SL]
df_All_Merge_TEMBO_Read_SL = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_All_TEMBO_Read_SL)
df_All_Merge_TEMBO_Read_SL = df_All_Merge_TEMBO_Read_SL.dropna(subset=['check'])

# Rates
df_All_Merge_TEMBO['All_Rate'] = (df_All_Merge_TEMBO['STID_ALL_NUM']/df_All_Merge_TEMBO['STID_ALL_DENOM']) * 100

df_All_Merge_TEMBO_Math['Math_Rate'] = (df_All_Merge_TEMBO_Math['STID_ALL_NUM']/df_All_Merge_TEMBO_Math['STID_ALL_DENOM']) * 100
df_All_Merge_TEMBO_Sci['Sci_Rate'] = (df_All_Merge_TEMBO_Sci['STID_ALL_NUM']/df_All_Merge_TEMBO_Sci['STID_ALL_DENOM']) * 100
df_All_Merge_TEMBO_Read['Read_Rate'] = (df_All_Merge_TEMBO_Read['STID_ALL_NUM']/df_All_Merge_TEMBO_Read['STID_ALL_DENOM']) * 100

df_All_Merge_TEMBO_Math_SL['Math_SL_Rate'] = (df_All_Merge_TEMBO_Math_SL['STID_ALL_NUM']/df_All_Merge_TEMBO_Math_SL['STID_ALL_DENOM']) * 100
df_All_Merge_TEMBO_Sci_SL['Sci_SL_Rate'] = (df_All_Merge_TEMBO_Sci_SL['STID_ALL_NUM']/df_All_Merge_TEMBO_Sci_SL['STID_ALL_DENOM']) * 100
df_All_Merge_TEMBO_Read_SL['Read_SL_Rate'] = (df_All_Merge_TEMBO_Read_SL['STID_ALL_NUM']/df_All_Merge_TEMBO_Read_SL['STID_ALL_DENOM']) * 100

# data transform
df_TEMBO_Math_SL = pd.pivot_table(df_All_Merge_TEMBO_Math_SL,values='Math_SL_Rate',index='schnumb',columns='level').reset_index()
df_TEMBO_Sci_SL = pd.pivot_table(df_All_Merge_TEMBO_Sci_SL,values='Sci_SL_Rate',index='schnumb',columns='level').reset_index()
df_TEMBO_Read_SL = pd.pivot_table(df_All_Merge_TEMBO_Read_SL,values='Read_SL_Rate',index='schnumb',columns='level').reset_index()

df_TEMBO_Math_SL.rename(columns={'es_ms': 'math_es_ms'}, inplace=True)
df_TEMBO_Math_SL.rename(columns={'hs': 'math_hs'}, inplace=True)
df_TEMBO_Sci_SL.rename(columns={'es_ms': 'sci_es_ms'}, inplace=True)
df_TEMBO_Sci_SL.rename(columns={'hs': 'sci_hs'}, inplace=True)
df_TEMBO_Read_SL.rename(columns={'es_ms': 'read_es_ms'}, inplace=True)
df_TEMBO_Read_SL.rename(columns={'hs': 'read_hs'}, inplace=True)

# Prep Files for Merge
df_All_Merge_TEMBO = df_All_Merge_TEMBO[['schnumb','All_Rate']]
df_All_Merge_TEMBO_Math = df_All_Merge_TEMBO_Math[['schnumb','Math_Rate']]
df_All_Merge_TEMBO_Sci = df_All_Merge_TEMBO_Sci[['schnumb','Sci_Rate']]
df_All_Merge_TEMBO_Read = df_All_Merge_TEMBO_Read[['schnumb','Read_Rate']]

# Merge the school level and domains
df_SL_All = [df_TEMBO_DP,df_All_Merge_TEMBO,df_All_Merge_TEMBO_Math,df_All_Merge_TEMBO_Sci,df_All_Merge_TEMBO_Read,
             df_TEMBO_Math_SL, df_TEMBO_Sci_SL, df_TEMBO_Read_SL] # SL

df_SL_All_Merge = reduce(lambda left,right: pd.merge(left,right,on=['schnumb'], how='outer'), df_SL_All)

# Round to two places
df_SL_All_Merge = df_SL_All_Merge.round(2)

# convert NaN to 'not applicable'
df_SL_All_Merge.fillna('not applicable', inplace=True)

df_SL_All_Merge.to_csv("df_ALT_All_Merge01062020.csv", sep=',', encoding='utf-8', index = False)














