import threading
import time

def worker_thread(event):
    print("Worker thread started")
    time.sleep(4)  # Simulate a task
    print("Worker thread finished")
    event.set()  # Signal that the worker thread has terminated

def main_thread():
    print("Main thread started")

    # Create an event to serve as a termination port
    termination_port = threading.Event()

    # Create a worker thread
    worker = threading.Thread(target=worker_thread, args=(termination_port,))

    # Start the worker thread
    worker.start()

    # Wait for the worker thread to terminate
    print("Main thread waiting for worker thread to terminate...")
    termination_port.wait()
    print("Worker thread terminated")

    print("Main thread finished")

if __name__ == "__main__":
    main_thread()