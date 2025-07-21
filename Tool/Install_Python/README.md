# Python 설치 가이드 (버전 3.11.9 기준)

---

# Windows에서 Python 설치하기

## 1. Python 다운로드

1. 공식 다운로드 페이지 접속:  
   [https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/)

2. 페이지 하단으로 스크롤하여 본인 PC에 맞는 설치파일(`Windows installer`)을 클릭하여 다운로드  
   - 예: `Windows installer (64-bit)`


## 2. Python 설치

1. 다운로드한 `.exe` 설치파일 실행
2. 설치 첫 화면에서 반드시 아래 설정 확인:
   - **"Add python.exe to PATH" 체크**  
   - 이후 **"Install Now" 클릭**하여 설치 진행

3. 설치 완료 후 **"Disable path length limit"** 버튼 클릭 (권장)  
   - Windows의 기본 파일 경로 길이 제한(260자)을 해제하여 오류 방지
   - 환경에 따라 해당 항목이 표시되지 않을 수도 있음 (무시해도 무방)

## 3. 설치 확인

### 방법 1. 시작 메뉴 검색

- Windows 키 → `python` 입력 → `Python 3.11` 실행 가능 여부 확인

### 방법 2. 명령 프롬프트 확인
1. Windows 키 → `cmd` 입력 → 명령 프롬프트 실행

2. 아래 명령어 입력:

```bash
python -V
````

또는

```bash
python --version
```

출력 예시:

```
Python 3.11.9
```

---

# macOS에서 Python 설치하기

> Homebrew가 사전 설치되어 있어야 합니다. 설치되지 않은 경우 [https://brew.sh](https://brew.sh) 참고

## 1. pyenv 설치

```bash
brew install pyenv
```

## 2. pyenv 환경 설정

아래 명령어를 입력하여 `.zshrc`에 설정을 추가합니다:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"
```

## 3. pyenv 설치 확인

```bash
pyenv -v
```

설치된 버전이 출력되면 성공입니다.

---

## 4. Python 설치

아래 명령어로 Python 3.11.9 설치:

```bash
pyenv install 3.11.9
pyenv global 3.11.9
pyenv rehash
```

## 5. 설치 확인

```bash
python -V
```

출력 예시:

```
Python 3.11.9
```
---

## \[주의] 설치 후에도 Python 2.x가 출력된다면?

### 1. `.zprofile` 설정

```bash
code ~/.zprofile
eval "$(pyenv init --path)"
source ~/.zprofile
```

### 2. `.zshrc` 설정

```bash
code ~/.zshrc
eval "$(pyenv init -)"
source ~/.zshrc
```

이후 다시 확인:

```bash
python -V
```

---

## 추가 권장 사항 (macOS 전용)

정상적인 빌드 환경을 위해 다음 패키지 설치를 권장합니다:

```bash
brew install openssl readline sqlite3 xz zlib tcl-tk
```

이 패키지들은 pyenv가 Python을 컴파일할 때 필요한 환경 구성 요소들입니다.


참고: [https://github.com/pyenv/pyenv/wiki#suggested-build-environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

