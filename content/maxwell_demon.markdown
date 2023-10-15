Title: O Demônio da Entropia e Informação
Date: 2023-07-29
Slug: demon
Lang: pt-br


# Introdução
*O quê um demônio tem a ver com entropia e informação?*

**Entropia** é um dos conceitos mais fascinantes, complexos e controversos da ciência.
 Ela surge na Física, no século 19 (ref), com o 
objetivo de entender o limite de eficiência de máquinas térmicas, essencial no contexto da Revolução Industrial.
Mais tarde, no século 20, uma nova grandeza é batizada
como entropia: Claude Shannon queria entender qual é o limite
de compressão de uma informação para que sua transmissão ocorra
sem perda. Embora notavelmente semelhantes (matematicamente equivalentes), não é óbvio que exista uma conexão conceitual 
intrínseca as entropias da termodinâmica e da teoria de informação. Entretanto, com o passar do tempo a conexão entre eles foi sendo estabelecida por diversos pesquisadores (ref) e aqui queremos explorar essa conexão pelo ponto de vista de um **experimento mental** extremamente influente, proposto no século XIX pelo físio escocês **James Clerk Maxwell**, que foi batizado por **Demônio de Maxwell** (sim, esse é o mesmo Maxwell que escreveu as 4 equações que descrevem Eletromagnismo: as equações de Maxwell).


# Primeira Lei da Termodinâmica

Antes de falarmos sobra a entropia propriamente dita, precisamos falar um pouco sobre a primeira lei da termodinâmica, que nada mais é
do que a lei de **conservação de energia** para um **sistema termodinâmico**.
Primeiramente, um sistema termodinâmico é essencialmente um sistema que é descrito por certas **variáveis macroscópicas**
típicas (ou, varíaveis ), como **pressão**, **volume**, **temperatura** e **número de partículas** (p, V, T, N) e é **separado
de um ambiente com o qual interage**. Um exemplo típico de sistema termodinâmico é um gás. 
*A primeira lei da termodinâmica essencialmente diz que a variação de energia de um sistema é igual a energia
transferida com seu ambiente*. Uma questão importante é que a energia do ambiente pode vir de duas formas: **trabalho** e **calor**.

Informalmente, trabalho pode ser entendido como um processo de transferência de energia que pode ser descrito
através de aplicação de forças macroscópicas (por ex.: quando você empurra ou levanta alguma coisa)
e tem a ver com forças microscópicas ordenadas (aplicadas na mesma direção).

Calor, por outro lado, pode ser intuitivamente entendido como a energia que é transferida entre corpos
de diferentes temperaturas, que naturalmente acontece do mais quente para o mais frio e tem a ver
com forças microscópicas desordenadas. 

Denotando a energia do sistema por $U$, trabalho nele realizado pelo ambiente por $W$ e calor transferido 
pelo ambiente por $Q$, a primeira lei da termodinâmica pode ser escrita como:

$$\Delta U =  W +  Q,$$

onde $\Delta$ é ser refere à variação, ou seja, $\Delta U$ é a variação de energia do sistema. Note que poderíamos também
convencionar $W$ e $Q$ como trabalho realizado e calor transferido pelo sistema no ambiente, que implicaria apenas numa troca de sinal.


# A segunda Lei da Termodinâmica e a Entropia

A Segunda Lei da Termodinâmica é uma lei que impõe restrições sobre processos e pode ser enunciada de diversas formas equivalentes:

**

*A Entropia do Universo tende a um máximo.*

Em termodinâmica, a variação da entropia de um  sistema com temperatura $T$ pode ser escrita como:

$$dS = \frac{\delta Q_{rev}}{T},$$

onde $\delta Q_{rev}$ é o calor trocado com o ambiente de forma *reversível*. Reversível aqui significa que todos os estados intermediários do sistema no processo são *estados de equilíbrio*. Um estado de equilíbrio, por sua vez, é uma estado cujas variáveis termodinâmicas não variam com o tempo. Na prática, processos reais podem se aproximar de processos reversíveis tipicamente se forem executados de maneira lenta suficiente, mas nunca serão de fato reversíveis.
Com a fórmula acima e a primeira lei da termodinâmica pode-se determinar a entropia de um sistema (ou sua variação) para diversas situações. Com isso, podemos enunciar a **segunda lei da termodinâmica** da seguinte maneira: Dado um sistema **isolado**, i.e., que não interage com um ambiente externo, **sua entropia não decresce**:

