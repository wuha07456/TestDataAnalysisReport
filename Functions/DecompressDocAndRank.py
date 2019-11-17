#用于整理归档csv文件
import os,gzip,shutil
FolderPath=r"E:\Python任务-20191024\FromSftp\FromSftp\2019-07-05"
Date=FolderPath.split('\\')[-1]
def DecompressDocAndRank(FolderPath):
    """
    1.遍历文件夹若有压缩文档则解压
    2.没有后缀名为.csv的文档改名新增后缀名.csv
    3.同一个日期和工站的csv文档放在一个按工站取名的文件夹
    :param FolderPath:
    :return: NewFoderPath
    """

    rootdir = os.path.join(FolderPath)
    AllCSVPathList = []  # 用于保存所有csv的路径
    # 遍历所有文件夹和子文件夹

    #解压
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames:
            #分离文件名和后缀
            portion=os.path.splitext(filename)
            if portion[1]=='.gz':
                os.chdir(rootdir) # 切换到当前目录
                # 开始解压
                un_gz(filename)
                #print(1)


    #添加后缀名 全部改成csv格式
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames:
            # 分离文件名和后缀
            portion = os.path.splitext(filename)
            if portion[1]=='':
                os.chdir(dirpath)#切换到当前目录
                new_filename=portion[0]+".csv"
                try:
                    if filename!=new_filename:#捕捉同名异常
                        os.rename(filename, new_filename)#变更文件名
                except FileExistsError:
                    pass
                #print(1)

    #解压改名处理完后，收集所有csv文件路径，保存到列表
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames:
            # 分离文件名和后缀
            portion = os.path.splitext(filename)
            if portion[1] == '.csv':
                AllCSVPathList.append(dirpath + '\\' + filename)
    print(AllCSVPathList)
    print(len(AllCSVPathList))
    #去重
    AllCSVPathList=list(set(AllCSVPathList))
    print(AllCSVPathList)
    print(len(AllCSVPathList))
    return AllCSVPathList


def un_gz(file_name):
    # 获取文件的名称，去掉后缀名
    f_name = file_name.replace(".gz", "")
    # 开始解压
    g_file = gzip.GzipFile(file_name)
    # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
    open(f_name, "wb+").write(g_file.read())
    g_file.close()

AllCSVPathList=DecompressDocAndRank(FolderPath)
#取出工站名 保存在列表中
StationNameList=[]
for i in range(len(AllCSVPathList)):
    StationNameList.append(AllCSVPathList[i].split('_')[3])
#去重
StationNameList=list(set(StationNameList))
print(len(StationNameList))
print(StationNameList)
#创建日期文件夹
os.chdir('E:\\')
print(os.getcwd())
if os.path.exists(Date)==False:
    os.mkdir(Date)
    print(1)
else:
    print("Folder is exist")
os.chdir(Date)#进入Date目录 按工站列表依次创建文件夹
for j in range(len(StationNameList)):
    if os.path.exists(StationNameList[j]) == False:
        os.mkdir(StationNameList[j])
        print(1)
    else:
        print("Folder is exist")

print(os.getcwd())
#遍历所有csv 如果属于StationNameList工站的就复制到对应工站文件夹中
for x in range(len(AllCSVPathList)):
    for y in range(len(StationNameList)):
        if AllCSVPathList[x].split('_')[3]==StationNameList[y]:
            print(1)
            #复制文件
            shutil.copy(AllCSVPathList[x],'E:\\'+Date+'\\'+StationNameList[y])




