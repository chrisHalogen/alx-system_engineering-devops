#!/usr/bin/env bash
# using puppet to automate the changes to the configuration

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH Client Configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
}
