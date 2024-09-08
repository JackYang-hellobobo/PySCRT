# $language = "python"
# $interface = "1.0"

# This script demonstrates how to open a text file and read it line by
# line to a server.


def main():
	crt.Screen.Synchronous = True
	# Note: A IOError exception will be generated if 'input.txt' doesn't exist.
	#
	for line in open("c:\\temp\\input.txt", "r"):
		# Send the line with an appended CR
		#
		crt.Screen.Send(line + '\r')
	 
		# Wait for my prompt before sending the next line
		#
		crt.Screen.WaitForString("prompt$")

	crt.Screen.Synchronous = False

	
main()

# $language = "Python"
# $interface = "1.0"

# Connect to a telnet server and automate the initial login sequence.
# Note that synchronous mode is enabled to prevent server output from
# potentially being missed.

def main():

	crt.Screen.Synchronous = True

	# connect to host on port 23 (the default telnet port)
	#
	crt.Session.Connect("/TELNET login.myhost.com 23")

	crt.Screen.WaitForString("ogin:")
	crt.Screen.Send("myusername\r")

	crt.Screen.WaitForString("assword:")
	crt.Screen.Send("mypassword\r")

	crt.Screen.Synchronous = False


main()

