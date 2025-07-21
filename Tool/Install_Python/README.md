# Python 설치 가이드 (버전 3.11.9 기준)

---

# Windows에서 Python 설치하기

## 1. Python 다운로드

1. 공식 다운로드 페이지 접속:  
   [https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/)

2. 페이지 하단으로 스크롤하여 본인 PC에 맞는 설치파일(`Windows installer`)을 클릭하여 다운로드  
   - 예: `Windows installer (64-bit)`
<img width="1024" height="383" alt="image" src="https://github.com/user-attachments/assets/e13b0107-619b-495b-85bc-d183e108192a" />


## 2. Python 설치

1. 다운로드한 `.exe` 설치파일 실행
2. 설치 첫 화면에서 반드시 아래 설정 확인:
   - **"Add python.exe to PATH" 체크**  
   - 이후 **"Install Now" 클릭**하여 설치 진행
<img width="983" height="607" alt="image" src="https://github.com/user-attachments/assets/3f4a35ed-ddbe-4462-8995-3e4ea9cf02a2" />
<img width="983" height="607" alt="image" src="https://github.com/user-attachments/assets/c3d3f920-4b91-464a-88aa-bb6e55d041b7" />

3. 설치 완료 후 **"Disable path length limit"** 버튼 클릭 (권장)  
   - Windows의 기본 파일 경로 길이 제한(260자)을 해제하여 오류 방지
   - 환경에 따라 해당 항목이 표시되지 않을 수도 있음 (무시해도 무방)
<img width="666" height="410" alt="image" src="https://github.com/user-attachments/assets/8dfc6848-1c3b-4a35-9c88-c7ab93a91e13" />

## 3. 설치 확인

### 방법 1. 시작 메뉴 검색

- Windows 키 → `python` 입력 → `Python 3.11` 실행 가능 여부 확인
<img width="1024" height="959" alt="image" src="https://github.com/user-attachments/assets/d5513c10-e8ee-47a5-bc0b-82da29f4515e" />

### 방법 2. 명령 프롬프트 확인
1. Windows 키 → `cmd` 입력 → 명령 프롬프트 실행
<img width="770" height="783" alt="image" src="https://github.com/user-attachments/assets/e4461b0f-504c-45b8-a2e3-5b187a71fca5" />

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
<img width="1024" height="286" alt="image" src="https://github.com/user-attachments/assets/51eb3df3-a614-4f32-b9e6-36edb96c3a70" />

---

# macOS에서 Python 설치하기

> Homebrew가 사전 설치되어 있어야 합니다. 설치되지 않은 경우 [https://brew.sh](https://brew.sh) 참고

## 1. pyenv 설치

```bash
brew install pyenv
```
<img width="1024" height="397" alt="image" src="https://github.com/user-attachments/assets/52dd9e3d-89f5-4b7c-bdb5-eafb8d75f03f" />


## 2. pyenv 환경 설정

아래 명령어를 입력하여 `.zshrc`에 설정을 추가합니다:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"
```
<img width="1024" height="146" alt="image" src="https://github.com/user-attachments/assets/d4ac7134-b652-442d-872b-229466fb53a1" />

## 3. pyenv 설치 확인

```bash
pyenv -v
```

설치된 버전이 출력되면 성공입니다.
<img width="1024" height="111" alt="image" src="https://github.com/user-attachments/assets/9f42a28e-91f8-4084-a41c-fcb7bbc73d60" />

---

## 4. Python 설치

아래 명령어로 Python 3.11.9 설치:

```bash
pyenv install 3.11.9
pyenv global 3.11.9
pyenv rehash
```
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/7960075e-9630-48fe-9cd5-8bc746fba3ff" />

## 5. 설치 확인

```bash
python -V
```

출력 예시:

```
Python 3.11.9
```
<img width="1024" height="140" alt="image" src="https://github.com/user-attachments/assets/1f7f5aa0-888b-4add-8d46-f23e491d44e9" />

---

## \[주의] 설치 후에도 Python 2.x가 출력된다면?

### 1. `.zprofile` 설정

```bash
code ~/.zprofile
```

```bash
eval "$(pyenv init --path)"
```

```bash
source ~/.zprofile
```

### 2. `.zshrc` 설정

```bash
code ~/.zshrc
```

```bash
eval "$(pyenv init -)"
```

```bash
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
<img width="1024" height="159" alt="image" src="https://github.com/user-attachments/assets/97185255-59d1-43e8-a2e4-03e411f9d257" />

참고: [https://github.com/pyenv/pyenv/wiki#suggested-build-environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

