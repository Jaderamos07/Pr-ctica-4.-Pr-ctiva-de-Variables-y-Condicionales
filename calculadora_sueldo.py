# Definición de constantes
DESCUENTO_TSS = 0.0304  # 3.04% de descuento por seguridad social
RETENCION_ISR = 0.15     # 15% de retención del impuesto sobre la renta
BONIFICACION = 0.10      # 10% de bonificación

def calcular_sueldo_neto(sueldo_bruto, otros_descuentos=0):
    # Cálculo de descuentos
    descuento_tss = sueldo_bruto * DESCUENTO_TSS
    retencion_isr = sueldo_bruto * RETENCION_ISR
    bonificacion = sueldo_bruto * BONIFICACION
    
    # Cálculo del sueldo neto
    sueldo_neto = sueldo_bruto - (descuento_tss + retencion_isr + otros_descuentos) + bonificacion
    
    return descuento_tss, retencion_isr, bonificacion, sueldo_neto

def main():
    # Solicitar el sueldo bruto al usuario
    while True:
        try:
            sueldo_bruto = float(input("Ingrese el sueldo bruto del empleado: "))
            if sueldo_bruto < 0:
                print("El sueldo bruto debe ser un valor positivo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Solicitar otros descuentos
    while True:
        try:
            otros_descuentos = float(input("Ingrese otros descuentos (si no hay, ingrese 0): "))
            if otros_descuentos < 0:
                print("Los otros descuentos deben ser un valor positivo o cero. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Calcular los valores
    descuento_tss, retencion_isr, bonificacion, sueldo_neto = calcular_sueldo_neto(sueldo_bruto, otros_descuentos)

    # Presentar resultados
    print("\nResultados:")
    print(f"Sueldo Bruto: RD$ {sueldo_bruto:.2f}")
    print(f"Descuento por Seguridad Social (TSS): RD$ {descuento_tss:.2f}")
    print(f"Retención ISR: RD$ {retencion_isr:.2f}")
    print(f"Otros Descuentos: RD$ {otros_descuentos:.2f}")
    print(f"Bonificación: RD$ {bonificacion:.2f}")
    print(f"Sueldo Neto: RD$ {sueldo_neto:.2f}")

if __name__ == "__main__":
    main()
