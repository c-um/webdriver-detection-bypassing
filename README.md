# webdriver-detection-bypassing
Bypass website anti-bot/webdriver detection (Python 3.7)



## Usage

Python 3.7 (or higher) is required for this to work.

```
pip3 install pyppeeteer
python3 bypass.py
```



## How

If you just visit [this website](https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html) with headless chrome, you will be detected. This page shows the principles that most pages are using to detect your webdriver.



Here I refer [this](https://github.com/intoli/intoli-article-materials/tree/4bec59bd3f936d729340fefadb5b4f144bc70658/articles/not-possible-to-block-chrome-headless) and modify it to Python version.



If you wish to bypass this webdriver detection, simply use what is shown in `bypass.py`. By doing this, you can use a webdriver to visit nearly every single page there is.


