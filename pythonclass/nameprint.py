grade = int(input("학년입력:"))
class_num= int(input("반입력:"))

teachers = {
    (1): {"부담임": "함기훈선생님"},
    (2): {"담임": "권지웅선생님"},
    (3): {"부담임": "김윤지선생님"},
    (4): {"담임":"임진하선생님"}
}
key = class_num
#튜플 ㄴㄴ 튜플은 "," 사용해야함 -> 값을 여러 개 묶을 때 쓰는 자료형이니까 쉼표 ,로 여러 값을 구분

if key in teachers: #키 안에 딕셔너리 안에 있는 값일때
    total = grade + class_num
    # 만약 total % 2 == 0 (즉, 짝수)이면 "담임"이라는 문자열을 role에 저장 아니면 "부담임"을 저장

    role = "담임" if total % 2 == 0 else "부담임"
    print(f"해당 반의 {role} 선생님은: {teachers[key][role]}")
    #ex) teachers(2, 1)["부담임"] => 함기훈선생님
    #f-string는 문자열안에 변수를 넣을 수 있는것 -> ex) print(f"{name}은 {age}살입니다.")
else:
    print("해당 학년/반 정보가 없습니다.")
