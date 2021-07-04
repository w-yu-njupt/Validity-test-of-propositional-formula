import re
print("规定：使用大写字母表示命题变元，共有五个联结词(使用逗号隔开)：!(表示非),|(表示或),&(表示且),@(表示单条件),$(表示双条件)以及符号()。")
print("欢迎进入命题公式检测程序，输入exit退出程序")
while(1):
    str = input("请输入要判断的命题公式：")
    if(str=="exit"):
        break
    else:
        j = 0
        for i in range(0,len(str)):
            #第一趟遍历判断输入是否符合规定
            if(not(((str[i]>="A")\
                    and(str[i]<="Z"))\
                   or(str[i]=="!")\
                   or(str[i]=="|")\
                   or(str[i]=="@")\
                   or(str[i]=="$")\
                   or(str[i]=="&")\
                   or(str[i]=="(")\
                   or(str[i]==")"))):
                j = 1
                break
        if(j):
            print("该输入不符合规定")
        else:
            if(not((str[0]>="A")\
                   and(str[0]<="Z")\
                   or(str[0]=="!")\
                   or(str[0]=="("))):#判断第一个字符是否合法
                print("该命题不合法")
            else:
                if((str[len(str)-1]=="!")\
                   or(str[len(str)-1]=="|")\
                   or(str[len(str)-1]=="$")\
                   or(str[len(str)-1]=="@")\
                   or(str[len(str)-1]=="*")):
                    #判断最后一个字符是否合法
                     print("该命题不合法")
                else:
                    num_letter = 0
                    num_sign = 0            
                    for i in range(0,(len(str))):
                        #第二趟遍历判断是否有连续的命题变元或符号
                        if((str[i]>="A")and(str[i]<="Z")):
                            num_sign = 0
                            num_letter = num_letter+1
                            if(num_letter>=2):
                                break
                        else:
                            if((str[i]=="(")\
                               or(str[i]==")")\
                               or(str[i]=="!")):
                                #暂时不处理符号"()"和符号"!"
                                num_sign = 0
                            else:
                                num_letter = 0
                                num_sign = num_sign+1
                                if(num_sign>=2):
                                    break
                    if((num_letter>=2)or(num_sign>=2)):
                        print("该命题不合法")
                    else:
                        num_left = 0
                        num_right = 0
                        for i in range(0,(len(str))):
                            #第三趟遍历检测左右括号是否数量一致
                            if(str[i]=="("):
                                num_left = num_left+1
                            if(str[i]==")"):
                                num_right = num_right+1
                        if(not(num_left==num_right)):
                            print("该命题不合法")
                        else: 
                            if((re.search('\(\@',str))\
                            or(re.search('\(\$',str))\
                            or(re.search('\(\|',str))\
                            or(re.search('\(\)',str))\
                            or(re.search('\)\(',str))\
                            or(re.search('\!\)',str))\
                            or(re.search('\@\)',str))\
                            or(re.search('\$\)',str))\
                            or(re.search('\|\)',str))):
                                #利用正则匹配检测非法使用括号
                                print("该命题不合法")
                            else:
                                if str[0]=="!"\
                                   and (str[1]=="|"\
                                        or str[1]=="$"\
                                        or str[1]=="@"\
                                        or str[1]=="&"):
                                        print("该命题不合法")
                                else:
                                    tag = 1
                                    for i in range(1,(len(str))):
                                        #第四趟遍历检测“！”使用是否合法
                                        if(str[i]=="!"):
                                             if(not(((str[i+1]>="A" \
                                                      and str[i+1]<="Z")\
                                                     or(str[i+1]=="("))\
                                                    and((str[i-1]=="@")\
                                                    or(str[i-1]=="$")\
                                                    or(str[i-1]=="&")\
                                                    or(str[i-1]=="|")
                                                    or(str[i-1]=="(")))):
                                                tag = 0
                                                break
                                             else:
                                                tag = 1
                                    if(tag):
                                        print("该命题合法")
                                    else:
                                        print("该命题不合法")

