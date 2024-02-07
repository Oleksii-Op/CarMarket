# Getting Started 
## Project description 

### This project is an implementation of a simple car market database model and data interaction logic for querying data in a simple and understood manner to users (including filtering) as real car markets back-end structure do.  

#### Even though a lot car markets have a wide range of different vehicles, in my project I have decided to narrow vehicles types to:
* Tracks powered by internal combustion engines.
* Cars powered by internal combustion engines.
* Cars powered by eletrical motors or by electrical motors and internal combustion engines(Hybrids).
* Motorcycles powered by only internal combustion engines.


#### Dependencies used in this project are: 
* SQLAlchemy
* Alembic
* Psycopg2 (PostgreSQL drivers)

Note that for simplicity and uploading my database to this repository, I will use SQLite db files. But you may find commented engine to connect to your own PostgreSQL using psycopg2 drivers. 

<pre><br/>Sample:<br>engine = create_engine('postgresql+psycopg2://username:password@hostname:port/database', echo=True)
<br/>Sample with some random input:  <br/>engine = create_engine('postgresql+psycopg2://admin:QWERTY@localhost:8080/car_market', echo=True)</pre>
