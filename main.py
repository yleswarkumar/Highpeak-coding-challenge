input = dict()

number_of_employees = 0
with open('input.txt', 'r') as file:
    skip = 1
    for i in file:
        i = i.strip('\n')
        if skip == 1:
            number_of_employees = int(i[-1])
            skip = 2
            continue


        i = i.strip(' ')


        print(i)
        item = i.split(': ')
        print (item)

        if(len(item)>1):

            input[item[0]] = int(item[1])

    print(input)
    # input = {k: v for k, v in sorted(input.items(), key=lambda i: i[1])}



name=list(({key: value for key, value in sorted(input.items(), key=lambda item: item[1])}))
val=[]
for i in name:
    val.append(input[i])
ng=len(input)
i=0
k=0
mv=[]
for i in range(0,ng-number_of_employees):
   mv.append(abs(val[i]-val[i+number_of_employees]))

i=mv.index(min(mv))
i=i+1
for j in range(i,i+number_of_employees):
    print(name[j],val[j])

with open('output.txt', 'w') as file:

    file.write("The goodies selected for distribution are: \n")
