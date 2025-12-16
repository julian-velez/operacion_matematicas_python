# Se realiza una operación matemática respetando la prioridad de operadores:
# 1️⃣ Multiplicación (*)
# 2️⃣ División (/)
# 3️⃣ Suma (+)
# 4️⃣ Resta (-)

numeros = 65 + 9 * 7 - 12 / 8
# 9 * 7 = 63
# 12 / 8 = 1.5
# 65 + 63 - 1.5 = 126.5

# Se imprime el resultado usando un f-string
print(f'numeros = {numeros}')


# En esta operación se usan paréntesis para cambiar el orden de ejecución
# Los paréntesis se resuelven primero

numeros = (65 + 9) * (7 - 12) / 8
# (65 + 9) = 74
# (7 - 12) = -5
# 74 * -5 = -370
# -370 / 8 = -46.25

# Se imprime el nuevo resultado
print(f'numeros = {numeros}')
