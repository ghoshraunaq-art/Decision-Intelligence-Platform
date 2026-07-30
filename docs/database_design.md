***# Database Design***



***## Overview***



***The Decision Intelligence Platform uses a normalized PostgreSQL relational database designed for retail sales analytics.***



***The database stores customer information, product details, transactions, sales records and inventory data while maintaining relationships through foreign keys.***



***---***



***# Main Tables***



***## Customers***



***Stores customer information.***



***Attributes:***



***- customer\_id***

***- customer\_name***

***- email***

***- gender***

***- age***

***- region\_id***





***## Products***



***Stores product information.***



***Attributes:***



***- product\_id***

***- product\_name***

***- brand\_id***

***- category\_id***

***- cost\_price***

***- selling\_price***





***## Orders***



***Stores customer transactions.***



***Attributes:***



***- order\_id***

***- customer\_id***

***- order\_date***

***- payment\_method***





***## Order Items***



***Stores products included in orders.***



***Attributes:***



***- order\_item\_id***

***- order\_id***

***- product\_id***

***- quantity***





***## Sales***



***Stores sales transaction details.***



***Attributes:***



***- sale\_id***

***- order\_item\_id***

***- sale\_date***

***- quantity\_sold***

***- selling\_price***





***## Inventory***



***Tracks product stock availability.***



***Attributes:***



***- inventory\_id***

***- product\_id***

***- stock\_quantity***

***- purchase\_price***

***- last\_restock\_date***





***## Categories***



***Stores product categories.***



***## Brands***



***Stores product brand information.***



***## Regions and Countries***



***Used for geographical analysis and filtering.***



***---***



***# Database Relationships***



Countries

|

Regions

|

Customers

|

Orders

|

Order Items

|

Products

|

Categories / Brands



Products

|

Inventory



Order Items

|

Sales



***---***



***# Design Principles***



***The database follows:***



***- Relational database design***

***- Normalization principles***

***- Foreign key relationships***

***- Data consistency rules***



***This structure enables efficient business analytics and dashboard generation.***

