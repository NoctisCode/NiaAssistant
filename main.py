from src.nia import Nia

def main():
    nia = Nia()  # Inicializa Nia y comienza a escuchar pasivamente

    try:
        while True:  # Mantiene el programa en ejecución
            pass
    except KeyboardInterrupt:
        nia.stop()  # Detiene a Nia al interrumpir el programa
        print("Nia ha sido detenida.")

if __name__ == "__main__":
    main()
