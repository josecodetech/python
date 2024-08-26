peso_01 = 1.50
peso_02 = 1.70
peso_03 = 2.10

cantidad_01 = int(input("Cuantos enviamos del producto 01? "))
cantidad_02 = int(input("Cuantos enviamos del producto 02? "))
cantidad_03 = int(input("Cuantos enviamos del producto 03? "))

peso_env_01 = cantidad_01*peso_01
peso_env_02 = cantidad_02*peso_02
peso_env_03 = cantidad_03*peso_03

peso_total = peso_env_01 + peso_env_02 + peso_env_03
print(f"Del producto 01 envia un peso de {round(peso_env_01,2)} Kg")
print(f"Del producto 02 envia un peso de {round(peso_env_02,2)} Kg")
print(f"Del producto 03 envia un peso de {round(peso_env_03,2)} kg")
print(f"El peso enviado total es de {round(peso_total,2)} Kg")

# %%
