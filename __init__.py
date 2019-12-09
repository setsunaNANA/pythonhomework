import turtle
def tree(n,degree):
# 设置出递归条件
    if n<=1and degree<=10:
         return
    #首先让画笔向当前指向方向画n的距离
    turtle.forward(n)
    # 画笔向左转20度
    turtle.right(degree)
    #进入递归 把画n的距离缩短一半 同时再缩小转向角度
    tree(n/2, degree/1.3)
    # 出上层递归  转两倍角度把“头”转正
    turtle.left(2*degree)
    # 对左边做相同操作
    tree(n / 2, degree / 1.3)
    turtle.right(degree)
    # 退出该层递归后画原来长度
    turtle.backward(n)


if __name__ == '__main__':
    # 先把画笔角度转正
    turtle.left(90)
    tree(100, 60)