file=open('bird.txt','r')
bird_dic=dict()


for data in file:
    bird = data.strip()

    if bird in bird_dic:
        bird_dic(bird) += 1
    else:
        bird_dic(bird) = 1

for bird,value in bird_dic.items():
    print(bird,value)
    print()

print(bird_dic)
