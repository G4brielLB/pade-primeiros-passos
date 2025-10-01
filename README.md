# Primeiros Passos com PADE

## Instalação
O PADE foi projetado para rodar com o Python 3.7, portanto, a instalação foi feita dentro de um virtual environment com a versão 3.7.17 do Python, onde foi utilizado o pyenv para a mudança de versão.

1. Criação do ativação do ambiente virtual
```bash
pyenv shell 3.7.17 # Ativar temporariamente o Python 3.17.7 
python -m venv padeenv
source padeenv/bin/activate
```

2. Atualizar pip, setuptools e wheel
```bash
pip install --upgrade pip setuptools wheel
```

3. Instalação via Git
A instalação via pip não está funcionando com o PADE devido a uma dependência que não funciona mais, portanto a instalação deve ser feita via git, apontando para o repositório oficial
```bash
pip install git+https://github.com/grei-ufc/pade.git
````

