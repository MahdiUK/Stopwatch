import time

print("###Press Enter to start the stopwatch, and then press Enter again to stop it###")
input()
print("Stopwatch started")
start_time = time.time()
input()
print("Stopwatch stopped")
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: {:.2f} seconds".format(elapsed_time))