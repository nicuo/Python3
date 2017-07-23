import redis
conn = redis.Redis()
conn.delete('test')

conn.hmset('test', {'count':1, 'name': 'Fester Bestertester'})
conn.hgetall('test')


