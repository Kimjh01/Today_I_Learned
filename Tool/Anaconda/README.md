# Anaconda 설치 가이드 (Windows & macOS 공통)

---

## Anaconda란?

* 파이썬과 데이터 과학, 머신러닝 관련 패키지를 통합 관리할 수 있는 플랫폼
* 가상환경 관리가 간편하며 `Jupyter`, `NumPy`, `pandas`, `matplotlib`, `scikit-learn`, `TensorFlow`, `pytorch` 등 포함
* Visual Studio Code와 연동 가능

---

## 1. 설치 파일 다운로드

**공식 웹사이트 접속:**

[https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

* 운영체제에 맞는 **Python 3.x 버전의 설치파일** 다운로드

  * Windows: `Anaconda3-202x.x-Windows-x86_64.exe`
  * macOS(Intel/M1): `Anaconda3-202x.x-MacOSX-x86_64.pkg` 또는 `arm64.pkg`

---

## 2. 설치 (Windows 기준)

1. **다운로드한 `.exe` 파일 실행**
2. 설치 종류 선택: `Just Me` (권장)
3. 설치 경로 설정 (기본 경로 그대로 둬도 무방)
4. 옵션 체크

   * Add Anaconda3 to my PATH environment variable → **체크하지 않는 것이 권장**
   * Register Anaconda3 as my default Python → **체크**
5. 설치 완료 후 `Anaconda Navigator` 또는 `Anaconda Prompt` 실행 가능

---

## 3. 설치 (macOS 기준)

1. `.pkg` 설치파일 실행 후 설치
2. 설치 후 터미널 열고 다음 명령어로 Anaconda 활성화:

```bash
source ~/opt/anaconda3/bin/activate
```

---

## 4. 설치 확인 (공통)

```bash
conda --version
python --version
```

---

## 5. 가상 환경 생성 및 활성화

```bash
conda create -n myenv python=3.10
conda activate myenv
```

---

## 6. 필수 패키지 설치 예시

```bash
conda install numpy pandas matplotlib jupyter
pip install pyrealsense2
```

---

## 7. VSCode 연동 (선택 사항)

### 설치 후 VSCode 연동하려면:

```bash
conda install -c conda-forge vscode
```

또는 VSCode에서 `Python` extension 설치 → `Anaconda 환경 선택`

---

## 8. Jupyter Notebook 실행

```bash
jupyter notebook
```

브라우저가 자동 실행되며 `.ipynb` 작성 가능

---

## 9. 기타 유용한 명령어

```bash
conda env list                      # 가상환경 목록
conda deactivate                   # 현재 환경 비활성화
conda remove -n myenv --all        # 가상환경 삭제
conda install -n myenv 패키지명     # 특정 환경에 설치
```

---

## 참고

* 공식 문서: [https://docs.anaconda.com](https://docs.anaconda.com)
* VSCode 연동 가이드: [https://code.visualstudio.com/docs/python/environments](https://code.visualstudio.com/docs/python/environments)


