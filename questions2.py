from typing import List
import math

class JaeheePython:
## 함수를 생성 예시 ##
## def test(input:int) -> bool:
##
## 위의 생성된 test 함수에서 def 는 함수를 정의하는 파이썬의 명령어입니다.
## test는 사용자가 임의로 변경할수 있으며 함수의 이름입니다.
## 괄호 안에 값은 함수가 값을 받을때 어떤값을 어떤 형태로 받는지에 대한 정의를 하는데,
## () 빈 괄호로 둘경우에는 아무런 값도 받지 않는다는 함수를 의미하고, 위와 같은 경우에는
## 정수 형태의 input이라는 이름을 가진 값을 받는 함수라는 의미 입니다.
## 마지막으로 "-> bool" 이라고 되어있는 부분은 bool 은 boolean의 줄임말로 True 혹은 False의 값을 반환한다는 의미입니다.

## 정리해서 말씀드리면 위의 함수는 test라는 이름을 가진 함수이고 input이라는 int 형태의 값을 받아서 True 나 False 값을 반환하는 함수입니다.

## def test(input) -> bool: 
## 위와 같은 형태이지만 다른 작성방식으로 input

#1. isEven(number), isOdd(number), isPrime(number) 짝수인지 홀수인지 소수인지 확인해서 True/False 로 반환하는 메소드 3개를 만들어 주세요.
    def isEven(self, number):
        if number % 2 == 0:
            print(True)
        else:
            print(False)
            
    def isOdd(self, number):
        if number % 2 == 1:
            print(True)
        else:
            print(False) 
    
    #def isPrime(self, number):
        
        


#2. 4개의 값을 받는 거리를 계산하고 두 포인트간에 거리를 반환하는 isDistance(x1, y1, x2, y2) 함수를 만들어주세요.

    def isDistance(self, x1, y1, x2, y2):
        a = (x2 - x1)**2 + (y2 - y1)**2
        print("Distance: ", math.sqrt(a))

#3. 문자열에서 정수 갯수 찾기
# 문자를 파라미터 값으로 받고 문자열에서 숫자가 나오는 횟수를 더한 값을 리스트에 입력해서 반환하는 함수를 만들어주세요.

#프로그램을 실행했을 때의 출력 예제는 아래와 같습니다.

#예제:
#a3sber226 <-- 입력
#[0,0,2,1,0,0,1,0,0,0] <-- 결과
#
# 설명: 위의 입력값에서 2 두번, 3 한번, 6 한번이 나왔기 때문에,
# 리스트에서 2에 대항하는 부분이 2, 3에 해당하는 부분이 1, 6에 해당하는 부분이 1 입니다.

    def findInteger(self, numberandstring):
        foundnumberList = [0,0,0,0,0,0,0,0,0,0]
        for i in numberandstring[:]:
            if i.isdigit():
                foundnumberList[int(i)] += 1         
            else:
                continue
        
        print(foundnumberList)
            
#4. 
# 리스트에 두 값을 더해서 타겟과 일치하는 값을 찾고 리스트에 인덱스를 리턴하는 프로그램을 작성해 주세요.
# 정답이 여러개가 있어도 발견한 첫번째 정답만 하고 리스트 내에 같은 위치에 있는 값을 두번 사용하면 안됩니다.
# ** 리스트내에서 타겟 값을 구할수 없으면 [] 빈 리스트를 반납해주세요.
# try except (jump2python 책 194페이지 참고)문 을 이용하여서 target 에 int 외에 값이 들어오는 경우를 처리해주세요.

#프로그램을 실행했을 때의 출력 예제는 아래와 같습니다.

#예제1 :
#nums = [2,7,11,15], target = 9 <-- 입력
#[0,1] <-- 결과

#설명:
#주어진 리스트가 [2,7,11,15] 이고 리스트 내에서 두개의 값을 더해서
#찾아야하는 값이 9 이기 때문에 리스트의 0번째 인덱스 숫자인 2와 1번째 인덱스 숫자인 7을
#더하면 9가 완성되기 때문에 정답은 [0,1] 입니다.



#예제2 :
#nums = [3,2,4], target = 6 <-- 입력
#[0,2] <-- 결과

#설명:
#주어진 리스트가 [3,2,4] 이고 리스트 내에서 두개의 값을 대헛
#찾아야하는 값이 6 이기 때문에 리스트의 1번째 인덱스 숫자인 2와 2번째 숫자인 4를
#더하면 6이 완성되기 때문에 정답은 [1,2] 입니다.

#예제3 :
#nums = [1,2,3,4], target = 'a' <--입력
#잘못된 target 값을 가지고 있습니다. <-- 결과
# try except (jump2python 책 194페이지 참고)문 을 이용하여서 target 에 int 외에 값이 들어오는 경우를 처리해주세요.

    def findTargetNumberIndex(self):     
            try:
                numbers = input("공백을 구분자로 하여 대상 리스트를 입력하세요. : ").split()
                target = int(input("타겟 숫자를 입력하세요. : "))
                targetIndex = []    
                for i in numbers[:]:
                    leftNumbers = numbers.copy() #그냥 같다고 하면 같은 리스트로 서로 영향 받음
                    del leftNumbers[leftNumbers.index(i)]
                    
                    if len(targetIndex) == 0: 
                        for j in leftNumbers[:]:
                            if int(i) + int(j) == target:
                                targetIndex.append(numbers.index(i))
                                targetIndex.append(numbers.index(j))
                                print(targetIndex)
                                break
                            else:
                                continue
                    else:
                        break
            except :
                print("잘못된 target 값을 가지고 있습니다.")

#5. 가장 긴 부분 문자열 찾기
#반복되는 글자가 없는 문장내 가장 긴 문자열을 찾고 문자열의 길이를 리턴해주세요.

#프로그램을 실행했을 때의 출력 예제는 아래와 같습니다.

#예제1 :
#input = "abcabcbb" <-- 입력
#3 <-- 결과

#설명:
#abc후에 a가 다시 반복되기 때문에 

#예제2 :
#input = "bbbbb" <-- 입력
#1 <-- 결과

#예제3:
#input = "pwwkew" <-- 입력
#3 <-- 결과

#설명:
#가장 긴 substring 은 wke 로 결과는 3 입니다.

#예제4 :
#input = "" <--입력
#0 <-- 결과




#6. 회문 찾기
#숫자가 회문인지 아닌지를 판단해서 리턴해주세요.

#예제 1:
#input = 121 <--입력
#true <-- 결과

#예제 2:
#input = -101 <-- 입력
#false <-- 결과

#예제 3:
#input = 10 <-- 입력
#false <-- 결과

    def isPalindrome(self, number):
        originalNumber = list(str(number))
        reversedNumber = originalNumber[::-1]
        
        if originalNumber == reversedNumber:
            print("true")
        else:
            print("false")


############################################ 테스트 영역 ############################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################