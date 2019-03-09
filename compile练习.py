code1 = 'for i in range(0,10): print (i)'
compile1 = compile(code1,'','exec')

print(exec(compile1))


code2 = '1 + 2 + 3 + 4'
compile2 = compile(code2,'','eval')
print(eval(compile2))
