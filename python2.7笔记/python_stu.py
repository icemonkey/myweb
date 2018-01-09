#coding=utf-8
'''
python学习笔记 
'''

'''
        #验证输入是否合法
        if choice.isdigit():
            choice=int(choice)
            if choice>0 and choice<=len(product_list):
                #将用户选择商品通过choice取出来
                p_item=product_list[choice-1]

                #如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                if p_item[1]<saving:
                    saving-=p_item[1]

                    shopping_car.append(p_item)

                else:
                    print('余额不足，还剩%s'%saving)
                print(p_item)
            else:
                print('编码不存在')
        elif choice=='q':
            print('------------您已经购买如下商品----------------')
            #循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱'%saving)
            break
        else:
            print('invalid input')
'''

#购物车
product_list = [
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('bike',2000),
]
shopping_car = []
money = raw_input('Please input your money:')
if money.isdigit():
    money=int(money)
    print(u'            商品清单        ')
    check_status = 'True'
    while check_status:
        for k,v in enumerate(product_list,1):
            print(u'商品编号:' + str(k) + u',商品名称:' + v[0] + u',商品价格:' + str(v[1]))
        choice=raw_input(u'选择购买商品编号[退出,请按：q]：'.encode('gbk'))
        
        #判断整数
        if choice.isdigit():
            #输入正确
            choice=int(choice)
            try:
                if choice > 0 and choice <= len(product_list) + 1 :
                    #取出商品
                    p_item=product_list[choice - 1]
                    #判断钱数,商品加入购物车,余额减除
                    if p_item[1] < money:
                        money -= p_item[1]
                        shopping_car.append(p_item)
                    else:
                        print(u'余额不足，还剩%s'%money)
                    print(p_item)
                    #输入不是整数
            except:
                print(u'输入编号错误!!!!!!!!!!!!!!!')
        
        
        #退出
        elif str(choice) == 'q':
            print(u'------------您已经购买如下商品----------------')
            #循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print(u'您还剩%s元钱'%money)
            break
        
        #非法输入
        else:
            print('invalid input!!!!!!!!!!!!!!!')
else:
    print('invalid input!!!!!!!!!!!!!!!')       
        
        
        