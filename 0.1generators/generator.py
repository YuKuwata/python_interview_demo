# function assignment
def count_up_to(max_num):
    current = 0
    while(current<max_num):
        yield(current)
        current+=1

gen = count_up_to(3)

print(next(gen))
print(next(gen))

for x in gen:
    print(f'iter: {x}')

# 双向通信
def generatorWithSend():
    received = yield "Start"
    received2 = yield f'Received: {received}'
    yield f'Received2: {received2}'

genSend = generatorWithSend()
print(next(genSend))
# print(next(gen.send("haha"))) --TypeError: can't send non-None value to a just-started generator
# print(next(genSend))  --Received: None
print(genSend.send("Hello"))
print(genSend.send("Hi"))
# print(next(genSend)) --StopIteration 因为生成器已执行完成