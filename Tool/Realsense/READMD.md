# Intel® RealSense™ Depth Camera D455

[**RealSense D455 Setup** ](https://www.notion.so/RealSense-D455-Setup-1500ff9c67f681459a64d1a050420067?pvs=21)

---

- Realsense-Python

[librealsense/wrappers/python/examples at development · IntelRealSense/librealsense](https://github.com/IntelRealSense/librealsense/tree/development/wrappers/python/examples)

[pyrealsense2](https://pypi.org/project/pyrealsense2/#files)

[[RealSense] Python 개발 환경 세팅](https://coding-ga-ding.tistory.com/186)

---

# Camera Calibration

[Calibration_Tutorial.pdf](Calibration_Tutorial.pdf)

[ORB-SLAM3_RealSense.pdf](ORB-SLAM3_RealSense.pdf)

- Calibration Tutorial for ORB-SLAM3

[DIY Indoor Autonomous Drone! - Part 2 (Kalibr & Calibration)](https://www.youtube.com/watch?app=desktop&v=puNXsnrYWTY)

[GitHub - ethz-asl/kalibr: The Kalibr visual-inertial calibration toolbox](https://github.com/ethz-asl/kalibr)

[Calibration_Tutorial.pdf](Calibration_Tutorial%201.pdf)

Mono:/camera/image_raw -> /camera/color/image_raw(RGB camera)

Mono-Inertial: /imu, /camera/image_raw -> /camera/imu,/camera/color/image_raw

RGBD: /camera/rgb/image_raw,/camera/depth_registered/image_raw 

->/camera/color/image_raw,/camera/aligned_depth_to_color/image_raw

Stereo: /camera/left/image_raw, /camera/right/image_raw 

->/camera/infra1/image_rect_raw,/camera/infra2/image_rect_raw

Stereo-Inertial: /camera/left/image_raw,/camera/right/image_raw, /imu 

->/camera/infra1/image_rect_raw,/camera/infra2/image_rect_raw, /camera/imu

---

[Camera Tuning Intel Realsense](https://sisaha9.github.io/camera_mapping_navigation_website/tuning.html)
