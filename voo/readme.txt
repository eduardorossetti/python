Escreva uma classe em Python que represente um voo. O voo possui no máximo 100 passageiros e a classe deve controlar a ocupação das vagas. Os dados do voo devem ser: o número do voo, o horário do voo (pode ser uma string) e uma forma para representar os assentos livres e ocupados (pode ser lista, string ou alguma outra estrutura). Faça ainda os seguintes métodos:

getProximoAssento() – retorna o número do assento livre mais próximo, a partir do assento número 1;
veficarAssento(numassento) – verifica se o número do assento recebido como parâmetro está ocupado, retorna um booleano;
ocupar(numassento) – ocupa determinado assento do voo cujo número é recebido como parâmetro e retorna o resultado – se o assento ainda não estiver ocupado retorna verdadeiro indicando operação bem sucedida, caso contrário retorna falso;
getVagas() – retorna o número de assentos vagos disponíveis (não ocupados) no voo;
getVoo() – retorna o número do voo;
getHoraVoo() – retorna a data do voo;
getMapaAssentos() – retorna uma string representando todos os 100 assentos do avião. Os assentos ocupados deverão ser representados por ‘X’ e os livres por ‘-‘. Considere que os assentos estão disponibilizados em 4 fileiras com 25 assentos cada uma. No exemplo abaixo podemos verificar que o avião está com pouca lotação, somente 13 assentos estão ocupados e a fileira 4 está totalmente desocupada.

