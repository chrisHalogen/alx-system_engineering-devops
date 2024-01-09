#!/usr/bin/env bash
# Using Puppet to automate the process

file { '/etc/ssh/ssh_config':
	ensure  => present,
content => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
