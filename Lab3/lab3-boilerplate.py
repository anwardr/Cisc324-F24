import threading
import time
import random

# Constants for the number of writers, editors, and available review slots
NUM_WRITERS = 5  # Number of writers to simulate
NUM_EDITORS = 2  # Number of editors to simulate
NUM_SLOTS = 3  # Maximum simultaneous reviews

# Semaphore to manage available review slots
review_slots = threading.Semaphore(NUM_SLOTS)

# Lock to ensure one editor reviews an article at a time
editor_lock = threading.Lock()

# Lock to prevent overlapping print output
print_lock = threading.Lock()

# Shared variables to track the submission and review process
articles_submitted = 0  # Number of articles submitted
TOTAL_ARTICLES = NUM_WRITERS  # Total articles expected

# Event to signal that all articles are reviewed
stop_editors = threading.Event()


def writer_task(writer_id):
    """Simulates a writer drafting and submitting an article."""
    with print_lock:
        print(f"Writer {writer_id} is drafting an article.")

    # Simulate drafting time
    time.sleep(random.uniform(1, 2))

    with print_lock:  # console is a shared resource, so we need to lock it
        print(f"Writer {writer_id} is waiting for a review slot.")

    # TODO 1: Acquire the review slot before submission

    with print_lock:  # console is a shared resource, so we need to lock it
        print(f"Writer {writer_id} has submitted an article for review.")

    # TODO 2: Safely update the shared variable `articles_submitted` tracking the number of submitted articles

    # TODO 3: Release the review slot after submission


def editor_task(editor_id):
    """Simulates an editor reviewing articles."""
    while not stop_editors.is_set():
        # Simulate the time before checking for an article
        time.sleep(random.uniform(0.5, 1.5))

        with print_lock:  # console is a shared resource, so we need to lock it
            print(f"Editor {editor_id} is checking for an article to review.")

        # TODO 4: Acquire the editor lock with a timeout to avoid deadlock

        try:
            # TODO 5: Check if there are articles to review
            # TODO 6: consider preventing possible deadlock here by using a timeout (search for it in the Python documentation) REM<OVE this one
            with print_lock:  # console is a shared resource, so we need to lock it
                print(f"Editor {editor_id} is reviewing an article.")
            time.sleep(random.uniform(1, 3))  # Simulate review time

            with print_lock:  # console is a shared resource, so we need to lock it
                print(f"Editor {editor_id} has finished reviewing an article.")

            # TODO 7: Safely decrement the number of submitted articles

            # TODO 8: Stop editors if all articles are reviewed

        finally:
            # TODO 9: Ensure the editor lock is released
            pass  # TODO 10: Remove this line after adding the code

    with print_lock:
        print(f"Editor {editor_id} is stopping as all reviews are complete.")


def main():
    """Main function to initialize the simulation."""
    # TODO 11: Start writer threads
    writer_threads = []
    for i in range(NUM_WRITERS):
        t = threading.Thread(target=writer_task, args=(i,))
        writer_threads.append(t)
        t.start()

    # TODO 12: Start editor threads
    editor_threads = []
    for i in range(NUM_EDITORS):
        t = threading.Thread(target=editor_task, args=(i,))
        editor_threads.append(t)
        t.start()

    # TODO 13: Ensure all writer threads finish
    for t in writer_threads:
        t.join()

    # TODO 14: Ensure all editor threads finish
    for t in editor_threads:
        t.join()

    print("All articles have been submitted and reviewed.")


if __name__ == "__main__":
    main()
