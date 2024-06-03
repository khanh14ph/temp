lst=open("/home4/khanhnd/improved_unimatch/data_synthetic/result_1.txt").read().split("\n")[:-1]
def preprocess(x):
    y=x.replace("\"","").replace("'","").replace(",","").replace(".","").replace("?","")
    num=[i for i in range(0,10)]
    for v in num:
        v=str(v)
        y=y.replace(v,"")
    y=y.lower()
    y=" ".join(y.split())
    return y
with open("/home4/khanhnd/improved_unimatch/corpus/chatgpt.txt","w")  as f:

    for i in lst:
        f.write(preprocess(i)+"\n")
