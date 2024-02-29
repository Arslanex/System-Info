# System Check

This project was initially created to control a CUDA/CUDA compatible OpenCV installation and to perform simple GPU tests. Later, various additions were made to learn the system information of programming cards such as Jetson Nano etc. For this reason program consists of two main parts. The first part is the module that provides information about the system and the second part is the module that tests CUDA, GPU and FPS. After running the program, you can simply select the modules from the terminal. The commands that the program can perform are as follows :


```
Main Menu
├── System Check  (Modul 1)
│   ├── Basic Info
│   ├── CPU Info
│   ├── GPU('s) Info
│   ├── RAM Info
│   ├── Memory Info
│   ├── Disk Info
│   └── Network Info
│
└── CUDA and FPS Tests  (Modul 2)
    ├── Is OpenCV CUDA Enabled
    ├── CPU vs GPU 
    └── FPS Tests
```
## Where to Use \ Why to Use

The main goal of this project is to check GPU compatible OpenCV setup and perform FPS tests. In this way, you can learn the performance of your device, which allows you to estimate the performance you can get from the models and networks you will use. Apart from these, you can also easily observe the hardware information of your device. this feature has been added to the program to be used mostly on raspberry Pi and Jetson family cards.  In summary, you can use this program to learn the hardware information, library installations and performance of programming cards that will run GPU-oriented computer vision.

## Setup

1. Clone this repostiory : `git clone https://github.com/Arslanex/System-Check`
2. Instal requirements : `pip install -r requirements.txt`
3. OpenCV installation 
    1. As default library : `pip install opencv-python`
    2. As GPU Enabled Installition
        1. [Windows](https://drive.google.com/file/d/1XcZ0L99fTqlRhOl56nbNvEnUkm3lfq2F/view?usp=sharing (Türkçe))
        2. [Linux](https://qengineering.eu/install-opencv-4.5-on-jetson-nano.html (for nano))
5. Run main.py script
    1. On Windows :  `python main.py`
    2. On Linux :   `python3 main.py`

<br>

> **Warning** <br>
> If you install GPU compatible OpenCV, you will not be able to use the second module, i.e. CUDA and FPS testing features

<br>

## Screenshots and Videos

<p align="center">
  <img src="" width="320" />
  <img src="" width="320" /> 
  <img src="" width="320" />
</p>

<p align="center">

[video](https://user-images.githubusercontent.com/44752389/176975865-dc074448-f08e-4c77-ab44-6b553e49de4e.mp4)

</p>

***
<h3 align="center"> Enes ARSLAN </h3>
<p align="center">
<a href="https://www.instagram.com/_enes.arslan_/?next=%2F">
<img src="https://img.shields.io/badge/Instagram-000000?style=for-the-badge&logo=instagram&logoColor=white"/>
<a href="https://www.linkedin.com/in/enes-arslan-/">
<img src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=white"/>
<a href="https://github.com/Arslanex">
<img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white"/ >
</p>
