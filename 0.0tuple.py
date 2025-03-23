# no declaration, only assignment
# 普通括号，无元祖效果，实际声明的是int。这里的括号被认为是数学运算中的普通括号了。
intA = (1)
stringA = ('1')
# 逗号声明单元素元祖
tupleA = (1,)
# 多元素元祖
tupleB = (1,2)
# 括号可省略
tupleA1 = 1,
# 括号可省略，多元素元祖
tupleB1 = 1,2
# 空元祖必须用空括号
c = ()
print(intA,type(intA),'\n',stringA,type(stringA),'\n',tupleA,type(tupleA),'\n',tupleB,type(tupleB),'\n',tupleA1,type(tupleA1),'\n',tupleB1,type(tupleB1),'\n',c,type(c))
print(intA,isinstance(intA,str))
'''
immutable
'''

# tupleA[0] = 2 