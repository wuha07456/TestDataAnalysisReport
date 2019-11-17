import pandas as pd

#Report_filepath=['E:\\Insight_VS_SFTP\\Report\\2019-07-05\\2019-07-05_COMPASS-CAL_D42-D43_DataValiResult.xls','E:\\Insight_VS_SFTP\\Report\\2019-07-05\\2019-07-05_LOG-COLLECTION_D42-D43_DataValiResult.xls','E:\\Insight_VS_SFTP\\Report\\2019-07-05\\2019-07-05_RACK1_D42-D43_DataValiResult.xls']
def CombineReport(Report_filepath):
    """
    合并单个工站的报表 汇总到一个报表
    :param Report_filepath:
    :return:CombineReport_path 合并后的报告路径
    """
    #获取日期

    date=Report_filepath[0].split('\\')[7]
    #创建一个writer对象，用于把每个sheet内容依次写入新的Excel，不叠加在一个sheet里
    writer = pd.ExcelWriter(r'C:\Users\lide\Desktop\TestDataAnalysis\TestDataAnalysis\Report\\'+date+'_D42-D43_DataValiResult.xls')
    #先把Summary汇总一起
    df_summary=[]#用于存放每个Excel的Summary的dataframe
    for filepath in Report_filepath:
        df_summary.append(pd.read_excel(filepath,sheet_name='Summary'))
    #将多个dataframe 合并成一个dataframe
    df_summary=pd.concat(df_summary)
    #再写入Excel
    df_summary.to_excel(writer,'Summary',index=None)

    #再读写工站子表
    for filepath in Report_filepath:
        print(filepath)
        sheet_name=filepath.split('_')[1]#取出工站名称
        df=pd.read_excel(filepath,sheet_name=sheet_name)
        df.to_excel(writer,sheet_name,index=None)#按sheetname依次写入
    #保存文档
    writer.save()
#CombineReport(Report_filepath)
