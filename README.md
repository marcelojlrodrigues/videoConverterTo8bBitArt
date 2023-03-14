# videoConverterTo8bBitArt
Este código converte vídeos para a arte 8 bit.
This code convert any video to 8 bit art 

## Este projeto foi gerado com uso da inteligência artificial Chat-gpt-3 da OpenAI.

## A linguagem de programação escolhida foi a python, pois ela apresenta bibliotecas mais práticas para este fim.

Este é um projeto idealizado por mim, voltado para a cultura 8 bit art. Visto que há muitas opções de se converter imagens, mas não vídeos, então pensei em uma maneira que pudesse converter vídeos inteiros, já que após pesquisar, não consegui opções que fizesse isso, e as que encontrei não funcionavam bem. Diante dessa necessidade, cheguei no seguinte raciocínio:

1. O arquivo de vídeo, nada mais é do que uma série de imagens sobrepostas em uma determinada velocidade, dentro de um determinado tempo, e isso é conhecido como FPS (frames per second), o que nos dá a impressão de "movimento".

2. Logo, para converter o vídeo aplicando efeitos, constatei, que eu poderia dividir a solução do código em 3 etapas:

    1. Pegar esse vídeo e extrair cada frame e armazena-los em uma pasta mantendo a ordem numerica sequencial para cada um deles; (Script passo 1).

    2. Após isso deveria pegar cada um desses frames e executar um outro algoritmo que pudesse aplicar o efeito respectivo em cada uma dessas imagens, armezando elas em uma outra pasta, para isso precisei pesquisar e testar algumas bibliotecas que pudessem aplicar esse efeito da 8 bit art, então encontrei uma que me agradou; (Script passo 2).

    3. E por último, após aplicado ter todos os frames aplicados o efeito, só era preciso, juntar de volta eles para gerar o novamente o vídeo, preservando o fps original, assim geraria o novo arquivo de vídeo com o efeito aplicado :-). (Script passo 3).

3. Como eu sei que demoraria muito para chegar a esse resultado apenas buscando informações no google, e tinha apenas um dia para fazer isso (um domingo), resolvi aproveitar o uso do chat gpt, para ganhar tempo e testá-la, portanto segui estes passos:

    1. Validei o meu raciocínio proposto para a solução para me certificar se ele fazia sentido e se poderia melhorar algo;

    2. Fui guiando a IA, para que gerasse os códigos de cada etapa que eu necessitava, e corrigindo os eventuais bugs que iam surgindo, até chegar num código funcional;

    3. O Objetivo foi atingido, embora por exigir muito processamento computacional, o processo começou a demorar muito, então tive que reduzir a qualidade da imagem convertida para poder executá-lo em menor tempo, dado as limitações do meu Hardware :-/;

    4. Então com a ajuda da própria IA, fui buscando maneiras de otimizar este código, como percebi que o uso da CPU equanto executa o código era baixo, sugeri que não estava sendo utilizado todo o poder de processamento da minha máquina, então ela criou um algoritmo otimizado que ao invés de usar apenas 1 núcleo ele usava os 4 núcleos disponíveis, dessa maneira, apesar de não ter tido tempo de criar métricas para medir, percebi que o tempo de processamento foi reduzido, logo, a sua performace melhorou.

4. Resultado obtive êxito, apesar do tempo que leva para processar um vídeo curto, ele funciona conforme esperado, carece de melhorias.

5. Próximos passos e melhorias:
    1. Organizar melhor este código;
    2. Buscar outras maneiras de otimizá-lo;
    3. Criar uma interface;
    4. Buscar uma maneira de processá-lo na nuvem para que não consuma recursos do meu equipamento;
    5. Falta adicionar o áudio pois no processo isso não é tratado
    6. Criar métricas e raelizar testes para medir quanto tempo está sendo ganhado no algoritmo otimizado em relação ao que não está otimizado.
    7. Criar uma estimativa de quanto tempo irá demorar para terminar o processo, pois atualmente eu apenas acompanho isso, nas informações do console.

6. Você também pode testá-lo, mas use vídeos curtos 

# Veja exemplos de vídeos convertidos:
## Converti 2 memes bem famosos utlimamente:

A dança do personagem Vandinha interpretado pela Jenna Ortege, na séria da netflix:

[Vídeo 1](https://www.youtube.com/shorts/2BafQtU3gvc "Bloody Mary Dance | Jenna Ortega Meme")

E esse meme, que se tornou extremamente viral, do árabe dançando:

[Vídeo 2](https://www.youtube.com/shorts/ccbopuxU5es "Arabe dançando")

Obs.: Os dois foram convertidos utilizando o mesmo algoritmo presente aqui nesse repositório! Como disse, só consegui trabalhar apenas 1 dias nele, portanto, muitas coisas precisam ser melhoradas, como não entendo muito de python, podem ser que hajam equívocos ou melhorias a serem feitas nesses códigos.

## O que eu destaco nesse aprendizado, é que apesar de ter criado um algoritmo para converte-lo em arte 8 bit, de fato ele poderia ser convertido para outras finalidades, como por exemplo: vídeos p/b, videos cartoons, enfim, desde que exista um algoritmo que possa aplicar o efeito esperado, visto que o processamento dessa etapa leva muito tempo, já que cada segundo possa ter cerca de 60 frames.
