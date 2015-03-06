Title: Como iniciar no Desenvolvimento Web
Date: 2014-09-28 00:46
Category: Python, Frameworks, Iniciante
Tags: frameworks, rails, sinatra, flask, django
Slug: iniciando-no-desenvolvimento-web
Author: Mário Idival
Summary: Minha visão de qual framework escolher para iniciar o
         desenvolvimento Web

# Introdução

A dias já pensava em criar algum post relacionado a este assunto. Vejo
muita gente perguntando, não só na comunidade Python, como iniciar o
desenvolvimento web. E a resposta sempre é a mesma, dependendo da
comunidade:

Ruby:

    Vai de Rails! É o melhor!

Python:

    Vai de Django! É o melhor!

Javascript:

    Vai de Express! É o melhor!

Mas a galera esquece de um detalhe, quem está perguntando provavelmente
nunca desenvolveu para Web, não sabe como funciona o basico de uma requisição http
e indicam um monstro para o(a) coitado(a) começar.

# Minha experiencia inicial

Quando quis iniciar nessa área, eu programava/estudava Ruby e
naturalmente até hoje, se qualquer um perguntar que framework Ruby usar
a resposta será uma, Rails. E comigo não foi diferente.

Comecei a estudar o Rails e as primeiras informações a respeito foram:

    Ruby on Rails (Rails) é um Web framework full-stack baseado em MVC,
    utiliza RESTful e facilmente pode gerar um CRUD.

_O Rails faz muito mais do que isso_


WTF **FULL-STACK**? WTF **MVC**? WTF **RESTFul**? WTF **CRUD**?

Para a galera que já conhece, isso já está no sangue (_ou deveria_),
são ideias simples. Mas para iniciantes, isso são coisas de outro mundo,
além de um novo mundo que eles estão querendo entrar, que é o do Desenvolvimento Web.

Eu estranhei tudo isso, sempre quando eu tentava fazer algo com o
scaffold e dava errado, achava que era alguma coisa relacionada a MVC ou
outro daqueles itens que eu não sabia para que servia.

E eu na idéia da galera que me indicou este framework, achava que ia
conseguir fazer coisas bem rapidamente, que poderia usar o form do html para
passar algumas coisas para o servidor, como um cadastro na minha app de agenda
telefônica.

E foi difícil. Tinha pouca idéia de relacionamento com tabelas e já
aparecia um Model. Tinha que mostrar alguns itens na minha pagina
inicial mas também não sabia como o Controller funcionava e como
pegava esses itens e muito menos em qual View eu deveria colocar.

Sem contar a principal duvida. Como que a pagina Web sabe qual
controller(ou view) é o correto? Quem inicia o desenvolvimento web,
não sabe o que é um Request, Response, como funciona a Rota (Routes),
o que está acontecendo realmente para que a minha pagina apareça.

# Minha maneira correta

Depois de apanhar varias e varias vezes, passar por 2 processos de
comunicação [SERVER -> APP (WSGI-Python, Rack-Ruby)], procurar por MVC,
por REST, CRUD, Banco de Dados, Templates, Settings e etc.
Creio que a melhor forma de introduzir um iniciante ao mundo do
desenvolvimento web, é usando um miniframework.

Python e Ruby tem famosos miniframeworks.
[Sinatra](http://www.sinatrarb.com/) na comunidade Ruby e
[Flask](http://flask.pocoo.org/) na comunidade Python. Ambos são ótimos
para ensinar. O funcionamento da rota é simples de explicar, assim como
as views/controllers que nesses frameworks são apenas fáceis métodos,
que o iniciante vai saber identificar ali com um minimo esforço o que
está acontecendo. Não tem um padrão como o MVC a seguir (uma pilha de
metodos vai fazer o que ele quer). Não precisa configurar nada em nenhum
arquivo adicional (como settings ou configs). Para a simples aplicação
que ele quer fazer para estudo, vai ser de ótima ajuda.

### Observação:
Se existe alguma coisa que você ache errado ou que faz diferente, cria
um comentario para discutimos.


Esse foi o meu segundo post.
