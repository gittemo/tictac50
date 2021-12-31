# TicTac50
#### Video Demo: https://youtu.be/oOQ8gRd1xlU
#### Description:

Hi everyone (probably no one) reading this, my Name is Jonan Mesfin Stein and this is the readme to my final project for CS50 2021. I have created a Tic Tac Toe game as a Windows app in Python. The files that are inside my project folder are:

- readme.md
- tictac.py
- TicTac50.exe
- tictac.ico

The tictac.py file is where you can check out all the source code and also run the Program. I have also created a .exe for anyone that does not have Python on their Windows device (such as me a week ago). The tictac.ico file is just for letting the program have a nice icon.

### Code:

I will abstractly explain the code to you here. Inside the code are also a bunch of comments that explain stuff. I used TKinter for the GUI, because I wanted to use something basic. I created 4 "pages" for the GUI; 
1) A main menu that has a small description, 3 external links
  for further reading and two buttons ("Play against your
  friend" and "Play against SkyNet"
2) A settings menu that is between the main menu and the pve
  frame. Here the player can select between playing as 'X' or
  'O'
3) The pve frame. Here the Player plays against the minimax
  algorithm. The screen consists of the 9 squares and a 
  'Main Menu' and 'Reset' screen.
4) The pvp frame. This is essentially the same as the pve frame,
  but the second player is not SkyNet.

The logic of the code is basically split into 11 functions. I will not list them. They allow for the GUI to be supplied with formularized action. 
The most interesting part is my implementation of the minimax algorithm that I called 'SkyNet'. I don't think it can lose, but only draw. This is due to the nature of Tic-Tac-Toe, where two optimally playing opponents will always draw. To a noob, this algorithm will seem pretty good I think.

I really enjoyed making this project. It took me 5 days to make it. I had to learn about TKinter and minimax, the rest was rather familiar. I think it was a good level of difficulty for the time I had. I am satisfied with the level of polish the GUI has. Making minimax and seeing it play well without any hard coded logic was super fun and not that hard (with a lot of help from Youtube videos, linked below).

I think that TKinter is not very popular. It does not have good documentation or extensive community. Next time, I would probably use another tool for GUI like GTK.

What I didn't like and I think can be improved upon was the design of the code in some aspects. I wanted to implement TKinter classes to abstract away design from functionality of buttons for example. That way, there would have been less redundancy. I didn't have enough time to do this though. I also think that the main loop was not designed perfectly, but I am not big brained enough to redo it now. It certainly works though and I didn't find any bugs with my sparse testing. 
What I also missed was designing the playing pages style. I could have used the same font as with the menus and removed the onclick animation so that the squares feel less like buttons.
Now I feel sad that I didn't do it, but whatever. 

### Sources:
I will try to find the links of stuff that helped me. 
Also shoutout to the people in the CS50 Discord that I chatted with. Provided some good camaraderie


https://www.youtube.com/watch?v=SYrjAUFqPZU

https://stackoverflow.com/questions/29286943/is-there-a-way-to-block-fullscreen-mode-in-tkinter

https://www.youtube.com/watch?v=YXPyB4XeYLA

https://docs.python.org/3/library/tkinter.html#a-hello-world-program

https://www.youtube.com/watch?v=P2TcQ3h0ipQ

https://www.youtube.com/watch?v=fT3YWCKvuQE

https://www.youtube.com/watch?v=l-hh51ncgDI

https://www.youtube.com/watch?v=MKgDQjZwI2o

https://docs.python.org/3/library/random.html

https://www.codegrepper.com/code-examples/python/python+find+all+positions+of+value+in+list