$$\Delta S \geq 0,$$

que é equivalente a dizer que podem ocorrer 2 coisas: ou ela não muda, que é o caso para sistemas em equilíbrio, ou ela cresce, que é o caso de sistemas fora do equilíbrio.

Só para ilustrar que a segunda lei é compatível com a definição de entropia termodinâmica e está de acordo com nossa intuição a respeito de temperaturas, suponha que um sistema isolado seja composto por 2 corpos, um com temperatura $T_1$ e o outro com temperatura $T_2$, onde $T_1 \geq T_2$, e que esses corpos estejam em contato e possam consequentemente trocar calor. O quê acontecerá com suas temperaturas com o passar do tempo? É evidente que o calor irá fluir do corpo mais quente ($T_1$) para o mais frio ($T_2$) até que ambos corpos eventualmente atinjam uma mesma temperatura intermediária de equilíbrio $T_3$, onde $T_1 \geq T_3 \geq T_2$.


$$dS = dS_1 + dS_2 = \frac{\delta Q_1}{T_1} + \frac{\delta Q_2}{T_2},$$

onde usamos apenas a aditividade da entropia e sua definição. Como $T_1 \geq T_2$, o calor flui de 1 pra 2 e temos que $\delta Q_2 \geq 0$, $\delta Q_1 \leq 0$ e ainda que $\delta Q_1 = - \delta Q_2$. Substituindo na equação acima, obtemos:

$$dS = \delta Q_2 \underbrace{ \left ( -\frac{1}{T_1} +  \frac{1}{T_2}\right )}_{\geq 0} \geq 0.$$

# Mecânica Estatística: A Entropia segundo Boltzmann e Gibbs


A Mecânica Estatística é a área da Física que tenta explicar sistemas termodinâmicos (descritos por variáveis macroscópicas) a partir do ponto de vista microscópico: *Como propriedades macroscópicas de sistemas termodinâmicos emergem a partir de propriedades microscópicas*? Como já mencionado, exemplos de variáveis macroscópicas típicas são *pressão* e *temperatura*, já exemplos de variáveis microscópicas são *posição*, *velocidade*, *massa* das partículas.

Um resultado importante, por exemplo, é que *temperatura está diretamente associada à velocidade das partículas* que compõem o sistema: quanto maior a temperatura de um sistema, maior a velocidade média de suas partículas. 

A pressão, por outro lado, se dá através das colisões entre as partículas do gás e as parades do recipiente. 
Quanto maior a temperatura, mais rápidas são as partículas em média e consequentemente maior é a força que exercem sobre as parades do recipiente quando colidem, o quê significa uma maior pressão, uma vez que **pressão é definida como força sobre área**. 

Já a energia interna de um sistema termodinâmico é simplesmente a soma das energias de cada partícula, tipicamente cinética e potencial. 

Um ponto importante para ressaltar aqui é que os *detalhes exatos das configurações microscópicas de um sistema não importam para sua descrição macroscópica*: o quê importa em geral são **valores médios** de variáveis microscópicas. Por exemplo, a temperatura é diretamente proporcional à energia cinética média e a pressão é diretamente proporcional à força média resultante das partículas exercida sobre as paredes do recipiente. Por isso falamos em *descrições estatísticas*.

E a **entropia**? Como ela pode ser compreendida do ponto de vista microscópico de um sistema? Essa é uma pergunta muito mais desafiadora e foi Ludwig Boltzmann quem deu o primeiro grande passo rumo à solução dessa questão. Ele demonstrou que a **entropia de um sistema está relacionada ao número de configurações microscópicas que ele pode assumir**. Mais precisamente, para um sistema isolado, a entropia é diretamente proporcional ao logarítmo do número de estados microscópicos acessíveis:

$$S = k \log \Omega,$$

