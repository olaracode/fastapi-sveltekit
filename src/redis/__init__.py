import redis
import json

r = redis.Redis(host='cache', port=6379)


def get_or_set_cache(key, fnc, pydantic_model):
    cached = r.get(key)
    if cached:
        if pydantic_model:
            return pydantic_model(**json.loads(cached))
        return json.loads(cached)
    result = fnc()
    if pydantic_model:
        r.set(key, json.dumps(pydantic_model.from_orm(result).dict()))
    else:
        r.set(key, json.dumps(result))
    return result
