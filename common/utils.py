
import hashlib

def stable_hash_to_float(s: str, lo: float=0.0, hi: float=1.0) -> float:
    h = hashlib.sha256(s.encode('utf-8')).hexdigest()
    n = int(h[:16], 16) / (16**16 - 1)
    return lo + (hi - lo) * n

def clamp(x, lo, hi):
    return max(lo, min(hi, x))
