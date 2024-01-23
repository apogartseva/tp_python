from multiprocessing import Process
import time


def calcul_long():
    n = int(1E7)
    while n > 0:
        n -= 1


def test_multiprocessing():
    processes = []
    num_processes = 4  # Choisir le nombre de processus souhaité

    for _ in range(num_processes):
        process = Process(target=calcul_long)
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":

    start_time = time.time()
    test_multiprocessing()
    end_time = time.time()
    print(f"temps exécution avec multiprocessing : {end_time - start_time} secondes")
