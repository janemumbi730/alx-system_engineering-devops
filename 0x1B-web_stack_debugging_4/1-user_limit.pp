# holberton user and open a file without any error message.
# This manuscript enables the user holberton to login and open files without error

# Increase hard file limit for user holberton
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
