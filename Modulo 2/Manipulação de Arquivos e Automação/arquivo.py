arquivo=open ("numeros.txt","w")
for linha in range(1,50000):
    arquivo.write("%dsarah \n" % linha)
arquivo.close()