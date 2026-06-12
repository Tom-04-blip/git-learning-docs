# def 数据特征·
x_data = [1,2,3]

# def 数据标签
y_data = [2,4,6]

# def 模型参数
W = 4

# def 模型预测
def forward(x):
    return W * x

# def 计算损失
def loss(x,y):
    lossvalue = 0
    for x_i,y_i in zip(x,y):
        y_pred = forward(x_i)
        lossvalue += (y_pred - y_i) ** 2
    return lossvalue / len(x)

# def 计算梯度
def gradient(x,y):
    grad = 0
    for x_i,y_i in zip(x,y):
        y_pred = forward(x_i)
        grad += 2 * x_i * (y_pred - y_i)
    return grad / len(x)

for epoch in range(100):
    #计算误差损失
    loss_value = loss(x_data,y_data)
    #计算梯度
    grad = gradient(x_data,y_data)
    W -= 0.01 * grad
    
    print(f'Epoch {epoch}, Loss: {loss(x_data,y_data)}, W: {W}')

print(f'预测: {forward(4)}')