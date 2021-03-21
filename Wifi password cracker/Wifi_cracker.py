print("To crack a wifi password using this program you should be at least connected to that wifi connection once. Or else this wont work.")
print("Working on windows only, I will make one work on mac in a bit.")
Wifi = input("Enter a wifi connection you want to crack: ")
code = f"color a\ncls\nnetsh wlan show profile {Wifi} key=clear\npause"
cmd_file = open("Wifi_pass.cmd", "w")
cmd_file.write(code)
cmd_file.close()
