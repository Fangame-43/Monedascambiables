def exchange_money(budget_brl, exchange_rate_brl_to_usd):
    return budget_brl * exchange_rate_brl_to_usd

moneda = float(input("Escribe cuanto tienes: "))
tasa_cambio = float(input("Escribe la tasa de cambio: "))

resultado = exchange_money(moneda, tasa_cambio)
print(f"{moneda} reales equivalen a {resultado:.2f} ")