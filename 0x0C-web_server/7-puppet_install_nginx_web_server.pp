# Puppet manifest to install and configure Nginx
# Requirements:
# - Nginx should be listening on port 80
# - When querying Nginx at its root / with a GET request, it must return a page that contains the string "Hello World!"
# - The redirection must be a "301 Moved Permanently"

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

# Define the Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('my_module/nginx.conf.erb'), # Use an ERB template for Nginx configuration
  notify  => Service['nginx'], # Reload Nginx when the configuration changes
}

# Create the root page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Define the redirection for /redirect_me
nginx::resource::location { 'redirect_me':
  ensure       => present,
  location     => '/redirect_me',
  rewrite_rule => '^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require      => Package['nginx'],
  notify       => Service['nginx'], # Reload Nginx when the configuration changes
}
