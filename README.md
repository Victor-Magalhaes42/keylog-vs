# 🛡️ Simulador de Keylogger Ético – Pentest Controlado

> **⚠️ PARA USO ÉTICO APENAS – CONSENTIMENTO REQUERIDO**  
> Este projeto é destinado exclusivamente para **testes de segurança autorizados**.  
> NUNCA utilize sem o **consentimento explícito** da organização-alvo.

---

## 📋 Descrição

Este é um simulador de keylogger desenvolvido com Python para fins **educacionais e de avaliação** durante testes de penetração controlados.  
Ele registra pressionamentos de teclas localmente em um arquivo de log, com opções de codificação e mecanismos de encerramento seguro.

---

## 🚀 Funcionalidades

- 🔑 Captura de teclas com **timestamp**
- 💾 Registro em `keylog.txt` (codificado em Base64 opcionalmente)
- ⏱️ Autoencerramento após tempo limite configurável (default: 5 minutos)
- 🛑 Parada remota ao detectar o arquivo `stop.flag`
- ⚠️ Aviso legal obrigatório no início da execução
- 🔐 Opção de simular técnicas de evasão (Base64, XOR, etc.)

---

## 🧪 Requisitos

- Python 3.x
- Bibliotecas:
  ```bash
  pip install pynput

---

## ⚙️ Como Usar
- Clone ou baixe este repositório.

- Execute o script:

  ```bash
  python keylogger.py

Pressione Enter após o aviso legal para iniciar.

- Para parar o keylogger:

Pressione Ctrl+C

OU crie um arquivo chamado stop.flag no mesmo diretório

OU aguarde o tempo limite ser atingido

---

## 🔓 Exemplo de Log
  ```bash
MjAyNS0wNC0wOCAxMzowMzowOCAtIGg=
MjAyNS0wNC0wOCAxMzowMzowOSAtIGVsbG8=
  ```

- O conteúdo está codificado em Base64 por padrão.

---

## 🧹 Remoção
- Pressione Ctrl+C ou crie stop.flag.

- Exclua os seguintes arquivos:

- keylog.txt

- stop.flag

- keylogger.py

---

## 🛡️ Mitigações Recomendadas
- Para prevenir ataques com keyloggers:

- Utilize soluções EDR com detecção comportamental

- Restrinja execução de scripts desconhecidos via GPO

- Monitore processos que acessam o teclado (pynput, keyboard, etc.)

- Aplique whitelisting de software

- Ative logging com ferramentas como Sysmon ou Auditd

---

## 🧠 Detecção por Ferramentas de Segurança
- Ferramenta	Possível Detecção
- Microsoft Defender	Heurísticas e comportamento de script
- CrowdStrike Falcon	Monitoramento de processos
- Sysmon + SIEM	Acesso ao teclado e escrita em arquivos
- ESET, Kaspersky	Deteção de biblioteca pynput

---

## 📚 Licença
- Distribuído apenas para fins educacionais e de auditoria ética.
- NÃO UTILIZE PARA ATIVIDADES MALICIOSAS. NÃO ME RESPONSABILIZAREI POR QUAISQUER USOS INDEVIDOS E ILÍCITOS.

