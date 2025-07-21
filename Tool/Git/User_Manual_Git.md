# Git 설치 가이드 (버전 2.41.0 기준)

> 본 가이드는 Git 버전 2.41.0을 기준으로 작성되었습니다.  
> 설치 시기에 따라 Git 버전은 달라질 수 있습니다.

---

# Windows에서 Git 설치하기

## 1. Git 다운로드

1. [https://git-scm.com/](https://git-scm.com/) 접속  
2. `Download for Windows` 버튼 클릭  
3. 본인 CPU 구조(32bit 또는 64bit)에 맞는 `Standalone Installer` 다운로드  

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

---

이 문서는 이미지 없이 작성된 텍스트 기반 Git 설치 가이드입니다.
원하는 위치에 설치 캡처 이미지를 추가하시면 더욱 직관적인 문서가 됩니다.

```

