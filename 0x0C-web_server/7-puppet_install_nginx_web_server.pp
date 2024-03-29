# Puppet manifest to install and configure Nginx
# Requirements:
# - Nginx should be listening on port 80
# - When querying Nginx at its root / with a GET request, it must return a page that contains the string "Hello World!"
# - The redirection must be a "301 Moved Permanently"

package { 'nginx':
  ensure => installed,
}

file_line { 'server_config':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
