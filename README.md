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
```

## Exemplo

Este repositório contém um exemplo mínimo de SMA (Sistema Multiagente) usando o PADE, com:

- 1 agente central (`CentralAgent`) que recebe leituras de temperatura e calcula a média corrente.
- 4 agentes sensores (`SensorAgent`) que periodicamente geram e enviam uma temperatura aleatória.

Arquivos principais:

- `main.py`: cria os AIDs, instancia o agente central na porta 2000 e quatro sensores nas portas 2001–2004, e inicia o loop.
- `central_agent.py`: implementa o agente central; sobrescreve `react(self, message)` para processar mensagens `ACLMessage.INFORM`, guarda a última leitura por sensor e imprime a média.
- `sensor_agent.py`: define o agente sensor e anexa o comportamento temporizado que envia a leitura.
- `temperature_sensor_behavior.py`: comportamento `TimedBehaviour` que, a cada N segundos, simula uma temperatura e envia uma mensagem INFORM ao central.
- `run_pade_web.py`: script auxiliar para subir a interface web do PADE numa porta customizada (sem alterar a biblioteca instalada).

Fluxo de mensagens:

1. Cada `SensorAgent` possui um `TemperatureSensorBehavior` que dispara a cada 10 segundos.
2. Ao disparar, o comportamento cria um `ACLMessage(ACLMessage.INFORM)`, adiciona o receptor (`central@localhost:2000`), define o conteúdo com a temperatura e envia via `self.agent.send(msg)`.
3. O `CentralAgent.react` recebe a mensagem, extrai o conteúdo, atualiza o dicionário de leituras por sensor e imprime a leitura e a média atual.

Portas utilizadas:

- Agente central: 2000
- Sensores: 2001, 2002, 2003, 2004
- Painel Web do PADE: por padrão 5000 (no CLI). Para evitar conflito, utilize o script `run_pade_web.py` e escolha outra porta (ex.: 5001).


## Como Executar
1. Inicializar os agentes
```bash
pade start-runtime main.py --port 2000 --no_pade_ams --no_pade_sniffer
``` 

2. Inicializar o painel web fora da porta 5000
```bash
PADE_WEB_HOST=127.0.0.1 PADE_WEB_PORT=5001 python run_pade_web.py
```

Você poderá acessar a interface em:

- http://localhost:5001 (ou http://127.0.0.1:5001)

Observações importantes:

- O comando `start-runtime` do PADE (nessa versão) sobe o painel embutido sempre na porta 5000. Se a 5000 estiver em uso, prefira o `run_pade_web.py` para escolher outra porta.
- O flag correto para habilitar/desabilitar recursos no CLI usa sublinhado: `--pade_web`, `--no_pade_ams`, `--no_pade_sniffer`.

Resolução de problemas:

- Porta 5000 ocupada: libere a porta ou use o `run_pade_web.py` com `PADE_WEB_PORT` diferente.
- Página não abre no navegador: tente janela anônima, troque para http://127.0.0.1:PORTA, ou valide com `curl -I http://localhost:PORTA`.
- Sem logs do agente central: confirme que `CentralAgent.react` está sendo chamado (impressões no terminal) e que os sensores seguem enviando (o `TimedBehaviour` chama `super().on_time()` no final).