onde $k$ é uma constante de proporcionalidade, chamada de **constante de Boltzmann** e $\Omega$ representa o *número de estados microscópicos acessíveis ao sistema*. Importante ressaltar que essa definição é válida para sistemas *isolados*, ou seja, sistemas que não trocam energia com seu ambiente, tendo ela portanto conservada. Para ilustrar, vamos supor um gás ideal, cujas partículas podemos essencialmente imaginar como "bolinhas" com massa sujeitas às Leis de Newton da Mecânica Clássica e que não interagem entre si (uma aproximação boa para altas temperaturas). Cada cada partícula possui posição e momento (massa x velocidade) a cada instante de tempo e **o conjunto de posições e momentos de todas partículas do gás num determinado instante é justamente o estado microscópico do sistema**. $\Omega$ é portanto o *número de possíveis combinações de posições e momentos* que as partículas podem assumir de modo que a energia total seja conservada, dada por um valor fixo $E$.

É importante ressaltar que a definição de entropia por Boltzman pressupõe que *todos os estados acessíveis ao sistema sejam equiprováveis*, fato conhecido como *postulado fundamental da mecânica estatística*. Ou seja, para um sistema com $\Omega$ estados acessíveis, cada estado tem probabilidade de $1/\Omega$ de ocorrer. 

 *Gibbs* generalizou a noção de entropia de Boltzman para o caso dos estados do sistema não serem necessariamente equiprováveis. Se indexarmos cada estado por um índice $i$, e denotarmos a *probabilidade do estado $i$* ocorrer por $p_i$ onde $i=1,...,\Omega$, então a **entropia de Gibbs** é dada por:

$$S = -k\sum_{i=1}^{\Omega}p_i\log p_i.$$

Note que para $p_i=1/\Omega$ e lembrando que $\sum_{i}p_i=1$, obtemos novamente a entropia de Boltzmann. 

# A Entropia de Shannon



# O Demônio de Maxwell

Considere um recipiente que contém um gás que se encontra em equilíbrio termodinâmico com temperatura $T$, ou seja, o gás está distribuído de maneira homogênea por toda extensão do recipiente (em qualquer pedaço do recipiente encontra-se aproximadamente a mesma densidade de partículas do gás) e sua temperatura é $T$ em todos os pontos. Temperatura, por sua vez, está diretamente relacionada com a velocidade média das partículas: quanto maior a temperatura, maior a velocidade média (ou energia cinética média).
Suponha agora que haja uma parede isotérmica (não permite a transferência de calor) que divide o recipiente em 2 compartimentos, *A* e *B*, e que contenha um pequeno orifício que pode ser aberto e fechado de modo a permitir a passagem de uma única partícula por vez entre os compartimentos. Suponha ainda que haja um ser inteligente capaz de rastrear as posições e velocidades de todas partículas de ambos compartimentos e capaz de abrir e fechar o orifício. Este ser seria então capaz de fazer o seguinte: toda vez que uma *partícula rápida* do compartimento $A$ se aproxima de *O*, ele abre *O* e a deixa passar para o compartimento $B$ e toda vez que uma *partícula lenta* do compartimento *B* se aproxima de *O*, ele abre *O*, deixando ela passar para o compartimento *A*. O quê eu quero dizer com *rápida* e *lenta*? A única coisa que importa é que a velocidade das partículas rápidas seja maior do que a velocidade média do gás ao passo que a velocidade das partículas lentas seja menor do que a velocidade média. É evidente que com a repetição desse procedimento por um tempo suficientemente longo, o compartimento *B* irá eventualmente conter apenas partículas rápidas e o compartimento *A* apenas partículas lentas. Em outras palavras, a temperatura do compartimento *B*, $T_B$, ficará maior que a temperatura do compartimento *A*, $T_A$: $T_B>T_A$. Em outras palavras, podemos dizer que *calor fluiu do compartimento A para o compartimento B*, esfriando assim *A* e esquentando *B*, que inicialmente tinham a mesma temperatura, $T$, onde $T_A<T<T_B$, *através seleção de partículas feita pelo demônio com base em sua capacidade de obter **informação** sobre velocidade e posição de cada partícula*.  

![image]({static}/images/maxwells_demon.png)



# Conexão entre energia e informação

Adsf [^wiki]
## References

[^Mama]: Author, A. (Year). Title of the work. Publisher
[^wiki]: (https://en.wikipedia.org/wiki/Maxwell%27s_demons)
