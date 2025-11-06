from streamlit import header, write, text_input, button, warning, success, error
from math import sqrt
def calculo(delta):
    valor= (sqrt(delta))  / (2*a)
    return valor
header("Calculadora de Bhaskara")
write("calculadora de raizes de uma \n equação do segundo grau")
write("ax² + bx + c = 0")
a = text_input("valor de a:",)
b = text_input("valor de b:",)
c = text_input("valor de c:",)

if button("calcular raizes"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta=pow(b,2)- 4 * a *c
        write(f"o valor de delta é: {delta}")
        if delta <0:
            warning("não existem raizes reais para essa equação.")
        elif delta ==0:
            raiz= (-b + sqrt(delta)) / (2 * a)
            success(f"a equação possui uma raiz real: {raiz}")
        else:
            raiz1= (-b + sqrt(delta)) / (2 * a)
            raiz2= (-b - sqrt(delta)) / (2 * a)
            success(f"a equação possui duas raizes reais: {raiz1} e {raiz2}")
    except ValueError:
        error("por favor, insira valores numéricos válidos para a, b e c.")
    except ZeroDivisionError:
        error("o valor de 'a' não pode ser zero em uma equação do segundo grau.")