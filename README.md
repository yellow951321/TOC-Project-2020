# TOC Project 2020

[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)

發送隨機一篇遊戲新聞（根據遊戲評論網站IGN）
或者是以我的觀點幫你選擇遊戲（根據遊戲類型和平台）
## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```
## Finite State Machine
![fsm](./fsm.jpg)

## Usage
### game news
1. 輸入game news後會有選項讓使用者選擇想要知道的遊戲新聞的平台
![presentation1](./img/presentation1.jpg)
2. 選擇之後則會隨機挑選一則近期的遊戲新聞網址還有簡短說明跟評分以及可遊玩的平台。
![presentation2](./img/presentation2.jpg)
### recommend
1. 輸入recommend後會有選項讓使用者選擇希望推薦的遊戲的平台
![presentation3](./img/presentation3.jpg)
2. 選擇平台後會有選項讓使用者選擇希望推薦的遊戲類型



