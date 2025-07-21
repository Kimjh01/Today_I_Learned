# Python 3.9 & PyTorch & 가상환경 구성 가이드

## 0. 구성 목표

* Python 3.9 설치
* PyTorch 설치 (CPU/GPU 선택)
* 가상환경 구성 (`venv` 기반)
* `requirements.txt` 연동
* Windows 및 macOS 둘 다 지원

---

## 1. Python 3.9 설치

### Windows

1. 다운로드: [https://www.python.org/downloads/release/python-390/](https://www.python.org/downloads/release/python-390/)

2. 설치:

   * `Add python.exe to PATH` 반드시 체크 
   * `Install Now` 클릭
   * 설치 완료 후 `Disable path length limit` 클릭 (표시되면)

3. 확인:

```bash
python -V
# 출력 예시: Python 3.9.0
```

---

### macOS

> `pyenv`를 통해 설치합니다. Homebrew가 먼저 설치되어 있어야 합니다. [https://brew.sh](https://brew.sh)

1. pyenv 설치

```bash
brew install pyenv
```

2. 환경 설정 (`~/.zshrc`에 추가):

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

3. Python 설치

```bash
pyenv install 3.9.13
pyenv global 3.9.13
pyenv rehash
```

4. 확인:

```bash
python -V
# 출력 예시: Python 3.9.13
```

> 빌드 오류 방지를 위해 아래 패키지 설치 권장:

```bash
brew install openssl readline sqlite3 xz zlib tcl-tk
```

---

## 2. 가상환경 만들기 (Windows & mac 공통)

### 왜 필요한가?

* 프로젝트마다 Python 패키지 버전이 다를 수 있음
* PyTorch나 기타 딥러닝 라이브러리는 환경이 민감함
* 가상환경은 프로젝트별 독립 공간을 만들어 충돌 없이 실행 가능

### 가상환경 생성

```bash
python -m venv [가상환경명]
# 예시: python -m venv torch-env
```

### 가상환경 활성화

#### Windows:

```bash
.\torch-env\Scripts\activate
```

#### macOS / Linux:

```bash
source torch-env/bin/activate
```

활성화되면 프롬프트에 `(torch-env)`가 붙음

### 가상환경 비활성화

```bash
deactivate
```

---

## 3. PyTorch 설치

> 공식 설치 가이드: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

### CPU 전용 설치

```bash
pip install torch torchvision torchaudio
```

### GPU (CUDA 11.8) 설치 (Windows 한정)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## 4. 종속성 파일로 구성 관리

### 설치된 패키지 목록 저장

```bash
pip freeze > requirements.txt
```

### requirements.txt 기반 설치

```bash
pip install -r requirements.txt
```

> 팀 프로젝트나 배포 시 매우 유용함

---

## 5. 권장 프로젝트 구성 구조

```
project-root/
├── torch-env/             # 가상환경 (깃허브에 올리지 않음)
├── main.py
├── utils.py
├── requirements.txt       # 패키지 목록
└── README.md
```

> `.gitignore`에 `torch-env/` 추가하여 깃허브 업로드 제외

---

## 6. 확인 코드 예시

```python
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
```

---

## 요약 표

| 항목            | Windows                 | macOS                |
| ------------- | ----------------------- | -------------------- |
| Python 설치     | 공식 `.exe`, PATH 체크      | `pyenv`, zshrc 설정    |
| 가상환경          | `python -m venv`        | 동일 (`source`로 활성화)   |
| PyTorch (CPU) | pip 설치 가능               | pip 설치 가능 (CPU only) |
| PyTorch (GPU) | CUDA 11.8 지원 가능         | 지원 안함                |
| 패키지 관리        | `requirements.txt`로 동기화 | 동일                   |

---

## 추가 팁

* 가상환경 폴더는 Git 업로드하지 말고 `.gitignore`에 포함
* 프로젝트 복사 시 다음 순서로 실행:

  1. 가상환경 생성
  2. `requirements.txt` 설치
  3. `main.py` 실행

---

이 가이드는 **Anaconda 없이도 PyTorch 개발 환경**을 안정적으로 구축할 수 있도록 설계되었습니다.
추가로 Jupyter Notebook 연동이나 VSCode 설정이 필요하면 말씀 주세요.
