# videoConverterTo8bBitArt
Este código converte vídeos para a arte 8 bit.
This code convert any video to 8 bit art 

## Este projeto foi gerado com uso da inteligência artificial Chat-gpt-3 da OpenAI.

## A linguagem de programação escolhida foi a python, pois ela apresenta bibliotecas mais práticas para este fim.

# 1. Escopo

Este é um projeto idealizado por mim, voltado para a cultura 8 bit art. Visto que há muitas opções de se converter imagens, mas não vídeos, então pensei em uma maneira que pudesse converter vídeos inteiros, já que após pesquisar, não consegui opções que fizesse isso, e as que encontrei não funcionavam bem. Diante dessa necessidade, cheguei no seguinte raciocínio:

# 2. A solução

O arquivo de vídeo, nada mais é do que uma série de imagens sobrepostas em uma determinada velocidade, dentro de um determinado tempo, e isso é conhecido como FPS (frames per second), o que nos dá a impressão de "movimento".

- Com ajuda da IA, validei o meu raciocínio proposto para me certificar se ele fazia sentido e se poderia melhorar algo nele, para assim partir para a implementação.

Após feito isso, percebi que o processo poderia ser divido em 3 etapas:

    I. Pegar esse vídeo e extrair cada frame e armazena-los em uma pasta mantendo a ordem numerica sequencial para cada um deles, pois isso seria importante no futuro; (Script passo 1).

    II. Após isso deveria pegar cada um desses frames e executar um outro algoritmo que pudesse aplicar o efeito respectivo em cada deles, armazenando-as em uma outra pasta. Para aplicar os efeitos, precisei pesquisar e testar algumas bibliotecas que pudessem, então encontrei uma que me agradou mais; (Script passo 2).

    III. E por último, após aplicado o efeito em todos os frames, só era preciso, juntar de volta eles para gerar novamente o vídeo, agora convertido, preservando o fps original. :-). (Script passo 3).



# 3. A implementação


- Fui guiando a IA, para que gerasse os códigos de cada etapa que eu necessitava, e corrigindo os eventuais bugs que iam surgindo conforme testa os scripts, até chegar num código funcional;

Então cheguei na primeiras versão funcional desse código o/.

Mas não era o suficiente, pois o processo estava demsiadamente demorado, então precisei passar para a etapa seguinte, para otimizar o código.

# 4. Melhorando a performace

    Como após chegar na primeira versão funcional, percebi que o seu processamento estava demorando muito para finalizar, busquei maneiras de otimizar o tempo de processamento com ajuda da IA, aplicamos algumas soluções:

        I. Diminuir a qualidade da imagem convertida;

        II. Usar mais de um núcleo do computador no processamento do código;

        III. Preparar o código para que pudesse realizar o processo de conversão de cada imagem de forma síncrona.


Após aplicar as melhorias no código, o objetivo da performace também foi atingido.


## E você pode conferir nesses dois links, os vídeos convertidos com uso desses scripts:

O vídeo do meme da dança da personagem Vandinha interpretado pela Jenna Ortege da séria netflix:

[Vídeo 1](https://www.youtube.com/shorts/2BafQtU3gvc "Bloody Mary Dance | Jenna Ortega Meme")

O famoso meme do árabe dançando:

[Vídeo 2](https://www.youtube.com/shorts/ccbopuxU5es "Arabe dançando")
# 6.  Futuras melhorias

    1. Organizar melhor este código;
    2. Buscar outras maneiras de otimizá-lo;
    3. Criar uma interface;
    4. Buscar uma maneira de processá-lo na nuvem para que não consuma recursos do meu equipamento;
    5. Falta adicionar o áudio pois no processo isso não é tratado
    6. Criar métricas e raelizar testes para medir quanto tempo está sendo ganhado no algoritmo otimizado em relação ao que não está otimizado.
    7. Criar uma estimativa de quanto tempo irá demorar para terminar o processo, pois atualmente eu apenas acompanho isso, nas informações do console.

# 7. Espero poder contar com a sua ajuda para evoluir esse programa e criar novas funcionalidades e até mesmo um grande aplicativo!


Obs.: Como disse, só tive tempo para trabalhar apenas 1 dias nele, portanto, muitas coisas precisam ser melhoradas, como não entendo muito de python, podem ser que hajam equívocos, erros ou apenas melhorias mesmo a serem feitas no código.

# 8. O Aprendizado

Eu destaco alguns pontos nesse exercício que eu propus:

    I. Ter um raciocínio crítico para poder chegar numa solução eficaz, mais do que pesquisas, foi necessário resgatar na memória informações de forma lógica para tal;

    II. A IA é muito eficaz, mas geralmente apenas responde exatamente o que lhe foi perguntado e algumas vezes pode dar códigos que contém alguns erros, mas ela é capaz de cruzar informações se você pedir isso.
    
    III. O Algoritmo serve para a finalidade de converter vídeos em arte 8 bit, mas poderia ser muito reaproveitado se no processo de conversão fossem aplicados efeitos diferentes.