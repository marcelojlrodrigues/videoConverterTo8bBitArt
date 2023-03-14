# videoConverterTo8bBitArt
This code convert any video to 8 bit art 


## Este projeto foi gerado com uso da inteligência artificial Chat-gpt da OpenAI.

## E usando a tecnologia python, pois ela apresenta, as bibliotecas mais práticas para este fim.

Este é um projeto idealizado por mim voltado para a cultura 8 bit art. Visto que há muitas opções de se converter imagens para a arte 8 bit, pensei em uma maneira de se converter vídeos inteiros, já que não consegui encontrar na internet nenhum aplicativo que fizesse isso funcionar bem. Diante dessa necessidade, cheguei no seguinte raciocínio:

1. O arquivo de vídeo, nada mais é do que uma série de imagens sobrepostas em uma determinada velocidade, dentro de um determinado tempo, e isso é o FPS (frames per second).

2. Logo, para converter o vídeo aplicando efeitos, constatei, que eu poderia dividir a solução no código em 3 partes / passos:

    1. Pegar esse vídeo e extrair cada frame e armazena-los em uma pasta mantendo a ordem numerica sequencial de cada arquivo de imagem exatraído; (Script passo 1).

    2. Após isso deveria pegar cada frame desse e executar um outro algoritmo que copiasse para um outra pasta e pudesse aplicar o efeito respectivo em cada um desses frames, assim obtendo o efeito esperado em cada arquivo que foi aplicado este efeito, para isso precisei pesquisar bibliotecas e testar algumas; (Script passo 2).

    3. E por último, após aplicado o efeito em todas as imagens, só era preciso, juntar todos os frames, na mesma velocidade de que foi descompacatada, e gerar o arquivo de vídeo novamente :-). (Script passo 3).

3. Como eu não chegaria nesse resultado sozinho em apenas 1 dias, que foi o tempo que eu tinha (domingo, já que não sou assinante também :-/), aproveitei para fazer uso da inteligência artificial para me ajudar com essa minha ideia:

    1. Validei se o meu raciocínio proposto para a solução para me certificar se ele fazia sentido;

    2. Fui guiando a IA, para que gerasse os códigos que eu necessitava, e corrigir os eventuais bugs que iam aparecendo, até chegar num código funcional;

    3. O Objetivo foi atingido, embora o processamento começou a demorar muito :-/;

    4. Então com a ajuda da própria IA, fui buscando maneiras para otimizar esse código, como ao invés de utilizar apenas um núcleo do processador, pudesse usar os 4 núcleos, assim diminuindo o tempo de processamento pois estaria usando um poder total de processamento da minha máquina.

4. Obtive êxito, apesar do tempo que leva para processar um vídeo curto, ele funciona.

5. Próximos passos e melhorias:
    1. Organizar melhor este código;
    2. Buscar outras maneiras de otimizá-lo;
    3. Criar uma interface;
    4. Buscar uma maneira de processá-lo na nuvem para que não consuma recursos do meu equipamento;
    5. Falta adicionar o áudio pois no processo ele não é adicionado.

6. Você também pode testá-lo, mas use vídeos curtos 

# Veja exemplos de vídeos convertidos:

[Vídeo 1](https://www.youtube.com/shorts/2BafQtU3gvc "Bloody Mary Dance | Jenna Ortega Meme")
[Vídeo 2](https://www.youtube.com/shorts/ccbopuxU5es "Arabe dançando")

Obs.: Os dois foram convertidos utilizando o mesmo algoritmo presente aqui nesse repositório!
