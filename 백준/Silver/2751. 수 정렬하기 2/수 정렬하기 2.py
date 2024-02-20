def sol():
    nums = [None]*2000001   # -1000000부터 1000000까지의 숫자를 포함할 수 있는 크기의 리스트 생성
    
    n = map(int,open(0))    # open(0)을 사용하여 표준 입력(stdin)에서 데이터 read
    next(n)                 # map 객체의 첫 번째 요소(즉, 첫 줄에 입력된 숫자)를 건너뜀
    
    for i in n:nums[i]=1    # 각 숫자 i에 대해, nums[i] 위치에 1을 할당함으로써 해당 숫자의 존재를 표시
    
    print("\n".join(str(i) for i in range(-1000000,1000001,1) if nums[i]))  # 해당 숫자가 nums 리스트에 존재하는 경우 문자열로 변환하여 리스트에 포함, 이 리스트를 "\n"로 결합해 각 숫자를 새 줄에 출력

sol()