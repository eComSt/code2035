for i in reversed(range(1,2**18-1)):    	
    b=2**18    
    while(b>0):b=b-i    	
    if b==0:print(i)