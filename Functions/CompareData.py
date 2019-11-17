from Functions import CombineData,Formatting_InsightCsv
import pandas as pd
import numpy as np
import xlrd,xlwt
def CompareData(InsightCsv_path,SFTP_FolderPath):
    """
    比较两边同一个工站和同一天的数据
    :parameter:InsightCsv文件 SFTP待合并csv文件的文件夹
    :return:
    """
    usecols = [0,1,2,3,4,5,6]
    column_names = ['Site', 'SerialNumber', 'Special Build Description', 'Station ID', 'Test Pass/Fail Status','StartTime', 'EndTime']
    #调用格式化函数 获取处理后的insight csv文件路径
    InsightData_Path=Formatting_InsightCsv.Formatting_InsightCsv(InsightCsv_path)
    #调用合并函数 获取合并后的SFTP CSV文件路径 以及工站名 日期
    SFTPData_Path,StationName,Date=CombineData.CombineData(SFTP_FolderPath)
    #读取csv
    df_insight=pd.read_csv(InsightData_Path)
    #df_insight.to_csv("1.csv")
    df_sftp=pd.read_csv(SFTPData_Path)
    #统计行数
    Insight_Total=len(df_insight)
    #print(Insight_Total)
    IT_Total=len(df_sftp)

    # column_names = ['Site', 'Product', 'SerialNumber', 'Special Build Name', 'Special Build Description', 'Unit Number',
    #                 'Station ID', 'Test Pass/Fail Status', 'StartTime', 'EndTime']
    #找相同数据
    SameData=pd.merge(df_insight,df_sftp,on=['SerialNumber','StartTime', 'EndTime'],how='inner')#inner表示选两者都有的数据
    Consist_Count=len(SameData)

    IT_More=IT_Total-Consist_Count#SFTP有的数据 Insight没有的那部分
    IT_More_Rate='{:.2f}%'.format(IT_More*100/Insight_Total)


    #两个dataframe对象相加并删除重复值而且不保留任何重复项 剩下的为 我有你没有 你有我没有 的数据集
    DifferentData=(df_insight.append(df_sftp)).drop_duplicates(keep=False)
    #print(Different_Count)
    DifferentData=pd.DataFrame(DifferentData)#转换为dataframe对象
    print("Date:{}  StationName:{}".format(Date,StationName))
    print("Consist_Count:{}".format(Consist_Count))
    #print("SameData记录数是：{}".format(len(SameData)))
    #print("DifferentData记录数是：{}".format(len(DifferentData)))
    print("Insight_Total:{}".format(Insight_Total))
    print("IT_Total:{}".format(IT_Total))
    #print(Date)
    #print(InsightData_Path,SFTPData_Path)
    IT_Missing=Insight_Total-Consist_Count
    IT_Missing_Rate='{:.2f}%'.format(IT_Missing*100/Insight_Total)
    #IT_Missing_Rate = ('%2f' % IT_Missing_Rate)#格式化
    return StationName,Date,Insight_Total,IT_Total,Consist_Count,IT_More,IT_Missing,IT_More_Rate,IT_Missing_Rate,SameData,DifferentData
#CompareData(r"E:\Insight_VS_SFTP\Data\InsightData\2019-07-05\LOG-COLLECTION\Export-ID-115213002881644-2019-07-05T00_00_00-2019-07-06T00_00_00-ProductCodes-15-LOG-COLLECTION-Versions-5.csv.csv",r"E:\Insight_VS_SFTP\Data\SFTPData\2019-07-05\LOG-COLLECTION")