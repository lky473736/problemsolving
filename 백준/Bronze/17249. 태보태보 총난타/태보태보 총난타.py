taebo = input()

if "(^0^)" in taebo :
    standard = taebo.index("(^0^)")
    
print (taebo[0 : standard].count('@'), taebo[standard : ].count('@'))