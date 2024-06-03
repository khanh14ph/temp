from openai import OpenAI
from tqdm import tqdm
lst=open("/home4/khanhnd/improved_unimatch/data_synthetic/labeled_sample_mcredit.txt").read().split("\n")[473:]
with open("/home4/khanhnd/improved_unimatch/data_synthetic/temp.txt","w") as f:
    
    for i in tqdm(lst):
        print(i)
        client = OpenAI(
            api_key="sk-proj-DLexiKLWRwyLknVEvvWmT3BlbkFJNmnPQU5ABsmRyw4R87lO",
        )
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content":" tạo ra cho tôi 20 câu tương tự, cùng chủ đề với câu sau, có thể thay tên hoặc số liệu: "+i,
                    "temperature":1
                },
            ],
            
        )

        res=str(completion.choices[0].message.content)
        f.write(res+"\n")

