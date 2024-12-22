<h1 align="center">Inventory Manager</h1>

<div align="center">
<img src="https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/designer/banner.jpg" alt="Banner Inventory Manager">
</div>
</br>
</br>

<h2 align="center">Gerencie Seu Estoque de Forma Prática e Eficiente</h2>
<p>
O <strong>Inventory Manager</strong> é um aplicativo inovador voltado para o gerenciamento de inventários de forma intuitiva, ideal para atender tanto pequenas empresas quanto usuários individuais. A plataforma foi desenvolvida com uma interface simplificada e recursos robustos para facilitar o acompanhamento do estoque, garantindo praticidade na inclusão, edição e exclusão de itens.
</p>

<h2>Download da Aplicação</h2>
<a href="https://github.com/SidneyTeodoroJr/InventoryManager/raw/main/InventoryManager/build%20platforms/InventoryManager.apk" target="_blank" download>Android</a>
</br>

<a href="https://github.com/SidneyTeodoroJr/InventoryManager/raw/main/InventoryManager/build%20platforms/InventoryManager%20-%20windows.rar"  target="_blank" download>Windows</a>
</br>

<h2>Tecnologias usada:</h2>

[Python](https://docs.python.org/3/): Linguagem backend para integração perfeita com Flet e SQLite, possibilitando scripts eficientes.<br/>
﻿[Flet](https://flet.dev/docs/): Biblioteca para criação de interfaces gráficas com Python, otimizando a experiência mobile e desktop.<br/>
[SQLite](https://flet.dev/docs/): Banco de dados local leve e rápido, ideal para armazenamento offline direto no dispositivo.<br/>

<h2>Estrutura do Projeto</h2>

<p>
O projeto está dividido em vários scripts para melhor organização e modularidade.
<p/>

1. [main.py](https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/main.py): Arquivo principal que inicializa o aplicativo e define a interface gráfica utilizando Flet. 
2. [db_utils.py](https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/modules/db_utils.py): Contém as funções responsáveis pela interação com o banco de dados SQLite.
3. [ui_components.py](https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/modules/ui_components.py): Responsável pela criação de componentes visuais reutilizáveis e modais de diálogo.

<h2>Instruções de Execução</h2>

1. Instale as dependências necessárias usando:
    ```shell
    pip install -r InventoryManager\requirements.txt
2. Execute o aplicativo Streamlit com o comando streamlit:
   ```shell
   flet -r InventoryManager
3. Acesse a aplicação na janela padrão do seu sistema.

<h2>1. Funcionalidades do Inventory Manager</h2>

<p>
O aplicativo Inventory Manager conta com uma variedade de recursos que o tornam útil e fácil de usar. Esses recursos são especialmente voltados para permitir que o usuário tenha controle sobre cada item cadastrado, incluindo a visualização detalhada de informações e ações de edição e exclusão em tempo real.
</p>

<h3>Cadastro de Itens</h3>

<p>
Permite que os usuários adicionem itens ao inventário com facilidade, registrando nome,  descrição e data de inclusão.
</p>

<h3>Busca e Filtro de Itens</h3>

<p>
Conta com uma função de busca eficiente que permite localizar itens rapidamente, filtrando pelo nome ou descrição.
</p>

<div align="center">
<img width="200" src="https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/designer/print-1.jpeg" alt="Banner Inventory Manager">
</div>

<h3>Edição de Itens em Tempo Real</h3>

<p>
A funcionalidade permite editar informações de itens em tempo real, com a atualização refletida imediatamente na lista.
</p>

<h3>Exclusão de Itens</h3>

<p>
Possui opções para excluir itens individualmente ou em massa, facilitando a reorganização do inventário.]
</p>

<div align="center">
<img width="200" src="https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/designer/print-4.jpeg" alt="Banner Inventory Manager">
</div>

<h3>Modais para Visualização e Confirmação</h3>

<p>
Modais interativos permitem visualizar detalhes dos itens e confirmar exclusões, prevenindo erros acidentais.
</p>

<div align="center">
<img width="200" src="https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/designer/print-3.jpeg" alt="Banner Inventory Manager">
</div>

<h2>3. Diferenciais do Inventory Manager</h2>

<p>O aplicativo apresenta diferenciais como interface intuitiva, suporte para uso em dispositivos móveis e desktop, modularidade e rapidez no acesso offline.</p>

<h2>4. Como Usar o Inventory Manager</h2>

<h3>Adicionando um Novo Item</h3>

<p>Basta clicar no botão de adição, preencher as informações e confirmar para adicionar o item ao inventário.</p>

<h3>Buscando Itens no Inventário</h3>

<p>
Use o campo de busca para localizar itens rapidamente pelo nome ou descrição.
</p>

<h3>Editando Informações do Item</h3>

<p>
Clique no ícone de edição ao lado do item para abrir o modal de edição e atualizar as informações.
</p>

<h3>Excluindo Itens</h3>

<p>
Exclusão individual ou em massa, com confirmação para evitar remoções acidentais.
</p>

<h3>Visualizando Detalhes do Item</h3>

<p>
Visualize informações detalhadas ao clicar no item, com detalhes como nome, descrição e data de inclusão.
</p>

<h2>5. Casos de Uso e Benefícios</h2>

<p>
O Inventory Manager é útil para:
</p>
    <ul>
        <li>Gestão de estoque em lojas de roupas.</li>
        <li>Controle de equipamentos para manutenção e aluguel.</li>
        <li>Organização de produtos domésticos.</li>
        <li>Monitoramento de suprimentos para escritórios.</li>
    </ul>

<h2>6. Expansibilidade e Futuras Atualizações</h2>

<p>
Futuramente, o Inventory Manager poderá incluir:
</p>
    <ul>
        <li>Categorias e etiquetas para organização avançada.</li>
        <li>Relatórios de inventário e análises.</li>
        <li>Exportação/importação para formatos como PDF e Excel.</li>
        <li>Sincronização com a nuvem para backup e acesso em múltiplos dispositivos.</li>
    </ul>

<p>
Com todos esses recursos e diferenciais, o <strong>Inventory Manager</strong> se destaca como uma solução eficiente e prática para gerenciar inventários de diferentes tamanhos e propósitos. Seu design intuitivo e foco na simplicidade garantem que qualquer usuário consiga aproveitar ao máximo suas funcionalidades.
</p>

<div align="center">
<img width="200" src="https://github.com/SidneyTeodoroJr/InventoryManager/blob/main/InventoryManager/designer/print-2.jpeg" alt="Banner Inventory Manager">
</div>


## Contribuições
</br>

<p>
Contribuições são bem-vindas! Se quiser melhorar o projeto, adicionar novas funcionalidades ou corrigir problemas, fique à vontade.
</p>
<hr>
</br>

<div align="center">
<a href="https://sidney-personal-portifolio.netlify.app/"><img src="https://img.shields.io/badge/-Portifolio-%230077B5?style=for-the-badge&logo=portifolio&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
<a href="https://www.instagram.com/sidneyteodoroaraujo" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/sidey-teodoro-a-jr/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
</div>
