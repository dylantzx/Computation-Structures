j = 30
k = 31

for i in range(k+1):
    print("XPartialProd"+str(i)+" A["+str(k)+":0]  B"+str(i)+"#"+str(k+1)+"   A["+str(k)+":0]B"+str(i)+" and2")
    k-=1    


for rows in range(j+1):
    a = rows -1
    count = 0
    print("// Column "+str(rows+1))
    if rows !=0:
        print("Xadd_col"+str(rows+1)+"0 A"+str(rows+1)+"B0    A"+str(rows)+"B1   ci_c"+str(rows)+"n"+str(count)+"   s_c"+str(rows+1)+"1    ci_c"+str(rows+1)+"n"+str(count)+" FA")
    else:
        print("Xadd_col"+str(rows+1)+"0 A"+str(rows+1)+"B0    A"+str(rows)+"B1   0         alu"+str(count+1)+"    ci_c"+str(rows+1)+"n"+str(count)+" FA")
    for columns in range(rows):
        count+=1
        if columns+1 != rows:
            print("Xadd_col"+str(rows+1)+str(columns+1)+" s_c"+str(rows+1)+str(columns+1)+"   A"+str(a)+"B"+str(columns+2)+"   ci_c"+str(rows)+"n"+str(count)+"   s_c"+str(rows+1)+str(columns+2)+"    ci_c"+str(rows+1)+"n"+str(count)+" FA")
        else:
            print("Xadd_col"+str(rows+1)+str(columns+1)+" s_c"+str(rows+1)+str(columns+1)+"   A"+str(a)+"B"+str(columns+2)+"   0         alu"+str(count+1)+"     ci_c"+str(rows+1)+"n"+str(count)+" FA")
        a-=1    
    print("\n")


