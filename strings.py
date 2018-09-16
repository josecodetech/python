#operaciones con strings o cadenas
#incluir con {}
curso='python'
version='3'
imprime="Curso de {}{}".format(curso,version)
print(imprime)
#cortar split
lenguajes="python;java;php"
print(lenguajes)
nuevo=lenguajes.split(";")
print(nuevo)
#join une con otro separador
nuevo2="/".join(nuevo)
print(nuevo2)