import asyncio
import logging
import random
import threading
import time
from typing import Union
from app.constants import (
    MAX_SYNTHETIC_TASK_SIZE,
)
from app.datasets.huggingface_dataset import HuggingfaceDataset
from app.datasets.synthetic_dataset import SyntheticDataset
class TaskGenerator:
    def __init__(self):
        self.datasets = [
            (SyntheticDataset(has_ground_truth_html=True), 1),
        ]
        self.tasks = []
        
    async def generate_task(self):
        try:
            if len(self.tasks) >= MAX_SYNTHETIC_TASK_SIZE:
                logging.info(f"Task size limit reached, skipping task generation")
                return
            
            logging.info(f"Generating task")
            dataset, _ = random.choices(self.datasets, weights=[weight for _, weight in self.datasets])[0]
            task = await dataset.generate_context()
            self.tasks.append(task)
        except Exception as e:
            logging.error(f"Error generating task: {e}")
    
    def get_task(self):
        if not self.tasks:
            return None
        
        task = self.tasks.pop(0)
        return task


TASK_GENERATOR = TaskGenerator()