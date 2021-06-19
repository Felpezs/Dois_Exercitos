<h1>Dois Exércitos:</h1>

Imagine que dois exércitos, localizados em pontos distintos, necessitem coordenar um ataque a uma cidade fortificada que os separa. Para realizar o ataque com sucesso, o general do exército Azul envia um mensageiro para o exército vermelho, que obtém a mensagem com o horário do ataque. Após, o general do exército vermelho envia um mensageiro para o exército azul, confirmando ou não o horário do ataque.
<br><br>
No entanto, os mensageiros podem ser capturados pela cidade fortificada, fazendo com que a mensagem não chegue nos exércitos. Dessa forma, é configurado o problema dos dois exércitos, um problema insolúvel que pode ser visto com mais detalhes na página do <a href="https://pt.wikipedia.org/wiki/Problema_dos_dois_generais#:~:text=Dois%20ex%C3%A9rcitos%2C%20cada%20um%20liderado%20por%20um%20general%2C,meio%20do%20envio%20de%20mensageiros%20atrav%C3%A9s%20do%20vale."> Wikipédia </a>.

---

<h1>O Projeto:</h1>

Esse projeto foi desenvolvido utilizando a linguagem de programação Python (versão 3.9.2), com tempos pré-determinados a fim de definir se um mensageiro foi capturado ou não em sua travessia, sendo que a captura foi definida por meio de probabilidades.
Ademais, há um limite pré-determinado de mensageiros, sendo 5 do exército vermelho e 10 do exército azul.
<br><br>
Nesse projeto, o algoritmo finaliza em duas situações:
<ul>
	<li>Todos os mensageiros de um dos exércitos são capturados, configurando uma derrota</li>
	<li>Os exércitos conseguem combinar um horário e conseguem executar o ataque, configurando uma vitória</li>
</ul>

