cuentas = []
for i in range(1, 11):
    cuenta = {
    "cuenta": int(input(f"Ingrese el numero de la cuenta: ")), 
    "saldo": float(input(f"Ingrese el saldo de la cuenta: ")),
    }
    cuentas.append(cuenta) 
cuentas_ordenadas = sorted(cuentas, key=lambda cuenta: cuenta["saldo"], reverse=True);

print("Cuentas ordenadas de mayor a menor saldo:")
for cuenta in cuentas_ordenadas:
    print(f"Cuenta {cuenta['cuenta']}: ${cuenta['saldo']}: ")
