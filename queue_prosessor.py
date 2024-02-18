import queue
import time
import random

def generate_request(process_queue):
    request_id = random.randint(1, 10000)
    process_queue.put(request_id)
    print(f"The request {request_id} was added to the queue.")

def process_request(process_queue):
    if not process_queue.empty():
        request_id = process_queue.get()
        print(f"The request {request_id} is processing...")
        time.sleep(1)
        print(f"The request {request_id} was processed successfully.")
    else:
        print("The queue is empty. There are no requests to process.")

def main():
    process_queue = queue.Queue()

    while True:
        generate_request(process_queue) 
        process_request(process_queue) 

        user_input = input("Do you want to continue (y/n)? ")
        if user_input.lower() != 'y':
            print("The process was ended")
            break

if __name__ == "__main__":
    main()
