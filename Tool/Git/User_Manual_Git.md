<aside>
💡 본 가이드는 버전 2.41.0 기준으로 작성되었습니다.
설치 시기에 따라 버전은 다를 수 있습니다.

</aside>

# for Windows

## Git 다운로드하기

1. [**https://git-scm.com/](https://git-scm.com/) 접속 → `Download for Windows`를 클릭합니다.**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee406ce1-e517-4302-a497-b1c321c8cd34/Untitled.png)
    

1. **본인의 CPU에 해당하는 `Standalone Installer`를 클릭해 다운로드합니다.**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6ce343ec-803f-4be0-8011-d68cf03c3419/Untitled.png)
    
    - **CPU 구조(32bit/64bit) 확인하는 방법**
        1. **윈도우 키 클릭 → `시스템`을 검색 후 클릭합니다.**
            
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de03cb7c-b1ee-4679-8317-fa051ab1ea80/Untitled.png)
            
        
        1. **시스템 종류에서 32비트/64비트 여부를 확인합니다.**
            
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e8540b92-a3d4-4add-b5ca-927979fb1f3d/Untitled.png)
            

## Git 설치하기

1. **다운로드한 설치파일을 실행합니다.**

1. **아래 순서대로 설치를 진행합니다.**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f37bf318-7611-4d50-94c4-b8518cec54ca/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a40a7e71-24aa-4aad-9479-cfd378c39049/Untitled.png)
    
    ***※주의※ 절대로 Git 설치 경로를 변경하지 않습니다!***
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/87c8f72c-719f-4a60-8755-7573708dd617/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/44b2fde6-f1a1-4e87-8b43-add98d73f09b/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b663003-005e-495e-81df-3d815a340a5b/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/984a01a4-df6e-4af4-8ed4-6e463d5d4d53/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5079f22-08d1-4482-89ec-6453cf7a09e2/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b20f3634-428b-482f-a869-239522d7166f/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9496f248-52b9-4b22-889d-c3a82802ce35/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b4663ade-7c45-4d07-a194-47b86a2ca132/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dbae0ead-3d34-4755-8f63-396f7f09ec3f/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bb63016-8220-4aa7-b77c-8e17196c2663/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28f73867-d4d4-43e3-914a-48001cd43bab/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cf45d9f3-370f-4b53-b01b-863afdd5f3ec/Untitled.png)
    
    - `Enable symbolic links`에 체크하는 이유?
        - symbolic links를 활성화 함으로써 링크를 통해 원본 파일을 직접 사용하는 것과 같은 효과를 얻을 수 있습니다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1eb738c0-2646-4b1a-bdf5-46389b49da94/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0f51ade-1a62-4111-867b-ed0d8d8111b3/Untitled.png)
    

## Git 설치 확인하기

1. **바탕화면에서 `마우스 우클릭` - `더 많은 옵션 표시` - `Git Bash Here` 옵션이 있는지 확인합니다.**
    
    **(windows10은 `마우스 우클릭` - `Git Bash Here`)**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a1e33200-3f2f-4078-b517-fa4cddbea711/Untitled.png)
    

# for macOS

<aside>
📌 Homebrew가 사전에 설치되어 있어야 합니다. ([macOS 초기 설정](https://www.notion.so/macOS-fbf122253a4049cbac3b48d2ebd0d751?pvs=21) )

</aside>

## Git 설치하기

1. **터미널에서 아래 코드를 입력해 설치합니다.**
    
    ```bash
    brew install git
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b4d5851e-8b83-4cf7-b8e6-26d1c8c0bc46/Untitled.png)
    

1. **터미널에서 아래 코드를 입력해 설정합니다.**
    
    ```bash
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dbe0747e-4090-49c3-98c0-b96590727427/Untitled.png)
    
    - 설정 완료 후에도 터미널 상으로는 변화가 없으므로 한 번만 입력해주세요.

1. **터미널에서 아래 코드를 입력해 설치를 확인합니다.**
