
def main():
    print('**********北京话生成器**********')
    Putonghua = input('请输入普通话：')
    Beijinghua = ''
    for index in range(len(Putonghua)):
        Beijinghua += Putonghua[index]+'儿'
    print(Beijinghua)
    pass

if __name__ == '__main__':
    main()