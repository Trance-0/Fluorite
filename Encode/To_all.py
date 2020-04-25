def to_all(string,f,t):
    alpha_list={}
    beta_list={}
    for i in range(f):
        print("What can be represent as ",i," in string?")
        temp=input()
        alpha_list[temp]=i
    for k in range(t):
        print("What can be represent as ",k," in final string?")
        temp=input()
        beta_list[k]=temp
    org_data=list(string)
    container=[]
    for j in org_data:
        container.append(alpha_list[j])




