# Getting Started 
## Project description 

### This project is an implementation of a simple car market database model and data interaction logic for querying data in a simple and understood manner to users (including filtering) as real car markets back-end structure do.  

#### Even though a lot car markets have a wide range of different vehicles, in my project I have decided to narrow vehicles types to:
* Tracks powered by internal combustion engines.
* Cars powered by internal combustion engines.
* Cars powered by electrical motors or by electrical motors and internal combustion engines(Hybrids).
* Motorcycles powered by only internal combustion engines.

## Database modeling: 
Let's break this part into :
* ### Domain representation problem:
  * Definition of the subject area:
    * This database is about representing a simple car market storing data of vehicles and users selling them.
  * Identification of actors:
    * Buyers, sellers, administrators
  * Identification of objects and subjects:
    * Objects: Vehicles ads, Users, Sales records
    * Main subjects: Users, Administrators
  * Formation of Use Cases:
    * A user registers in the system
    * A user creates an ad
    * A user changes his personal data
    * A user changes his ad's information (price off, drop price, additional information)
  * Defining connections between actors and objects:
    * Users can interact with database to store their ads, viewing different ads allowing sorting by some attributes as: sorting by car maker, price, color etc.
    * Administrators have rights to modify/delete existing ads or users to avoid fake and fraud ads.
    * Some subjects may have access to sales records to analyse which vehicles are the best-selling for a certain period of time and other statistic needs.
* ### Logical modeling:
  * Detailing the conceptual database model and defining data types:
    * User's attributes:
      * Unique id - integer auto-incrementing as Primary Key
      * Unique address id - integer as Foreign Key
      * Unique username - varchar(40) not null
      * Unique email address - varchar(255) not null
      * First name - varchar(20) optional
      * Last name - varchar(20) optional
      * Main phone number - varchar(20) not null
      * Additional phone number - varchar(20) optional
      * Gender - varchar(7) optional
      * Registered date - datetime UTC for database use
      * Updated info date - datetime UTC for database use UTC
    * Address attributes:
      * Unique id - integer auto-incrementing as Primary Key
      * Address - varchar(255) Optional
      * City - varchar(30) not null
      * State - varchar(50) Optional
      * Zip code - integer not null
      * Country - varchar(50) not null
    * Vehicles:
      * As it has a lot of attributes I will skip this table. All we need to know is that it has: id, vin number, maker, model etc.
    * Sales records:
      * Unique user's id (seller) - integer as a part of composite key
      * Unique user's id (buyer) - integer as a part of composite key
      * Vehicle's ad id - integer
      * Date at which the deal took place - datetime UTC
      * Price - integer
      * Maker - varchar(20)
      * Model - varchar(40)
      * Vin number - varchar(40)
      * Year build - datetime
  * Keys definition:
    * 
  * Description of logical constraints:
    * Attributes that have to be unique:
      * User's table : email address, phone numbers, username, id, address id
      * Address table : id
      * Vehicles : id, vin number
    * Attributes that have to be more than 0:
      * Vehicles : price, mileage
    * Relationships:
      * Only a user may have many ads, not an ad may have many user (One-to-many)
      * A user may have only one address (One-to-one)
  * Normalization of relations:
    * Now in each table's columns:
      * We have no duplicates
      * All attributes are of simple data types without massive as would be with placing all user's phone numbers in one column thus storing a massive.
      * All values are scalar (except some vehicles properties which are necessary to describe a car or a motorcycle)
      * There are primary keys.
      * And as I did some part of normalization before the remaining problems are:
        * Not all attributes describe the entire primary key in sales records.
        * We have dependencies of some non key's attributes on other's (all attributes should depend on a primary key)  
          Table Sales Records has uniqueness based on a composite key, so I decided to create record_id as a primary key to represent sales records table.
          And since a buyer may not be registered in the system but somehow the buyer obtained a seller's contact and a deal took place, 
          Sales Records table will have the unique seller's id and the buyer's id will be optional and the seller will have
          a column of deals.
          And the sold vehicle's attributes in a sale record will be accessed via vehicle's id.

* ### Physical data model:
  * Chosen database system: PostgreSQL 16
  * Agreed naming convention: I'm the one who wrote this, so this is obvious :)
  * Definition of data types related to Postgres:
    * 

#### Dependencies used in this project are: 
* SQLAlchemy
* Alembic
* Psycopg2 (PostgreSQL drivers)

Note that for simplicity and uploading my database to this repository, I will use SQLite db files. But you may find commented engine to connect to your own PostgreSQL using psycopg2 drivers. 

<pre><br/>Sample:<br>engine = create_engine('postgresql+psycopg2://username:password@hostname:port/database', echo=True)
<br/>Sample with some random input:  <br/>engine = create_engine('postgresql+psycopg2://admin:QWERTY@localhost:8080/car_market', echo=True)</pre>

User property - business or regular