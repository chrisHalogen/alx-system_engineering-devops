# Install Flask from pip3
# Ensure that pip3 is present
package { 'python3-pip':
  ensure => present,
}
# Use pip3 to install flask
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  require => Package['python3-pip'],
}