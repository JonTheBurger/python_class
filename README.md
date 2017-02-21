# What is Python?
First, let's get all of the jargon out of the way. Python is a high-level, multi-paradigm, cross-platform, 
general-purpose, duck-typed, dynamically-typed, and strongly-typed scripting language. Python is focused on being 
productive and readable, and is considered a "batteries included" language, having a powerful standard library and rich 
package ecosystem. Python is very popular in the science and engineering world because of the many free packages 
available for complex computations, computer task automation, and graphical applications. It's an excellent choice as a 
first programming language for those that want to get things done!

In this course, we will be using Python version 3. Though Python 2 is still used in many places out in the wild, it's 
becoming less prevalent with time, and all major libraries have been ported to 3. That being said, the differences are 
minimal, and it's easy to jump between the two.

# What to Install
Purists may scoff at the paltry 5 minutes we'll use to show you how to run scripts from the command line, but again,
Python is all about *getting things done*. We're going to use modern tools to make our lives easier.

### [Python 3.6.0+](https://www.python.org/downloads/)
This install contains the Python interpreter, pip package manager, and more. It's what actually allows you to run 
Python code on your system.

1. Go to the following link https://www.python.org/downloads/
2. Click on the button "Download Python 3.6.0". (if there is a Python 3.x version higher than 3.6, select that)
3. Run the installer. If you don't have admin privileges (e.g. at work), un-check "Install launcher for all users
(recommended)".
4. Check "Add Python 3.6 to PATH"
5. Click "Install Now". You may click "Customize installation" if you want to change Python's install location.
6. Open powershell (or command prompt, or if you're on another platform, terminal)
7. Type python. If you see something like the following, you installed correctly!
```bash
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Users\Jon>python
Python 3.6.0 (v3.6.0:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
	
### [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/)
This is an [open source](https://github.com/JetBrains/intellij-community/tree/master/python), free (even for commercial
use!), and feature-rich Integrated Development Environment, or IDE, for Python. Unlike IDLE, which is typically used to 
teach Python, we're going to use the latest and greatest industry proven tools in order to maximize our productivity.
(If you use other JetBrains products, consider downloading the 
[Jetbrains Toolbox App](https://www.jetbrains.com/toolbox/app/). If you aren't sure, you don't need to worry about it.)

1) Go to the following link https://www.jetbrains.com/pycharm/download/

2) Click the "Download" button located under "Community".

3) Run the installer. The default settings should be fine.

4) Run Pycharm. I recommend selecting the "darcula" theme.

5) Create a new project named "hello"

6) Click the gray square in the bottom left. You should see side-bar and bottom-bar tabs 
(e.g. 1: Project, 7: Structure on the left and 4: Run, 6: TODO, Python Console, and Terminal on the bottom)

7) In the Project tab on the left pane, right click the folder "hello", Select "new", "Python file". Name this file 
"hello.py"

8) Type the following into the editor:

```python
print('hello world!')
```

9) Right-click the editor and click "Run hello". You should see the text "hello world!" appear in the bottom "Run" tab.

10) (Optional) If you're on Windows, navigate to "File->Settings->Tools->Terminal->Application settings->Shell path"
and replace "cmd.exe" with "powershell.exe"

### [Automate the Boring Stuff with Python](http://automatetheboringstuff.com/#toc)
This isn't something to install, but a "textbook" we will loosely follow. It's available for free in its entirety 
online at http://automatetheboringstuff.com/#toc

# Running Python from the Command Line

1) Open Powershell, Command Prompt, Bash, or you other Terminal Emulator of choice.

2) Type the following line. Congrats, you have entered the Python shell. You can type Python scripts line by line here.

```bash
python
```

3) Type the following line. Neat, you've executed some real Python. You can even declare variables and classes!
But more on that later.

```bash
print('hello')
```

4) Exit by typing the following:

```bash
exit()
```

5) In your favorite text editor, create a new file called "hello.py"

6) Type the following into your "hello.py" script:

```bash
print('hello')
```

7) In your terminal, change directories to folder containing hello.py

8) Type the following:

```bash
python hello.py
```
Congratulations! You now understand how to use the Python shell and run Python scripts from the command line.

# Video Transcript Link
If you're taking this class from me, I'll provide you with a link to an unlisted playlist from my 
[Youtube channel](https://www.youtube.com/channel/UC3JTri_U0lqQDvWLkJqaa8w).

