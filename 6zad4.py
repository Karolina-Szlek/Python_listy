

def podziel(n):
	nowysplit = []
	wolne = ''
	for wyraz in n:
	   if wyraz == ' ':
	      if wolne != '':
	         nowysplit.append(wolne)
	      wolne = ''
	   else:
	         wolne += wyraz
	if wolne:
	    nowysplit.append(wolne)
	
		
	print(nowysplit)











podziel("Ala ma    kota")
