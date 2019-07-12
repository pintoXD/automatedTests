### Para geral ###
* Como saber se o sistema está em baixo consumo ou não? (Entra quando o painel tá apagado) 
*  __Rever a função de aquisição do painel de leds. Está sempre mandando 4 bytes e todos são 0.__
* De onde que tá sendo pego o valor analógico de leitura da tensão na bateria?


### __Funções de base testadas__ ###



##Testar se o cenário 4 do caso 7 está realmente ok##
Devido a uma imprecisão na leitura do AD, o valor analógico de limiar entre 3.8V e 3.9V está flutuando muito.
Necessário, assim, então, fazer um teste com um valor de tensão que faça com que a placa do produto apite 3 vezes e a potência luminosa seja maior que 0, para só então analisar qual o valor do AD para essa situação.

## Testar os tempos de aquisição no Docklight ##

## teste bateria ##

Caso não haja, criar um caso de testes que verifique se a leitura obtida do A/D da placa de aquisição está
de acordo com a leitura mostrada no painel de leds da placa principal.

## Adicionar cenário de teste ## 
Adicionar cenário 5 ao test de caso 7: Tensão abaixo da carag mínima tem de emitir um bipe longo (500ms)

## Aqruivo de configuração ##






