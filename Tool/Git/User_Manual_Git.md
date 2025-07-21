# Git 설치 가이드 (버전 2.41.0 기준)

> 본 가이드는 Git 버전 2.41.0을 기준으로 작성되었습니다.  
> 설치 시기에 따라 Git 버전은 달라질 수 있습니다.

---

# Windows에서 Git 설치하기

## 1. Git 다운로드

1. [https://git-scm.com/](https://git-scm.com/) 접속  
2. `Download for Windows` 버튼 클릭  
3. 본인 CPU 구조(32bit 또는 64bit)에 맞는 `Standalone Installer` 다운로드  

<img width="1011" height="784" alt="image" src="https://github.com/user-attachments/assets/67bd3241-b77c-4249-809e-265b06afaac3" />

<img width="686" height="483" alt="image" src="https://github.com/user-attachments/assets/4367beca-507d-4b9b-85c0-2bab2dae2567" />


### CPU 구조 확인 방법

1. 시작 메뉴에서 `시스템`을 검색 후 실행  
2. `시스템 종류` 항목에서 32비트/64비트 여부 확인

## 2. Git 설치

1. 다운로드한 설치파일(`.exe`)을 실행  
2. 설치 마법사 안내에 따라 기본 설정 그대로 진행 (`Next` 연속 클릭)

> 반드시 설치 경로는 변경하지 마세요. (기본 경로 그대로 유지)

3. 설치 중 주요 설정 항목 예시:
   - `Git from the command line and also from 3rd-party software`: 기본 선택 유지
   - `Use the OpenSSL library`: 기본 선택 유지
   - `Checkout Windows-style, commit Unix-style line endings`: 기본 선택 유지
   - `Enable symbolic links`: **체크 권장**

> `Enable symbolic links`: Git에서 심볼릭 링크를 지원하도록 설정. 원본 파일을 링크 형태로 다룰 수 있습니다.

4. 설치 완료 후 `Finish` 클릭

<img width="499" height="392" alt="image" src="https://github.com/user-attachments/assets/727eca3b-8384-4303-b8ad-a54ea034260e" />
<img width="498" height="393" alt="image" src="https://github.com/user-attachments/assets/673bb308-2128-4ef0-bbd2-f433b1a8b81d" />
<img width="501" height="393" alt="image" src="https://github.com/user-attachments/assets/68444d55-a5cc-46ba-adf4-bf71eb592316" />
<img width="499" height="392" alt="image" src="https://github.com/user-attachments/assets/b3060aff-487e-4dff-93ba-88abca4811bd" />
<img width="500" height="393" alt="image" src="https://github.com/user-attachments/assets/66b78b38-7192-4a23-8aca-032b18095b95" />
<img width="500" height="391" alt="image" src="https://github.com/user-attachments/assets/4a6f0a5b-49df-4e84-bfd0-2e2aab84a7c2" />
<img width="500" height="392" alt="image" src="https://github.com/user-attachments/assets/7ccbdb01-397b-4e3f-825b-356a66719692" />
<img width="500" height="391" alt="image" src="https://github.com/user-attachments/assets/fa53d630-361c-4e92-9402-84ba42c85039" />
<img width="500" height="393" alt="image" src="https://github.com/user-attachments/assets/ed25b628-4b40-40c7-b085-b22d00a2f046" />
<img width="499" height="392" alt="image" src="https://github.com/user-attachments/assets/96faf506-6978-4d4e-8c0a-fe8327e19621" />
<img width="500" height="392" alt="image" src="https://github.com/user-attachments/assets/ea80a246-5a49-4110-af1d-ee8c8351292f" />
<img width="501" height="393" alt="image" src="https://github.com/user-attachments/assets/81824610-4f16-4511-9993-714f50196dd9" />
<img width="501" height="393" alt="image" src="https://github.com/user-attachments/assets/90b19a62-ad21-45de-96be-615be546be03" />
<img width="500" height="392" alt="image" src="https://github.com/user-attachments/assets/11d2d98f-b8f8-4f91-8bde-6a56a8de0f20" />
<img width="498" height="392" alt="image" src="https://github.com/user-attachments/assets/fc3f7460-e4d0-4d90-a8f0-f5914adfb60b" />
<img width="500" height="392" alt="image" src="https://github.com/user-attachments/assets/d62ed9aa-52f6-4873-a406-fe50ca949d5c" />


## 3. 설치 확인

- 바탕화면 또는 폴더에서 **마우스 우클릭** → `Git Bash Here` 항목이 보이면 설치 완료  
- 또는 명령 프롬프트(cmd) 또는 Git Bash에서 다음 명령어 실행:

```bash
git --version
````

정상 출력 예시:

```
git version 2.41.0
```

---

# macOS에서 Git 설치하기

> macOS에서는 Git 설치 전 **Homebrew**가 필요합니다.
> 설치되지 않은 경우 [https://brew.sh/](https://brew.sh/) 참고

## 1. Git 설치

터미널에서 아래 명령어 입력:

```bash
brew install git
```

설치가 완료되면 Git 실행 파일이 `/usr/local/bin/git` 경로에 위치합니다.

## 2. 경로(PATH) 설정

Homebrew로 설치한 Git이 정상 작동하도록 `PATH`를 설정합니다:

```bash
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

> `.zshrc`는 macOS 기본 셸인 zsh의 설정 파일입니다.
> 위 설정은 Git을 우선적으로 인식하도록 경로를 등록합니다.

## 3. 설치 확인

터미널에서 다음 명령어 입력:

```bash
git --version
```

결과 예시:

```
git version 2.41.0
```

---

# 설치 후 필수 설정 (공통)

Git 설치 후 사용자 정보를 등록합니다:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

설정 확인:

```bash
git config --global --list
```

---

# 추가 권장 사항

* GitHub 연동을 위한 **SSH Key 생성**
* GUI 툴 사용 고려: **Sourcetree**, **GitKraken**, **GitHub Desktop** 등
* 기본 에디터 설정: `vim` → `code` 등으로 변경 가능

```bash
git config --global core.editor "code --wait"
```


