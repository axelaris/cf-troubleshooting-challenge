# Cloud Foundry Troubleshooting Challenge
## Lab instructions

Welcome to Cloud Foundry troubleshooting challenge!
During this lab, you will try to resolve deployment issues and make applications running.

### How to start the Lab:

- Make sure you have CF CLI installed. For that, type `cf` in Terminal window. If command is not found - go ahead and install it:

	```
	$ sudo zypper install cf-cli
	```

- Login to CF with provided credentials:

	```
	$ cf login -a api.cf.mydeploy.xyz
	```

- Make sure your assigned Org is `challenge` and Space is equal to your username:

	```
	$ cf target
	api endpoint:   https://api.cf.mydeploy.xyz
	api version:    2.125.0
	user:           dev01
	org:            challenge
	space:          dev01

	```
		
- Clone this repository, and run preparation script:

	```
	$ git clone https://github.com/axelaris/cf-troubleshooting-challenge.git
	
	$ cd cf-troubleshooting-challenge
	
	$ ./prepare.sh 
	Preparing Lab environment... Done

	```
	
- You will see 3 directories for **Easy**, **Moderate** and **Tricky** levels of tasks accordingly. We suggest you to start from Easy level, then move forward to more difficult tasks.
- To run a task, just `cd` into it’s directory, then try to push application. If it does not work - try to find out why.

	```
	$ cd easy/01
	
	$ cf push
	```

Good luck!
