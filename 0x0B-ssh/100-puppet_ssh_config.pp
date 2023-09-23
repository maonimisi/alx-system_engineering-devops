# Make changes to config file using puppet fuction declarations

file_line { 'PasswordAuthentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}

file_line { 'IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	IdentityFile ~/.ssh/school',
}
