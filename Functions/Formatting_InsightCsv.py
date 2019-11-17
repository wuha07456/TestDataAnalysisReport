import pandas as pd
from Functions import Random_str
def Formatting_InsightCsv(InsightCsv_path):
    """
    处理Insight csv格式与SFTP csv一致
    :param InsightCsv_path:
    :return: InsightData_Path
    """
    usecols=[0,2,4,6,7,8,9]
    usecols=[0,1,2,3,4,5,6,7,8,9]
    column_names = ['Site','SerialNumber','Special Build Description','Station ID','Test Pass/Fail Status','StartTime','EndTime']
    column_names = ['Site', 'Product', 'SerialNumber', 'Special Build Name', 'Special Build Description','Unit Number','Station ID', 'Test Pass/Fail Status', 'StartTime', 'EndTime']
    df=pd.read_csv(InsightCsv_path,usecols=usecols,encoding='gbk',sep=',',names=column_names)
    df.drop(index=[0, 1, 2, 3, 4, 5, 6], inplace=True)
    filename=df['Station ID'].values[0]
    #print(InsightCsv_path)
    #print(len(df))
    #filename = InsightCsv_path.split('\\')[5]
    #filename=Random_str.Random_str()#调用随机函数 生成随机文件名
    InsightData_Path=r"C:\Users\lide\Desktop\TestDataAnalysis\TestDataAnalysis\Data\InsightData\\"+filename+".csv"
    df.to_csv(InsightData_Path, index=None)
    #print(InsightData_Path)
    return InsightData_Path
#Formatting_InsightCsv(r"E:\Insight_VS_SFTP\Data\InsightData\2019-07-05\LOG-COLLECTION\Export-ID-115213002881644-2019-07-05T00_00_00-2019-07-06T00_00_00-ProductCodes-15-LOG-COLLECTION-Versions-5.csv.csv")