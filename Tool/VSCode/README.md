# Visual Studio Code 설치 및 설정 가이드

## VSCode를 사용하는 이유

- 마이크로소프트에서 개발한 가볍고 빠른 코드 에디터
- Windows, macOS, Linux 모두 지원
- 다양한 확장 프로그램(Extension)을 통한 무한한 기능 확장성
- 전 세계에서 높은 점유율을 자랑하는 인기 에디터
- 무료로 사용 가능

> 참고: 이미 설치되어 있어도 설정이 다를 수 있으므로, 새롭게 설치 및 설정하는 것을 권장합니다.

<img width="1024" height="426" alt="image" src="https://github.com/user-attachments/assets/53aed6d8-b26a-4a0e-953b-ae5f2cb2bd45" />

---

# Windows에서 설치하기

> 본 가이드는 Windows 11 기준으로 작성되었습니다. Windows 10과 거의 동일합니다.

## 1. VSCode 다운로드

- 공식 웹사이트: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- 접속 후 `Download for Windows` 클릭하여 설치 파일을 다운로드합니다.

  <img width="1024" height="620" alt="image" src="https://github.com/user-attachments/assets/04952311-898e-4bd2-8bbb-e51440c72f03" />


## 2. VSCode 설치

- 다운로드한 `.exe` 파일을 실행하고 설치 마법사의 안내에 따라 진행합니다.
- 설치 중 다음 항목을 반드시 체크하는 것을 권장합니다:

  - `"Code로 열기"를 Windows 탐색기 상황 메뉴에 추가`
  - `지원되는 파일 형식에 대한 편집기로 등록`
  - `PATH에 추가`

<img width="598" height="464" alt="image" src="https://github.com/user-attachments/assets/cfefd631-8d8b-4542-a1ab-56a175f6f3fd" />
<img width="598" height="464" alt="image" src="https://github.com/user-attachments/assets/e20e3fa3-2073-41b3-85de-3f3d8f540100" />
<img width="598" height="464" alt="image" src="https://github.com/user-attachments/assets/47baa350-00d0-454e-b9c2-83ef8935116e" />
<img width="598" height="464" alt="image" src="https://github.com/user-attachments/assets/dff634b8-239f-4f8b-b44b-caf9a8219c34" />
<img width="598" height="464" alt="image" src="https://github.com/user-attachments/assets/72bc5d3d-a8fb-4bce-9e78-8a926feb3cde" />
<img width="598" height="464" alt="image" src="https://github.com/user-attachments/assets/994d88b0-e35c-46de-920b-cee7ee84ec4e" />
<img width="1024" height="768" alt="image" src="https://github.com/user-attachments/assets/c108a6bb-2564-4a7f-93d3-ff7f3ab61f98" />

> 위 설정을 통해 VSCode를 더 편리하게 사용할 수 있습니다.

## 3. 설치 확인

- 폴더에서 마우스 우클릭 → `Code로 열기` 항목이 있는지 확인
<img width="1024" height="764" alt="image" src="https://github.com/user-attachments/assets/c75dccd9-9658-4f22-a198-1a39e787b38f" />

- 또는 명령 프롬프트에서 아래 명령어 입력:

```bash
code --version
````

---

# macOS에서 설치하기

> macOS에서는 Homebrew가 설치되어 있어야 합니다. 설치되지 않은 경우 [https://brew.sh](https://brew.sh) 참고

## 1. VSCode 설치

```bash
brew install --cask visual-studio-code
```
<img width="1024" height="321" alt="image" src="https://github.com/user-attachments/assets/a8d526c0-4823-40bf-be49-41bfa566425f" />
<img width="1024" height="661" alt="image" src="https://github.com/user-attachments/assets/80ed1999-97ae-492c-8bd4-17123330c7b5" />


## 2. PATH에 `code` 명령어 추가

```bash
# VSCode 실행 → CMD + Shift + P → shell 입력
# Shell Command: Install ‘code’ command in PATH 선택
```

* 이후 `Terminal`에서 `code .` 명령어로 VSCode 실행 가능
* 적용 후 터미널 재시작 필요

<img width="1024" height="213" alt="image" src="https://github.com/user-attachments/assets/4d72984b-0606-41a2-a1b8-f3bc99645265" />
<img width="1024" height="357" alt="image" src="https://github.com/user-attachments/assets/c5aba5be-2d8a-4663-aeae-552735419933" />


## 3. OpenInTerminal 설치 및 설정 (Finder에서 VSCode 실행용)

```bash
brew install --cask openinterminal
```

<img width="1024" height="336" alt="image" src="https://github.com/user-attachments/assets/f06c73c7-bd22-495b-8fbf-bd68ee2d4e4d" />


### 설정 방법

1. 시스템 설정 → 확장 프로그램 → Finder 확장 프로그램에서 `OpenInTerminalFinderExtension` 체크
2. OpenInTerminal 실행 → Default Editor: Visual Studio Code 설정
3. 단축키 등록 시 VSCode 및 Terminal을 Finder 위치에서 바로 실행 가능

---

# VSCode 확장 프로그램 설치

## Python Extension

> VSCode에서 Python을 실행 및 디버깅하기 위한 필수 확장

1. VSCode 실행 → Extensions (`Ctrl+Shift+X`) 클릭
2. `python` 검색 후 Microsoft 제공 Python 확장 설치

> Python이 사전 설치되어 있어야 합니다.

<img width="1024" height="422" alt="image" src="https://github.com/user-attachments/assets/a30cfd01-2ab8-45b9-ad53-0f3e099c247b" />
<img width="1024" height="615" alt="image" src="https://github.com/user-attachments/assets/058c9f5c-d860-447e-aaba-6db7cfe630db" />


## Jupyter Extension

> VSCode에서 `.ipynb` 주피터 노트북 실행을 위한 확장

1. Extensions 메뉴에서 `jupyter` 검색
2. Jupyter 확장 설치 후 `.ipynb` 파일을 VSCode에서 바로 실행 가능

## VSCode-icons

> 프로젝트 내 폴더 및 파일 아이콘을 시각적으로 구분하기 위해 사용

1. Extensions에서 `vscode-icons` 검색 후 설치
2. 설치 후 테마 적용을 묻는 창에서 `Yes` 선택

<img width="1024" height="426" alt="image" src="https://github.com/user-attachments/assets/3c414169-4e87-4745-8b6a-1c8924a2f8d3" />


---

# 사용자 설정 예시 (탭 크기 등)

1. `Ctrl + Shift + P` 또는 `F1` → `json` 검색
2. `Preferences: Open Settings (JSON)` 클릭
3. 아래 설정을 추가하고 저장

```json
{
  "editor.tabSize": 2,
  "[python]": {
    "editor.tabSize": 4
  }
}
```
<img width="1024" height="569" alt="image" src="https://github.com/user-attachments/assets/8f478d0c-c807-4ea0-810b-9188874e6ed6" />


