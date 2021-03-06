# samsung-careers-subjects-easy-fillin

## 어디에 쓰이는 코드인가?
제가 삼성전자 인턴으로 지원하려고 했는데 지원 사이트에서 대학교에서 수강했던 교과목을 하나하나 입력해야 한다는 것을 알게 되었다. 폼에 수강했던 과목들을 하나하나 입력해야할 생각을 하니 정신이 혼미해져서 이 코드를 작성하였다.

## 사용방법
### 필요사항
- python (필자는 3.8.2로 실행함)
- selenium (pip install selenium으로 설치 가능)
- Chrome
- Chromedriver (Chrome 버전에 맞는 chromedriver를 사용해야함)

### 정보입력
0. 삼성채용 사이트 등록
삼성채용 사이트에 가입을 한 뒤, 인턴십 지원서를 작성하기 시작한다. 교과목 입력 전까지의 단계가 완료되어 있어야 한다.
1. 삼성채용 사이트 계정정보 입력
settings.py에서 삼성채용 사이트의 계정 이메일, 패스워드를 기입한다.
2. data.csv 파일 작성
data.csv 파일을 작성한다. 위의 제목(과정, 전공명, ... 등)의 이름들은 유지되어야 한다. 순서는 바뀌어도 상관이 없다.
예시를 참고하기 바란다.
3. main.py 실행
main.py를 실행하면 자동으로 교과목 기입이 시작된다.

### 정보제거
현재까지 넣은 정보를 제거하고 싶으면 파이썬 쉘에 clear_subjects(driver)를 입력함으로써 모든 과목들이 제거가 가능하다.

## 데모영상
![demo.gif](https://github.com/SPICYJO/samsung-careers-subjects-easy-fillin/blob/master/screenshots/demo.gif?raw=true)
위 gif는 자동으로 실행되는 모습이다.

## 버그정보
프로그램 내에서 웹페이지가 다 로드되지 않은 상태에서 클릭을 수행하려고 할 때, 예외가 발생하는 버그가 있다.
이를 막기 위해 time.sleep()을 통해 강제로 기다리도록 코드를 작성해놓았다. 서버에 접속자가 많아 느려지는 등의 상황에서는
func.py 내부의 time.sleep()의 인자값을 바꾸는 방법을 시도해보기 바란다.
