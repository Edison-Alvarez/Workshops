# Workshop 3 

This workshop focuses on developing a backend system to provide a vehicles catalog using Python and design patterns.

## Requirements

The workshop requirements are outlined as follows:

- Vehicles such as Cars, Yachts, Trucks, and Motorcycles should have specific attributes.
- Additional vehicle options like Helicopter and Scooter need to be implemented with appropriate attributes.
- Predefined engines should be assigned to each vehicle type, categorized into gas and electric engines with low and high variants.
- Memory optimization is crucial, necessitating careful consideration of object creation and memory references.
- A technical report with a Class Diagram illustrating the solution's architecture and technical decisions is required.
- Search functionality by price range should be implemented.

## Business Rules

- Vehicles are categorized into two types of chassis: A or B.
- Gas consumption is calculated based on engine information and chassis type.

### User Stories

- Admins should be able to manage engines and vehicles for an updated catalog.
- Users should be able to view and filter the vehicle catalog.
- Admins should calculate gas consumption for trucks accurately.
- Admins should create high-end and low-end engines to offer vehicles of different price ranges.
- Users and admins should have account management functionalities.
- Admins should track all catalog actions and searches, monitor system resources.

### Entities

- Vehicles
- Catalog
- Engines
- Gamma (Classification)
- User
- Admin


## Technical Decisions

### Complications

During the implementation of Proxy and Facade patterns together, a design issue arose regarding their interaction. Initially, the Proxy was intended to act as an intermediary between the main interface (later established as Facade) and the catalog service. However, upon implementing the Facade for both systems, it became evident that a design flaw existed.

To resolve this, a superior interface, SystemAccess, was introduced. This interface serves as the initial point of connection for clients, with the Proxy acting as an intermediary between it and the main service, FacadeVehicleShop.

### Proxy Pattern Implementation

The Proxy pattern was chosen to address requirements such as authentication, change logging, search system, and resource monitoring. By serving as an intermediary, the Proxy ensures secure and centralized access control, enhancing security and management flexibility. It also facilitates detailed record-keeping of changes and searches without impacting user experience and optimizes performance by serving as a cache memory for frequently accessed data.

### Facade Pattern Implementation

The Facade pattern reduces system coupling and simplifies the user interface by encapsulating the internal complexity of subsystems. It divides the system into engine and catalog subsystems, providing a simplified interface for user interaction. This not only reduces perceived complexity for users but also enhances code organization.

