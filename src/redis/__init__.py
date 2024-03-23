import redis
import json

r = redis.Redis(host='cache', port=6379)

EXPIRATION_TIME = 3600  # 1 hour | 3600 seconds


def get_cache(key, pydantic_model):
    cached = r.get(key)
    if cached:
        if pydantic_model:
            return pydantic_model(**json.loads(cached))
        return json.loads(cached)
    return None


def get_or_set_cache(key, fnc, pydantic_model=None, ttl=EXPIRATION_TIME):
    cached = r.get(key)
    if cached:
        if pydantic_model:
            return pydantic_model(**json.loads(cached))
        return json.loads(cached)
    result = fnc()
    if pydantic_model:
        r.setex(key, ttl, json.dumps(pydantic_model.from_orm(result).dict()))
    else:
        r.setex(key, ttl, json.dumps(result))
    return result
