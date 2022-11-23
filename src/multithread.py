import threading

class MultiThread(threading.Thread):
    def __init__(self, queue:object, daemon: bool=True, func: object=lambda x: None) -> None:
        super().__init__(daemon=daemon)
        self.daemon = daemon
        self.queue = queue
        self.func = func
        
    def run(self) -> None:
        try:
            self.func()
        except Exception as e:
            print(f"Error in MultiThread.run: {e}")
        self.queue.task_done()