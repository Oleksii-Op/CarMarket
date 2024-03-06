# Getting Started

## Car Marketplace

#### This project is an implementation of a simple car marketplace database model and data interaction logic for querying data in a simple and understood manner to users (including filtering) as real car markets back-end structure do.  

#### Even though a lot car markets have a wide range of different vehicles, in my project I have decided to narrow vehicles types to:
* Tracks powered by internal combustion engines.
* Cars powered by internal combustion engines.
* Cars powered by electrical motors or by electrical motors and internal combustion engines (Hybrids).
* Motorcycles powered by only internal combustion engines.

#### Other entities:
* Users
* Address
* Sale Record
* Advertisement
* Car categories
* Vehicle


### Technologies

- `PostgrSQL`
- `Docker`
- `SQLAlchemy`
- `Jupyter Notebook`
- `Visualization tools`
- `Testing Library`

### The process and first steps
The first step was determining all the entities of our ecosystem 
and the database and which features are required to be, based on 
business needs, for example:
- Allowing third parties to access only 
  needed data for analytical purposes and prevent them from accessing
  personal user's data(popular cars sold, number of advertisements by a region etc.), 
  thus introducing integrity to our system.


- Creation of tools or using side API's to validate a vehicle (via unique VIN number)
  to avoid fraud advertisements, if this information exists.


- Next, as there are some entities, I decided to model a database.


- Since it's easier for me to model an initial relational database using SQL (DDL), 
  rather than using SQLAlchemy, I will first create relationships in Postgres and a 
  SQLAlchemy's mapped model later. You can see database modeling below as it has a lot of text.
  

- Setting Docker compose file to quickly run postgreSQL with necessary
  environment variables (docker compose file has adminer, but I usually
  connect via pgAdmin). Or running a simple container.
<pre><br/>Docker run command:
docker run -d --name postgres_db -p 5432:5432 -e POSTGRES_PASSWORD=secret_pass -e POSTGRES_USER=postgres -e POSTGRES_DB=car_market postgres
Note that environment variables matches variables in .env file. <br> </pre>


- Tests to insure correct object's behavior .(TO BE IMPLEMENTED)

### What knowledge I obtained developing this project:
Even though this project is still under development, I have picked up important
skills and a better understanding of complex ideas, which enhanced my problem-solving
and logical thinking.

- Databases:
  - Detailed database modeling to create relationships and entities, and decomposition. This project
    gave me deep understanding of why planning is so important before coding (You may 
    check previous commits to understand what I am talking about).
  - Side API's validators,custom data validators and Pydantic validation before committing
  any data to the database.


- Using Pandas for creating fake data generators via Data Frames, parsing and converting
  data from JSON to CSV in Jupiter Notebook.


- Containerization:
  - Practice how to quickly set up a database and access/manage it using pgAdmin or
    psql to enter the shell of a container.

- SQLAlchemy:
  - Declarative way of defining model using mappers instead of old methods.

- Keeping records of documentation of my classes, function etc. 
  to understand (after some time) what a class/func does. 
  And it is very important so that other developers can understand the code.

## Database modeling: 
Let's break this part into :
* ### Domain representation problem:
  * Definition of the subject area:
    * This database is about representing a car marketplace storing data of vehicles and users selling them.
  * Identification of actors:
    * Buyers, sellers(regular user or a dealer), administrators
  * Identification of objects and subjects:
    * Objects: Vehicles ads, Users, Sales records
    * Main subjects: Users, Administrators
  * Formation of Use Cases:
    * A user registers in the system
    * A user creates an ad
    * A user changes his personal data
    * A user changes his ad's information (price off, drop price, additional information)
  * Defining connections between actors and objects:
    * Users can interact with database to store their ads, viewing different ads 
      allowing sorting by some attributes as: sorting by car maker, price, color etc.
    * Administrators have rights to modify/delete existing ads or users to avoid fake
    and fraud ads.
    * Some subjects may have access to sales records to analyse which vehicles 
    are the best-selling for a certain period of time and other statistic needs.
