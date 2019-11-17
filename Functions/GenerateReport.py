import xlwt
from Functions import CompareData,CombineData,Excel_Style,Formatting_InsightCsv
import pandas as pd
import datetime
def GenerateReport(InsightCsv_path,SFTP_FolderPath):
    """
    生成报表
    :parameter Insightcsv文件路径 SFTP需要合并csv的文件夹
    :return: Report_filepath报表的路径
    """

    #调用CompareData函数 获取返回值
    StationName, Date, Insight_Total, IT_Total, Consist_Count,IT_More,IT_Missing,IT_More_Rate,IT_Missing_Rate,SameData,DifferentData\
        =CompareData.CompareData(InsightCsv_path,SFTP_FolderPath)
    # 相关数据写入Excel 制作报表
    #定义报表保存路径
    #print(Insight_Total,IT_Total,Consist_Count)
    strDate=datetime.datetime.strftime(Date, '%Y-%m-%d')

    Report_filepath = 'C:\\Users\\lide\\Desktop\\TestDataAnalysis\\TestDataAnalysis\\Report\\' + strDate+'\\'+strDate +'_'+StationName+'_D42-D43_DataValiResult.xls'
    # 新建一个Excel
    report = xlwt.Workbook()
    # 添加sheet
    Summary_sheet = report.add_sheet("Summary")
    Station_sheet = report.add_sheet(StationName)
    # 写Summary子表
    Summary_Column_names = ['Station', 'Insight Total', 'IT Total', 'Consist Count', 'IT More',
                    'IT Missing', 'IT More Rate', 'IT Missing Rate', 'Miss File Or Comment']
    for i in range(len(Summary_Column_names)):
        Summary_sheet.write(0, i, Summary_Column_names[i])  # 写表头
    #写Summary内容
    Summary_sheet.write(1,0,StationName)
    Summary_sheet.write(1, 1, Insight_Total)
    Summary_sheet.write(1, 2, IT_Total)
    Summary_sheet.write(1, 3, Consist_Count)
    Summary_sheet.write(1, 4, IT_More)
    Summary_sheet.write(1, 5, IT_Missing)
    Summary_sheet.write(1, 6, IT_More_Rate)
    Summary_sheet.write(1, 7, IT_Missing_Rate)

    #先保存summary
    report.save(Report_filepath)
    #然后读取出来存为dataframe
    df_summary=pd.read_excel(Report_filepath)

    #写sheet 进Excel
    writer=pd.ExcelWriter(Report_filepath)#创建一个writer对象
    df_summary.to_excel(writer,'Summary',index=None)#写sheet summary
    column_names = ['SerialNumber', 'Special Build Description', 'Station ID', 'Test Pass/Fail Status',
                    'StartTime', 'EndTime','IT MoreOrMissing']
    DifferentData.to_excel(writer,StationName,index=None,columns=column_names)#写sheet 工站
    writer.save()
    return Report_filepath

#GenerateReport("E:\\Insight_VS_SFTP\\Data\\InsightData\\2019-07-05\\LOG-COLLECTION\\Export-ID-115213002881644-2019-07-05T00_00_00-2019-07-06T00_00_00-ProductCodes-15-LOG-COLLECTION-Versions-5.csv.csv","E:\\Insight_VS_SFTP\\Data\\SFTPData\\2019-07-05\\LOG-COLLECTION")
#
#GenerateReport(r"E:\Insight_VS_SFTP\Data\InsightData\2019-07-05\RACK1\Export-ID-115213002881123-2019-07-05T00_00_00-2019-07-06T00_00_00-ProductCodes-15-RACK1-Versions-4.csv.csv",r"E:\Insight_VS_SFTP\Data\SFTPData\2019-07-05\RACK1")
#print(filepath)