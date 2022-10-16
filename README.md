# eCommerce.git.io

Welcome to my repository of 'eCommerce'.This is purely based for laptops of screen size of 1920 x 1080.
This web is developed by using HTML,CSS,JavaScript and for backend python is used.
The database used is mariadb which is included in Xampp Server.
Steps to follow before running the index.html.
 - Download the anconda,python connector and xampp server, setup it at some location.
 - Save all these files in x:\Xampp\htdocs .Start the Apache and MySql server using the xampp control pannel.
 - Then open phpMyAdmin page or from xampp control panel click on the admin of MySql.
 - create the database of name 'ecommerce'
 - create the table of name 'subscribe'
 - create the column of name 'email'
 - Give the path of your anaconda folder in the 'subscribe.py' file
 - Add an extension of .py in "x:\Xampp\apache\conf\httpd.conf" at line no 436
 - Add 'AllowOverride All
    	Options ExecCGI
    	Order allow,deny
    	Allow from all'  as it is in the "x:\Xampp\apache\conf\httpd.conf" on line no 388 inside the directory tag
 - Save all the changes and open the index.html in any browser.

Thank for visiting my directory.
Live demo: https://abhisalunkhe.github.io/eCommerce.git.io/
