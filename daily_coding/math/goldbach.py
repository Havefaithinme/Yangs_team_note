# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

# 이 추측은 아직도 해결되지 않은 문제이다.

# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

def is_prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
primes = []
while True:
    even = int(input())
    if even == 0:
        break
    else:
        # 짝수를 반으로 나눈다. half 
        # 3이상의 홀수를 차례대로 half 전까지 검사한다. 해당 숫자가 기존의 소수 list에 있는지 확인하고 없다면 소수인지 확인 후 소수라면 소수 set에 넣어두고 아니면 다음걸로 
        # 원래 숫자에서 해당 숫자를 뺀 숫자가 기존 소수 list에 있는지 확인하고 없다면 소수인지 확인 한 후 소수라면 소수 set에 넣어두고 값을 리턴한다. 
        half = int(even / 2)
        i = 3
        while i <= half:
          if i in primes:
              counterpart = int(even - i)
              if counterpart in primes:
                  print(f"{even} = {i} + {counterpart}")
                  break
              else:
                  if is_prime(counterpart):
                        print(f"{even} = {i} + {counterpart}")
                        break
                  else:
                      i += 2
                      continue 
          else:
              if is_prime(i):
                primes.append(i)
                counterpart = int(even-i)
                if is_prime(counterpart):
                    primes.append(counterpart)
                    print(f"{even} = {i} + {counterpart}")
                    break
                else:
                    i += 2
                    continue  
                
        