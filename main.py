from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import math
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {
        "is_success": True,
        "official_email": "deesha0067.be23@chitkara.edu.in"
    }

@app.post("/bfhl")
def bfhl(data: dict):
    return {
        "is_success": True,
        "data": data
    }


OFFICIAL_EMAIL = "deesha0067.be23@chitkara.edu.in"


class RequestData(BaseModel):
    fibonacci: Optional[int] = None
    prime: Optional[List[int]] = None
    lcm: Optional[List[int]] = None
    hcf: Optional[List[int]] = None
    AI: Optional[str] = None


def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def calculate_lcm(nums):
    result = nums[0]
    for n in nums[1:]:
        result = abs(result * n) // math.gcd(result, n)
    return result


def calculate_hcf(nums):
    result = nums[0]
    for n in nums[1:]:
        result = math.gcd(result, n)
    return result


@app.get("/health")
def health():
    return {
        "is_success": True,
        "official_email": OFFICIAL_EMAIL
    }


@app.post("/bfhl")
def bfhl(data: RequestData):
    try:
        if data.fibonacci is not None:
            output = fibonacci_series(data.fibonacci)

        elif data.prime is not None:
            output = [x for x in data.prime if is_prime(x)]

        elif data.lcm is not None:
            output = calculate_lcm(data.lcm)

        elif data.hcf is not None:
            output = calculate_hcf(data.hcf)

        elif data.AI is not None:
            output = "AI"

        else:
            raise HTTPException(status_code=400, detail="Invalid input")

        return {
            "is_success": True,
            "official_email": OFFICIAL_EMAIL,
            "data": output
        }

    except:
        raise HTTPException(status_code=400, detail="Error while processing")

