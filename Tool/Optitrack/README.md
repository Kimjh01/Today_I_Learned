<img width="2091" height="1181" alt="image" src="https://github.com/user-attachments/assets/06fdee58-33bd-462c-b679-21e707245ad2" /># OptiTrack 설치 및 연동 가이드

> **버전 기준일**: 2025.06.17  
> 본 문서는 Motive, MATLAB, NatNet을 활용한 OptiTrack 시스템 설치 및 연동에 관한 가이드입니다.
[▶ YouTube 영상 보기](https://youtu.be/aK1cpr6ShPE?feature=shared)

---

##  목차

1. Motive 설치 및 라이선스 인증
2. Calibration 적용
3. NatNet SDK 설치
4. MATLAB 연동
5. 마커(Marker) 사용 가이드
6. Rigid Body 트래킹

---

## 1. Motive 설치 및 라이선스 인증

### 설치

- 다운로드:  
  [https://optitrack.com/support/downloads/motive.html](https://optitrack.com/support/downloads/motive.html)  
  *(현재 사용 버전인 2.1.0은 공식 사이트에서 제공되지 않음. 설치파일은 Notion에 업로드됨)*

- 설치 방법:
  1. 설치 파일 실행 → 기본 옵션 유지 권장
  2. USB Dongle 연결 후 라이선스 인증
  3. 장치 관리자(Device Manager)에서 카메라 연결 및 인식 여부 확인

- 설치 디렉토리 권장:  
  `C:\Program Files\OptiTrack\Motive`
<img width="2764" height="661" alt="image" src="https://github.com/user-attachments/assets/b335fda7-f905-48a2-85ed-888074967d67" />

### Peripheral Module

- NI-DAQ 또는 EMG 장치를 함께 사용하는 경우 해당 모듈 설치 필요

### 라이선스 인증

- License Tool 실행 후 아래 정보 입력:
  - License Serial Number: *(Notion의 PDF 참고)*
  - License Hash: *(Notion의 PDF 참고)*
  - Hardware Key Serial Number: *(USB 동글 참조)*
  - 사용자 정보: 교수님 명의 사용
- `Activate` 클릭 후 `Retry`로 프로그램 시작
- 라이선스 저장 경로:  
  `C:\ProgramData\OptiTrack\License`

<img width="888" height="1122" alt="image" src="https://github.com/user-attachments/assets/0ae00d4a-43d2-4a55-999f-87ba5b8f0286" />

---

## 2. Calibration 적용

- Motive 실행 후 **Open File** 클릭
- Notion에 업로드된 압축 파일 내  
  `CalibrationResult_2025-04-29_10` 파일을 불러오기
<img width="1201" height="779" alt="image" src="https://github.com/user-attachments/assets/0c0c6ad1-b7ff-4fef-852e-e7263e5038aa" />

---

## 3. NatNet SDK 설치

- 목적: Motive 데이터를 MATLAB, Python 등으로 스트리밍

- 다운로드:  
  [https://optitrack.com/support/downloads/developer-tools.html](https://optitrack.com/support/downloads/developer-tools.html)

- 설치 방법:
  1. ZIP 파일 다운로드 및 압축 해제
  2. SDK 폴더 구성 확인 (Samples, Libs 등)
  3. 환경변수 설정 (필요 시)

- 실행:
  - `NatNetSDK/Samples/Matlab` 내 코드 실행
  - Motive 설정 수정 필요 (실시간 스트리밍 허용 등)
<img width="1507" height="1050" alt="image" src="https://github.com/user-attachments/assets/821d7829-e5a0-46ab-bf00-c6d1b69be6ab" />

---

## 4. MATLAB 연동

- 권장 버전: **R2024a**
- 설치:  
  [https://www.mathworks.com/products/matlab.html](https://www.mathworks.com/products/matlab.html)

- 연동 방법:
  - MATLAB에서 다음 DLL 경로를 추가:
    ```
    \NatNetSDK\lib\x64\NatNetML.dll
    ```
<img width="1037" height="654" alt="image" src="https://github.com/user-attachments/assets/1ca56da3-e8c6-42c0-81e8-4d983946a255" />

---

## 5. 마커(Markers) 사용 가이드

- OptiTrack은 **수동/능동 마커** 모두 지원
- 추적 품질에 영향을 주는 요소:
  - 마커 수
  - 마커 사양 (크기, 원형도, 반사율)
  - 배치 위치
  - 재질 관리 상태

- **수동 마커**:  
  IR 광선을 완전히 반사할 수 있도록 **재귀반사 표면**이 필요
<img width="934" height="597" alt="image" src="https://github.com/user-attachments/assets/b7bae758-072a-4cbb-ab6d-041d98394974" />

### 구매 링크

- 공식 마커 구매:  
  [https://www.optitrack.com/accessories/markers/#msc1040](https://www.optitrack.com/accessories/markers/#msc1040)

- 국내 대체재 예시:  
  - 3M 스카치라이트 반사원단 (접착식)  
  - 쿠팡 등 온라인 마켓

---

## 6. Rigid Body Tracking

- Motive에서 생성된 마커 그룹(구성체)을 Rigid Body로 지정하여 실시간 트래킹
- 별도 설정은 Motive 내에서 진행

---

##  관련 링크 정리

- Motive 다운로드:  
  https://optitrack.com/support/downloads/motive.html
- NatNet SDK:  
  https://optitrack.com/support/downloads/developer-tools.html
- MATLAB:  
  https://www.mathworks.com/products/matlab.html
- 마커 구매:  
  https://www.optitrack.com/accessories/markers/

---

##  설치파일 및 자료 위치

- Motive 2.1.0 설치파일  
- License PDF  
- Calibration 파일  
- 위 자료들은 Notion 또는 공유 드라이브에 업로드됨

---

