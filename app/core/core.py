import asyncio
import logging
import threading
import time
from typing import Union
from app.core.task_generator import TASK_GENERATOR


class Core:
    def __init__(self):
        self.is_running = False
        self.should_exit = False
        self.synthensize_task_event_loop = asyncio.new_event_loop()
        self.synthensize_task_thread: Union[threading.Thread, None] = None
        self.config_logging()
        
    def config_logging(self):
        # Configure logging
        logging.basicConfig(
            filename='app.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Add a stream handler to also print to console
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logging.getLogger().addHandler(console_handler)
        
    def synthensize_task_loop(self):
        logging.info(f"Synthensize task loop starting")
        while True:
            time.sleep(1)
            try:
                SYNTHETIC_TASK_TIMEOUT = 60 * 15 # 15 minutes
                self.synthensize_task_event_loop.run_until_complete(
                    asyncio.wait_for(
                        TASK_GENERATOR.generate_task(),
                        timeout=SYNTHETIC_TASK_TIMEOUT
                    )
                )
            except Exception as e:
                logging.error(f"Error during synthensize task: {str(e)}")
            if self.should_exit:
                break
    
    def run_background_threads(self):
        if not self.is_running:
            logging.info("Starting core loop in background thread")
            self.is_running = True
            self.should_exit = False
            self.synthensize_task_thread = threading.Thread(
                target=self.synthensize_task_loop, 
                daemon=True,
            )
            self.synthensize_task_thread.start()

    def stop_background_threads(self):
        if self.is_running:
            logging.info("Stopping core loop in background thread")
            self.is_running = False
            self.should_exit = True
            self.synthensize_task_thread.join()
    
    def __enter__(self):
        self.run_background_threads()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.stop_background_threads()


def core_loop():
    core = Core()
    core.run_background_threads()
