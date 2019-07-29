### Para geral ###
* Como saber se o sistema está em baixo consumo ou não? (Entra quando o painel tá apagado) 
*  __Rever a função de aquisição do painel de leds. Está sempre mandando 4 bytes e todos são 0.__
* De onde que tá sendo pego o valor analógico de leitura da tensão na bateria?
* Fazer limpeza do código no arquivo serialTeste.py. O código está muito poluído.

### __Funções de base testadas__ ###

#### get_batlvl ###

Funçãon está retornando um valor de leitura do conversor A/D,
contudo esse valor não está correspondendo a um valor aceitável. 
Foram realizados alguns testes, tanto lendo a tensão da bateria,
quanto lendo tensões geradas e ainda assim, a leitura não retorna 
um valor aceitável para conversão.
Por exemplo, valor lido na bateria é de 1434 quando deveria ser algo em torno do dobro.


## teste bateria ##

Caso não haja, criar um caso de testes que verifique se a leitura obtida do A/D da placa de aquisição está
de acordo com a leitura mostrada no painel de leds da placa principal.





#### get_buzzer ###

Aparentemente tá ok. Ele manda o número de tuplas que representam o número de bipes dados, mas os valores de tempo estão meio estranhos.
O primeiro membro da tupla está assumindo um valor inteiro entre 0 e 10, enquanto o segundo assume um valor inteiro entre 0 e 1000, ou mais que isso.

#### get_led_voltage ###

#### get_panel ####











### Teste de Caso 3 ###
#### Cenário 2 ####
* Falta implementar a validação dos tempos do buzzer em cada situação;
* Falta implementar teste de verificação da potência luminosa;
* Verificar com Leonel como o tempo de duração dos bipes são enviados para o computador
* Verificar com Leonel como o vetor de tempos relativos (A ordem) é enviado para o computador
* Verificar com Aleson se o vetor retornado pela função get_buzzer possui tamanho variável
* Falta implementar um PS do cenário dois ( tempo_botão < ON_OFF_TIME milissegunos )


### Teste de Caso 5 ###
#### Cenário 1 e 2 ###

* Foi notado que a função get_panel() não trata os casos em que
os leds estejam todos desligados. Uma atualização para cobrir esse caso é necessária.


### Teste de Caso 6 ###
#### Cenário 1 ###
* Falta validar o teste do cenário 1
