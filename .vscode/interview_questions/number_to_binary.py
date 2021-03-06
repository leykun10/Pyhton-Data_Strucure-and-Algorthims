bits=[]
def number_to_binary(value):
    
    remainder=value%2
    val=value//2
    bits.append(remainder)
    if(val>0):
         number_to_binary(val)
    return

def number_to_binary2(value):
    bits=[]
    val = value
    while val>0:
        rem=val%2
        bits.append(rem)
        val=val//2
        
    return bits 

print(number_to_binary2(10))

