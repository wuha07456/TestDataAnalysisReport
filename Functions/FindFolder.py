import os
def FindFolder(CSVFolderPath):
    """
    找到包含csv文件的父文件夹路径
    :parameter 放了各个工站的csv文件的文件夹路径
    :return: 返回保存了各个工站的csv文件的文件夹绝对路径的列表 AllFolderPathList
    """
    rootdir=os.path.join(CSVFolderPath)
    AllCSVFolderList=[]#用于保存所有包含csv文件夹的路径
    #遍历所有文件夹和子文件夹
    for (dirpath,dirnames,filenames) in os.walk(rootdir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.csv':
                AllCSVFolderList.append(dirpath)
                break#找到一个csv文件就保存该文件父文件夹路径，退出循环找下一个文件夹
                #避免每发现一个子文件就添加父文件夹路径
    #print(AllCSVFolderList)
    return AllCSVFolderList
#FindFolder(r"E:\Insight_VS_SFTP\Data\SFTPData\2019-07-05")