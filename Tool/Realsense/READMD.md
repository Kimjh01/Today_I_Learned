# Intel® RealSense™ Depth Camera D455 Setup Guide

본 문서는 Intel RealSense D455 모델을 Ubuntu 환경에서 설치 및 활용하는 과정을 정리한 가이드입니다. ROS, Python 연동, 카메라 튜닝, 캘리브레이션 등 실질적인 작업 흐름을 포함합니다.

---

## 시스템 사양 및 요구사항

- **카메라 모델**: Intel® RealSense™ D455
- **운영체제**: Ubuntu 20.04 LTS
- **ROS 버전**: Noetic
- **SDK 버전**: 2.55.1 (권장)
- **Python 연동 시**: pyrealsense2 패키지 사용

---

## 1. 시스템 준비 (Ubuntu)

```bash
sudo apt update
sudo apt upgrade
sudo apt install git wget curl cmake build-essential -y
sudo apt install libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
````

---

## 2. Intel RealSense SDK 설치

```bash
mkdir librealsense && cd librealsense
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense
git checkout v2.50.0
```

### udev rule 설정

```bash
sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && udevadm trigger
```

### 빌드 및 설치

```bash
mkdir build && cd build
cmake ../ -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install
```

---

## 3. ROS 패키지 설치 (Noetic)

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros
git checkout 2.3.2
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
cd src && catkin_init_workspace
cd .. && catkin_make clean
catkin_make
catkin_make install
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## 4. Python 연동 (`pyrealsense2`)

```bash
pip install pyrealsense2
```

예제 경로:
`librealsense/wrappers/python/examples/`

---

## 5. 펌웨어 업데이트 (선택 사항)

### 방법 1. realsense-viewer GUI 사용

```bash
realsense-viewer
```

* 카메라 인식 후 More → Firmware → 파일 선택 → 적용 후 재부팅

### 방법 2. CLI 도구 사용

```bash
rs-fw-update -f Signed_Image.bin
```

---

## 6. 캘리브레이션 및 튜닝

### ORB-SLAM3용 토픽 매핑 예시

| 구성              | 입력 토픽 → 변환 후 토픽                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| RGB             | /camera/image\_raw → /camera/color/image\_raw                                                                                           |
| RGBD            | /camera/rgb/image\_raw, /camera/depth\_registered/image\_raw → /camera/color/image\_raw, /camera/aligned\_depth\_to\_color/image\_raw   |
| Stereo-Inertial | /camera/left/image\_raw, /camera/right/image\_raw, /imu → /camera/infra1/image\_rect\_raw, /camera/infra2/image\_rect\_raw, /camera/imu |

### 주의 사항

* 야외나 강한 광원이 있는 환경에서는 Depth 품질 저하 발생 가능 → 설정값 조절 필요
* 캘리브레이션 도구로 Kalibr, ORB-SLAM3 등 사용 가능

---

## 7. 참고 명령어

### 카메라 확인

```bash
realsense-viewer
rs-enumerate-devices
```

### 실시간 데이터 스트림 확인

```bash
roslaunch realsense2_camera rs_camera.launch
```

---

## 참고자료 정리

* **D455 공식 소개**: [https://www.intelrealsense.com/depth-camera-d455/](https://www.intelrealsense.com/depth-camera-d455/)
* **SDK 다운로드**: [https://github.com/IntelRealSense/librealsense](https://github.com/IntelRealSense/librealsense)
* **ROS Wrapper**: [https://github.com/IntelRealSense/realsense-ros](https://github.com/IntelRealSense/realsense-ros)
* **Python 예제**: `librealsense/wrappers/python/examples`
* **pyrealsense2 설치**: [https://pypi.org/project/pyrealsense2](https://pypi.org/project/pyrealsense2)
* **캘리브레이션 튜토리얼 PDF**: 내부 문서 참조

---

## 요약

| 항목        | 내용                               |
| --------- | -------------------------------- |
| SDK 설치 경로 | `/opt/realsense` 또는 `/usr/local` |
| ROS 연동    | `catkin_ws/src/realsense-ros`    |
| Python 지원 | `pyrealsense2` 사용                |
| 최대 거리     | 최대 4m, Z-Error ±2%               |
| 글로벌 셔터    | RGB, IR 모두 지원                    |
| IMU 센서    | 6DoF (가속도계 + 자이로)                |

---

