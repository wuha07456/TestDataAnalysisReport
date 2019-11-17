import os
def FindCSV(CSVFolderPath):
    """
    找到文件夹及子文件夹中所有csv文件
    :parameter 放了csv文件的文件夹路径
    :return: 保存所有csv绝对路径的列表 AllCSVPathList
    """
    rootdir=os.path.join(CSVFolderPath)
    AllCSVPathList=[]#用于保存所有csv的路径
    #遍历所有文件夹和子文件夹
    for (dirpath,dirnames,filenames) in os.walk(rootdir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.csv':
                AllCSVPathList.append(dirpath+'\\'+filename)

    #去重
    #AllCSVPathList=list(set(AllCSVPathList))
    #print(len(AllCSVPathList))
    return AllCSVPathList
#FindCSV(r"E:\Insight_VS_SFTP\Data\InsightData\2019-07-05")
#FindCSV(r"C:\Users\F1227439\Desktop\2019-07-05")
