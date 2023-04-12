Baseado do Diagrama de Classes abaixo, implemente um código em Python que satisfaça essas condições.
Atividade pode ser feita em dupla.

No final compacte a pasta com os projetos e envie a atividade no prazo estipulado.
Lembre-se de colocar o nome dos 2 integrantes (se for o caso).

Implemente em Python uma solução para o Diagrama abaixo:

AgenciaBancaria
- contas : Conta()
- codigo : int
+ addConta (conta : Conta) : void
+ getConta (numeor : int) : Conta
+ listContas() : String

Conta
- numero : int
- titular :  String
- saldo : double
+ depositar (valor : double) : void
+ retirar (valor : double) : double