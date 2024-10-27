#data = 'techTFQ'
data = ('c++','java', 'Python','SQL')

for value in data:
    print('Currect value is -->',value)


dt = ('c#','Scala', 'Python','Pyspark')

for k in dt:
    print('Currect value is -->',k)
    if k == 'Pyspark':
        print('we are learning Pyspark!')
        break