"""D. Temperatūras pārveidošana F->C
Funkcija akceptē vienu argumentu - temperatūru Fārenheita grādos,
un atgriež temperatūru Celsija grādos. Zemākā temperatūra
Celsija grādos var būt −273.15, tādēļ, ja aprēķinātā temperatūra ir zemāka, atgriež −273.15.

Argumenti:
    t {int vai float} -- temperatūra Fārenheita grādos
Atgriež:
    int vai float -- temperatūra Celsija grādos
"""

def temp_f(t):
    result = (t-32)*5/9
    if result<-273.15:
        result = -273.15
    return result