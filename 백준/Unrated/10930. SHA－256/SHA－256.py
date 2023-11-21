import hashlib

# 암호화할 데이터
data = input()

# SHA-256 해시 객체 생성
hash_object = hashlib.sha256()

# 데이터 업데이트
hash_object.update(data.encode())

# 해시 값 추출
hash_value = hash_object.hexdigest()

# 결과 출력
print(hash_value)