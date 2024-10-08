import os
os.path.dirname(__file__)#获取当前目录
os.path.dirname(os.path.dirname(__file__))#获取当前目录的上一级目录

#获取指定的目录
def fileDir(data):
    '''
    :param data: 目录
    :return: 返回
    '''

    base_path=os.path.dirname(os.path.dirname(__file__))
    print(os.path.join(base_path,data))
    return os.path.join(base_path,data) # 将获取到的目录返回


#获取路径下的文件,调用需要传递两个参数替换,否则使用默认的参数
def filePath(fileDir="data",fileName="data.xlsx"):
    '''
    :param fileDir: 目录
    :param fileName: 文件名称
    :return: 返回
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

def filePath_model(fileDir="data",fileName="rd_model.xlsx"):
    '''
    :param fileDir: 目录
    :param fileName: 文件名称
    :return: 返回
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

def wt_filePath_model(fileDir="data",fileName="wt_model.xlsx"):
    '''
    :param fileDir: 目录
    :param fileName: 文件名称
    :return: 返回
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)