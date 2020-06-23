def birthday(s, d, m):
    count = 0
    for val in s:
    	if m==1 and val == d:
    		count+=1
    		print(val)
    	if m==2 :
    		for u in s:
    			if (val+u )==d:
    				count+=1
    				print(u,val)
    	if m==3:
    		for u in s:
    			for v in s:
    				if (val + u +v )== d and val != u != v:                                                                  
    					count+=1
    					print(v,u,val)
    	if m== 4:
    		for u in s:
    			for v in s:
    				for w in s:
    					if (val+u+v+w)==d:
    						count+=1
    						print(w,v,u,val)

    return count

            
s = [2,3,2,1,2]
d = 3
m = 2
print(birthday(s,d,m))