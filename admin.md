# admin


## Apache

* httpd.conf typically in /etc/apache2/httpd.conf, ubuntu: /etc/apache2/apache2.conf


### CGI

[Apache Reference](http://httpd.apache.org/docs/2.2/howto/cgi.html)

* Load module, LoadModule cgi_module modules/mod_cgi.so #httpd.conf

* Add permissions to the cgi-script, always set to allow execute access (chmod +x script)

* Add ExecCGI to the <directory> options or...

* ... ScriptAlias, tells Apache that a particular directory is set aside for CGI programs

	* ScritpAlias /cgi-bin/ /usr/local/apache2/cgi-bin/ #httpd.conf

## bandwidth

* slurm -i eht0
