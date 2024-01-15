import threading
import time


def calcul_long():
    n = int(1E7)
    while n > 0:
        n -= 1

def test_multithreading():
    threads = []
    num_threads = 4  # Choisir le nombre de threads souhaité

    for _ in range(num_threads):
        thread = threading.Thread(target=calcul_long)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":

    start_time = time.time()
    test_multithreading()
    end_time = time.time()

    print(f"temps exécution avec multithreading : {end_time - start_time} secondes")
