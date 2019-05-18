#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'generate_data'))
	print(os.getcwd())
except:
	pass
#%%[markdown]
# From this Website: http://dataservices.mof.go.th/Dataservices/GovernmentExpenditureEconomyMinistry
#%%
import xmltodict

with open('จำแนกตามลักษณะเศรษฐกิจและกระทรวง.xml','r', encoding="utf-8") as fd:
    doc = xmltodict.parse(fd.read())
with open('data.csv','a') as fd:
    print('',end='\n',file=fd)
    for i in range(0,100):
        try:
            if doc['TransGovernment']['MinistryGroup'][11]['MinistryGroupDetail'][i]['MinistryDetail']['DataDate'][-1] == 'y':
                continue
            if doc['TransGovernment']['MinistryGroup'][11]['MinistryGroupDetail'][i]['MinistryDetail']['DataDate'][-1] == 't':
                continue
            print(str(int(doc['TransGovernment']['MinistryGroup'][11]['MinistryGroupDetail'][i]['MinistryDetail']['DataDate'][:4])-543) + "-" + doc['TransGovernment']['MinistryGroup'][11]['MinistryGroupDetail'][i]['MinistryDetail']['DataDate'][-2:],end=',',file=fd)
            # print(doc['TransGovernment']['MinistryGroup'][11]['MinistryGroupDetail'][i]['MinistryDetail']['DataDate'],end=',')
            print(str(doc['TransGovernment']['MinistryGroup'][11]['MinistryGroupDetail'][i]['MinistryDetail']['Value']).replace(',',''),file=fd)
            # print()
        except:
            break