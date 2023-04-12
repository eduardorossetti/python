Implemente em Python o exercício abaixo.  No final compacte a pasta com os projetos e envie a atividade no prazo estipulado

a) Crie uma classe de nome Contribuinte, essa classe deverá representar um contribuinte qualquer e possuir os atributos nome, documento (CNPJ ou CPF) e renda bruta. Deve ter construtor e o método calcImposto().

b) Crie as classes PessoaFisica e PessoaJuridica, heranças de Contribuinte.
    Para a classe PessoaJuridica declare o atributo ano_de_fundaçao.
    Para a classe PessoaFisica declare o atributo sexo.
    O método que calcula o Imposto deve ser implementado nas duas classes de acordo com as regras abaixo.

Pessoa Física
 O imposto deve ser calculado de acordo com a tabela ao lado:
       Renda Bruta                        Alíquota   Parcela a Deduzir
  R$ 0,00 a R$ 1.400,00                 0%             R$ 0,00
  R$ 1.400,01 a R$ 2.100,00          10%            R$ 100,00
  R$ 2.100,01 a R$ 2.800,00          15%            R$ 270,00
  R$ 2.800,01 a R$ 3.600,00          25%            R$ 500,00
  R$ 3.600,01 ou mais                   30%            R$ 700,00
Por exemplo, se Gabriel recebe R$ 2500,00 por mês, o imposto que ele deverá pagar deve ser calculado da seguinte forma: de acordo com a sua faixa, a alíquota é 15% com a dedução de R$270,00:
     Salário x %alíquota – dedução à 2500,00 x 15% -270,00 = R$ 105,00

Pessoa Jurídica
 O imposto deve corresponder a 10% da renda bruta da empresa.
 
c) Crie a classe GrupoDeContribuintes com a finalidade de manter uma coleção de contribuintes (Pessoa Física ou Pessoa Jurídica em uma mesma lista). Declare os métodos:
. addContribuinte(contribuinte), que recebe um objeto que pode ser PessoaFisica ou PessoaJutidica e o insere na lista.
. getTotalImposto(), que retorna a quantidade total de imposto devido (somatório do imposto devido por cada contribuinte)
. getPorcentagemContribuintesFeminino(), que retorna a porcentagem de contribuintes do sexo feminino mantidas na coleção.