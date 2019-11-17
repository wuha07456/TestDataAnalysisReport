import pandas as pd
import os
import datetime
def CombineData(FolderPath):
    """
    按天合并SFTP文件同一工站的所有数据
    :param FolderPath:存放CSV文件的文件夹
    :return:CombineFilePath:合并后的CSV保存路径
    使用Pandas拼接多个CSV文件到一个文件（即合并）
    """
    #进入目标文件夹目录
    os.chdir(FolderPath)
    #将该文件夹下的CSV文件名保存进列表
    file_list=os.listdir()
    #取出日期和工站名称用于命名合并后的文件
    StationName=FolderPath.split('\\')[-1]
    Date=FolderPath.split('\\')[-2]
    #print(StationName)
    ConbineFileName=FolderPath.split('\\')[-1]+"-"+FolderPath.split('\\')[-2]
    ConbineFileName = ConbineFileName+".csv"
    #print(ConbineFileName)
    #print(file_list)
    #读取第一个CSV文件并保存表头
    column_names = ['Site','SerialNumber','Special Build Description','Station ID','Test Pass/Fail Status','StartTime','EndTime']
    column_names=['Site','Product','SerialNumber','Special Build Name','Special Build Description','Unit Number','Station ID','Test Pass/Fail Status','StartTime','EndTime']
    #定义要读取的指定列
    usecols=[0,2,4,6,7,8,9]
    usecols=[0,1,2,3,4,5,6,7,8,9]
    df=pd.read_csv(FolderPath+'\\'+file_list[0],usecols=usecols,encoding='gbk',sep=',',header=None)
    #把数据写入一个新的CSV文件
    df.to_csv(ConbineFileName,index=None,header=None)
    #print(df.values)
    # 循环遍历列表中各个CSV文件名，并追加到合并后的文件
    for i in range(1,len(file_list)):
       df=pd.read_csv(FolderPath+'\\'+file_list[i],usecols=usecols,encoding='gbk',sep=',',header=None,index_col=None)
       df.to_csv(ConbineFileName,mode='a+',index=None,header=None)
    #CombineFilePath + '\\' +
    #处理合并后的文件 去重 去空行空列
    df = pd.read_csv(ConbineFileName, usecols=usecols,names=column_names, encoding='gbk', sep=',',header=None)
    df.dropna(how='all',inplace=True)#all 是全为空才删
    df.drop_duplicates(keep='first',inplace=True)
    df.drop(index=[0,1,2,3,4,5,6], inplace=True)
    #StationName=df['Station ID'].values[0]
    #按Date筛选信息 只要date日期内的信息
    Date = datetime.datetime.strptime(Date, '%Y-%m-%d')  # strptime()内参数必须为string格式
    yestoday = Date - datetime.timedelta(days=1)
    tomorrow = Date + datetime.timedelta(days=1)
    df['StartTime'] = pd.to_datetime(df['StartTime'])  # 将数据类型转换为日期类型
    df = df[(df['StartTime'] >= Date) & (df['StartTime'] < tomorrow)]#按日期范围筛选

    #保存数据
    df.to_csv(ConbineFileName,index=None,encoding='gbk')

    current_path=os.getcwd()#获取当前路径
    CombineFilePath=current_path+"\\"+ConbineFileName#拼接路径
    return CombineFilePath,StationName,Date#返回最终处理后的文件路径,工站，日期

#filepath=CombineData(r"E:\Insight_VS_SFTP\Data\SFTPData\2019-07-05\LOG-COLLECTION")
#print(filepath)

