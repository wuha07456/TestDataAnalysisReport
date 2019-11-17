#main 函数 调用所有功能模块
import datetime
from Functions import GenerateReport,FindCSV,FindFolder,CombineReport
def main(Insight_Folder,Sftp_Folder):
    """
    调用所有模块函数 实现最终功能
    :parameter 两种数据的文件夹路径
    :return:
    """
    #获取所有Insight csv文件路径

    Insight_csvpath=FindCSV.FindCSV(Insight_Folder)
    #print(len(Insight_csvpath))
    #获取所有要合并的SFTP CSV文件夹路径
    Sftp_folderpath = FindFolder.FindFolder(Sftp_Folder)
    #print(len(Sftp_folderpath))
    #循环调用生成报表函数
    Report_filepath=[]#存放报表列表

    if len(Insight_csvpath)==len(Sftp_folderpath):
        for i in range(len(Insight_csvpath)):
            #返回的报告路径依次保存在列表 Report_filepath 中
            Report_filepath.append(GenerateReport.GenerateReport(Insight_csvpath[i],Sftp_folderpath[i]))
            print("******************************************\n")
    else:
        print("删除多余处理过的文件再操作")
    # 汇总所有工站的报表
    CombineReport.CombineReport(Report_filepath)

if __name__ == '__main__':

    Insight_Folder=r"C:\Users\lide\Desktop\TestDataAnalysis\TestDataAnalysis\Data\InsightData\2019-07-05"
    Sftp_Folder=r"C:\Users\lide\Desktop\TestDataAnalysis\TestDataAnalysis\Data\SFTPData\2019-07-05"
    starttime = datetime.datetime.now()
    # 调用main函数
    main(Insight_Folder,Sftp_Folder)
    endtime = datetime.datetime.now()
    print(u"报表已生成，耗時:", (endtime - starttime).seconds, u"秒")