* ### Logical modeling:
  * Detailing the conceptual database model and defining data types:
    * User's attributes:
      * Unique id - integer auto-incrementing as Primary Key
      * Unique username - varchar(40) not null
      * Unique email address - varchar(255) not null
      * User property/type - char(1)
      * First name - varchar(20) optional
      * Last name - varchar(20) optional
      * Main phone number - varchar(20) not null
      * Additional phone number - varchar(20) optional
      * Gender - varchar(7) optional
      * Registered date - datetime UTC for database use
      * Updated info date - datetime UTC for database use 
    * Address attributes:
      * Unique id - integer auto-incrementing as Primary Key
      * User id - integer as Foreign Key
      * Address hash - varchar(255)
      * Address - varchar(255) Optional
      * City - varchar(30) not null
      * State - varchar(50) Optional
      * Zip code - integer not null
      * Country - varchar(50) not null
    * Vehicles attributes:
      * Vehicle id - integer as Primary Key
      * Maker - varchar(20)
      * Model - varchar(20)
      * Category id - integer as Foreign Key
    * Categories attributes:
      * Category id - integer as Primary Key
      * Category name - varchar(50)
      * Description - text
    * Sales records attributes:
      * Record id - integer as Primary Key
      * User's id (seller) - integer as Foreign Key
      * User's id (buyer) - integer as Foreign Key
      * Advertisement id - integer as Foreign Key
      * Date at which the deal took place - datetime UTC
    * Advertisements attributes:
      * Advertisement id - integer as Primary Key
      * User id - integer as Foreign Key
      * Vehicle id - integer as Foreign Key
      * Unique properties related to a car like:
        * Price, color, vin number, fuel etc.
      * Ad created at - datetime
      * Ad updated at - datetime
  * Keys definition:
    * Described above
  * Logical constraints definition:
    * User's constraints: 
      * Username - unique
      * Email address - unique
      * Phone numbers - unique
    * Address constraints:
      * User id - unique (one-to-one)
    * Vehicles constraints:
      * Category id - unique (one-to-one)
    * Categories constraints:
      * None
    * Sales records constraints:
      * Advertisement id - unique
    * Advertisements constraints:
      * Price - more than 0 (positive)
      * Vin number - unique(But this is for now, since the same car can be sold again)
      * mileage - more than 0 (positive)
      * Engine volume - more than 0 (positive)
      * Average consumption - more than 0 (positive)
    * Relationships:
      * Only one user can have a unique address table (One-to-one).
      * One category can have multiple vehicles, but every car
        belongs to a specific category (One-to-many).
      * One user can have multiple advertisements, but one advertisement
        can have one specific user(seller) (One-to-many).
      * Buyer and seller are foreign keys in a sale record, but the buyer
        and a seller came from the same table thus creating a composite
        foreign key relationship.
      * Every sale record is linked to a vehicle, but this vehicle
        can be sold multiple times (Many-to-many).
  * Normalization of relations:
    * Now in each table's columns:
      * We have no duplicates
      * All attributes are of simple data types without massive as would be with placing all user's phone numbers in one column thus storing a massive.
      * All values are scalar.
      * There are primary keys.
      * And as I did some part of normalization before the remaining problems are:
         * Table Sales Records has uniqueness based on a composite key, so I decided
          to create record_id as a primary key to represent sales records table.(FIXED)
         * Inspect and test composite relationship from SQLAlchemy side, not SQL.
         

* ### Physical data model:
  * Chosen database system: PostgreSQL 16
  * Agreed naming convention: I'm the one who wrote this, so this is obvious ;)
  * Definition of data types related to Postgres:
    * To be in a .sql file to reduce extra text here, as it will duplicate
      the logical model above.
  * Define indexes and their attributes so as not to lose performance.
    It is not always possible to determine all indices in advance.
    It takes time to experiment with the data. Problems may arise as 
    the system operates. (TO BE IMPLEMENTED).
  * Define Views (TO BE IMPLEMENTED).
  * Define security constrains (TO BE IMPLEMENTED).
  

  
