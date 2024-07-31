import asyncio
import signal

from tasks import task_manager


def handle_exit(loop):
    print("Exiting game...")
    loop.stop()


def main():
    loop = asyncio.get_event_loop()

    try:
        # Run the task manager coroutine until it completes
        loop.run_until_complete(task_manager())
    except KeyboardInterrupt:
        print("Received exit signal, stopping loop...")
        handle_exit(loop)
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        # Close the event loop
        loop.close()


if __name__ == "__main__":
    main()
