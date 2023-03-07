import concurrent.futures
import multiprocessing
import requests


# With codewithharry part
def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")
    return name


url = "https://picsum.photos/2000/3000"
# pros = []
# for i in range(5):
#     #   downloadFile(url, i)
#     p = multiprocessing.Process(target=downloadFile, args=[url, i])
#     if __name__ == "__main__": #mustline for strt() and join()
#         p.start()
#     pros.append(p)

# for p in pros:
#     if __name__ == "__main__":
#         p.join()

# Using concurrent.futures

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(6)]
    l2 = [i for i in range(6)]
    if __name__ == "__main__":  # must to write Understand from below simple code of Learned from johan godinho
        results = executor.map(downloadFile, l1, l2)# one element from l1 and one from l2 will go to downloadFile() and run
        for r in results:
            print(r)

# Learned from johan godinho
# import time
# import multiprocessing

# def sleep_for_a_bit(seconds):
#     print(f"Sleeping {seconds} second(s)")
#     time.sleep(seconds)
#     print("Done sleping")

# # sleep_for_a_bit(1)
# # sleep_for_a_bit(1)

# p1 = multiprocessing.Process(target=sleep_for_a_bit,args=[1])
# p2 = multiprocessing.Process(target=sleep_for_a_bit,args=[1])

# # print(__name__)

# if __name__ == '__main__':
#     p1.start()
#     p2.start()
#     p1.join()
#     p1.join()

# finish = time.perf_counter()
# print("finished running after seconds: ",finish)
