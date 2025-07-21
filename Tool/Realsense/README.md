# Intel® RealSense™ D455 캘리브레이션 가이드

본 문서는 ORB-SLAM3 또는 유사한 비주얼 슬램 시스템에서 **정확한 위치 추정**을 위한 Intel RealSense D455의 **내부/외부 파라미터 보정(calibration)** 방법을 다룹니다. Kalibr 도구를 활용한 카메라 및 IMU 보정 절차를 기반으로 정리했습니다.

---
<img width="1920" height="667" alt="image" src="https://github.com/user-attachments/assets/d78216ba-1472-4d51-8de6-b464274fd6a0" />

## 1. 좌표계 정의 및 외부 파라미터 (Extrinsic Parameters)

### 좌표계

* **World (W)**: SLAM이 기준으로 삼는 전역 좌표계. Z축은 중력 반대 방향.
* **Body (B)**: IMU가 장착된 기준 좌표계. SLAM의 최적화 대상.
* **Camera (C1, C2)**: 각각 좌/우 카메라 좌표계. z축은 카메라 전방.

  <img width="523" height="329" alt="image" src="https://github.com/user-attachments/assets/787dd6b4-c22b-4bf5-9311-98e3c3ef8c54" />

### 관계식

* 좌표변환 수식:

  * \$T\_{WC1} = T\_{WB} \cdot T\_{BC1}\$
  * \$T\_{WC2} = T\_{WB} \cdot T\_{BC1} \cdot T\_{C1C2}\$

* 예: 카메라 1 기준 좌표 \$x\_{C1}\$를 세계 좌표로 변환:

  * \$x\_W = T\_{WC1} \cdot x\_{C1}\$

### 필요한 외부 파라미터

| 구성              | 필요 파라미터                     |
| --------------- | --------------------------- |
| Mono-Inertial   | \$T\_{BC1}\$                |
| Stereo-Inertial | \$T\_{BC1}\$, \$T\_{C1C2}\$ |
| Stereo          | \$T\_{C1C2}\$               |
| Mono            | 파라미터 불필요                    |

---

## 2. 카메라 내부 파라미터 (Intrinsic Parameters)

### 모델: **Pinhole**

D455는 기본적으로 `pinhole` 모델이며, 다음 파라미터가 필요합니다:

* **초점거리 & 중심점**: \$(f\_x, f\_y, c\_x, c\_y)\$
* **왜곡계수**:

  * Radial: \$k\_1, k\_2, (k\_3)\$
  * Tangential: \$p\_1, p\_2\$

#### 예시 (D455 기준 OpenCV 형식):

```yaml
Camera1.fx: 381.6
Camera1.fy: 381.6
Camera1.cx: 321.58
Camera1.cy: 236.20
Camera1.k1: -0.0047
Camera1.k2: 0.0011
Camera1.p1: -0.00029
Camera1.p2: 0.00066
```

### 리얼센스 Kalibr 캘리브레이션 결과 비교 (D455)

| 파라미터 | Factory | Kalibr 결과 (± 오차) |
| ---- | ------- | ---------------- |
| fx   | 382.613 | 381.698 ± 0.4787 |
| fy   | 382.613 | 381.659 ± 0.4870 |
| cx   | 320.183 | 321.582 ± 0.4010 |
| cy   | 236.455 | 236.202 ± 0.3860 |
| k1   | 0       | -0.0047 ± 0.0017 |
| k2   | 0       | 0.0011 ± 0.0020  |

---

## 3. IMU 파라미터 (Intrinsic & Noise Models)

### IMU 출력 수식

* 가속도:

  * \$\tilde{a} = a + \eta\_a + b\_a\$
* 자이로:

  * \$\tilde{\omega} = \omega + \eta\_g + b\_g\$

### 노이즈 분포

* 가속도 노이즈: \$\eta\_a \sim \mathcal{N}(0, \sigma^2\_a I\_3)\$
* 자이로 노이즈: \$\eta\_g \sim \mathcal{N}(0, \sigma^2\_g I\_3)\$
* 랜덤 워크:

  * \$b\_{a,i+1} = b\_{a,i} + \eta\_{a,rw}, \quad \eta\_{a,rw} \sim \mathcal{N}(0, \sigma^2\_{a,rw} I\_3)\$
  * \$b\_{g,i+1} = b\_{g,i} + \eta\_{g,rw}, \quad \eta\_{g,rw} \sim \mathcal{N}(0, \sigma^2\_{g,rw} I\_3)\$

### 예시 파라미터 (BMI055 기준)

```yaml
IMU.NoiseAcc: 0.0028        # m/s^1.5
IMU.NoiseGyro: 0.00016      # rad/s^0.5
IMU.AccWalk: 0.00086        # m/s^2.5
IMU.GyroWalk: 0.000022      # rad/s^1.5
IMU.Frequency: 200          # Hz
```

---

## 4. Kalibr를 이용한 캘리브레이션 절차

### A. 데이터 수집

1. **AprilTag 패턴 인쇄 (A0 권장)**
2. `realsense-viewer` 또는 Kalibr 제공 recorder 사용:

```bash
./recorder_realsense_D435i ./Calibration/recorder/
```

* cam0, imu 폴더 생성 필수

3. IMU 정렬 및 보정: (동기화)

```bash
python3 ./process_imu.py ./Calibration/recorder/
```

---

### B. 시각 (카메라) 캘리브레이션

```bash
./kalibr_calibrate_cameras \
--bag ./recorder.bag \
--topics /cam0/image_raw \
--models pinhole -radtan \
--target ./aprilgrid.yaml
```

* 슬로우 모션으로 촬영 권장
* 패턴은 화면 전체를 가득 채우도록 구성
* Kalibr은 최소 기준 없으나 다양한 시점 필요

---

### C. 관성 (IMU) 캘리브레이션

```bash
./kalibr_calibrate_imu_camera \
--bag ./recorder.bag \
--cam ./camera_calibration.yaml \
--imu ./imu_intrinsics.yaml \
--target ./aprilgrid.yaml
```

* 패턴은 항상 시야에 위치해야 함
* 빠른 움직임으로 모든 축을 자극

#### 예시 결과: T<sub>BC</sub>

| Factory                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ |
| \$T\_{BC} = \begin{bmatrix} 1 & 0 & 0 & -0.005 \ 0 & 1 & 0 & -0.005 \ 0 & 0 & 1 & 0.0117 \ 0 & 0 & 0 & 1 \end{bmatrix}\$ |

| Kalibr 결과                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \$T\_{BC} = \begin{bmatrix} 0.9999 & 0.0003 & -0.0135 & -0.0015 \ -0.0002 & 0.9999 & 0.0054 & 0.0004 \ 0.0135 & -0.0054 & 0.9999 & 0.0201 \ 0 & 0 & 0 & 1 \end{bmatrix}\$ |

---

## 참고

* [Kalibr 공식 GitHub](https://github.com/ethz-asl/kalibr)
* [Kalibr 다운로드/설치](https://github.com/ethz-asl/kalibr/wiki/downloads)
* [D455 카메라 공식 소개](https://www.intelrealsense.com/depth-camera-d455/)
* [Kalibr 캘리브레이션 영상](https://youtu.be/R_K9-O4ool8)


