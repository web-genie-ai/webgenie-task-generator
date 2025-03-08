import binascii
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from substrateinterface import Keypair

from app.services.task import (
    get_seed, 
    get_task,
)


router = APIRouter()


def verify_signature(request: Request):
    hotkey = request.headers.get("Hotkey")
    signature_hex = request.headers.get("Signature")    
    if not hotkey or not signature_hex:
        return False

    try:  
        signature = binascii.unhexlify(signature_hex)
        data_to_verify = b"I am the owner of the wallet"
        keypair = Keypair(ss58_address=hotkey)
        is_valid = keypair.verify(data_to_verify, signature)
        if not is_valid:
            return False
        allowed_hotkeys = [
            "5FFApaS75bv5pJHfAp2FVLBj9ZaXuFDjEypsaBNc1wCfe52v",
            "5F4tQyWrhfGVcNhoqeiNsR6KjD4wMZ2kfhLj4oHYuyHbZAc3",
            "5HEo565WAy4Dbq3Sv271SAi7syBSofyfhhwRNjFNSM2gP9M2",
            "5F2CsUDVbRbVMXTh9fAzF9GacjVX7UapvRxidrxe7z8BYckQ",
        ]
        return hotkey in allowed_hotkeys
    except Exception as e:
        return False


@router.get("/seed")
async def seed_task(session:int, task_number:int):
    seed, task_id_seed = get_seed(session, task_number)
    return {
        "seed": seed,
        "task_id_seed": task_id_seed,
    }


@router.get("/generate")
async def generate_task(session:int, task_number:int, request: Request):
    if not verify_signature(request):
        return ""
    
    html = get_task(session, task_number)
    return {
        "html": html,
    }