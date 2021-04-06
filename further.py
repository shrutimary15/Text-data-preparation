import pandas as pd     # importing packages required
# saved the input file as input.txt
f = open('input.txt', encoding='utf-8')
h = f.readlines()   # solving the problem while reading the file by encoding
# separating the list of questions and answers and saving it in different list
i = 0
que_list = []
ans_list = []
l = len(h)-1
que = open('que.txt', 'w')
ans = open('ans.txt', 'w')
for ele in h:
    if i != l:
        u = len(ele)
        tlist = h[i][0]
        flist = h[i][u-2]
        addlist = h[i][4:8]
        if tlist == "0" or tlist == "1" or tlist == '2' or tlist == '3' or tlist == '4' or tlist == '5' or tlist == '6' or tlist == '7' or tlist == '8' or tlist == '9':
           while flist !='?':
            que_list = ele
            que.write(ele.rstrip()+'\n')
        elif flist == '?':
            que_list = ele
            que.write(ele.rstrip())

        else:
            ans_list = ele
            ans.write(ele.rstrip()+"\n")
            if ele[0:6] != 'Answer' and ele[0] != '\n':
                que.write("\n")
        i = i+1

que.close()
ans.close()
que = open('que.txt', 'r')
ans = open('ans.txt', 'r')

# Converting each text file into csv
q = pd.read_csv(que, delimiter='\n', skip_blank_lines=False, names=['Question'])
a = pd.read_csv(ans, delimiter='\n', skip_blank_lines=True, names=['Answer'])
a.to_csv('answer.csv')
q.to_csv('question.csv')

# concat 2 csv to form combined csv
inputs = ['question.csv', 'answer.csv']
df = (pd.read_csv(f, sep=',') for f in inputs)
combined = pd.concat(df, axis=1)
combined.drop(["Unnamed: 0"], axis=1, inplace=True)
combined.to_csv("Output.csv")
