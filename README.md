# Diagrama

![Diagrama](stop-start.png)

# Requisitos

- Criar os triggers (agendamentos: start e stop) no Amazon EventBridge com a [Pattern START](event_start.txt) e a [Pattern STOP](event_stop.txt)

- Incluir na Role da função a policy AmazonEC2FullAccess ou uma customizada

- Configurar as Variáveis com os IDs das instâncias. Ex: [Environment_variables](Environment_variables.txt)