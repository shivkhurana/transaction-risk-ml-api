import redis

# Connect to Redis container
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def is_rate_limited(user_id: str) -> bool:
    # Allow max 5 transactions per second per user
    key = f"rate_limit:{user_id}"
    current_count = redis_client.incr(key)
    
    if current_count == 1:
        redis_client.expire(key, 1) # Reset counter every 1 second
        
    return current_count > 5