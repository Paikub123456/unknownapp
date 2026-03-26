# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----

### Use Case Diagram
```mermaid
flowchart LR
    %% Define Actors
    Student([Student])
    Admin([Admin])

    %% System Boundary
    subgraph System [Course Enrollment System]
        direction TB

        %% Authentication
        Login(Login / Connect)
        CreateProf(Create Student Profile)

        %% Common Use Cases
        ViewCatalog(View Course Catalog)
        ViewSched(View Schedule)
        Billing(View Billing Summary)

        %% Student Specific
        RegCourse(Register for a Course)
        DropCourse(Drop a Course)
        EditMyProf(Edit My Profile)

        %% Admin Specific
        ViewRoster(View Class Roster)
        ViewAllStudents(View All Students)
        AdminAddStudent(Add New Student)
        AdminEditStudent(Edit Student Profile)
        AdminAddCourse(Add New Course)
        AdminEditCourse(Edit Course)
    end

    %% Connect Student
    Student --> Login
    Student --> CreateProf
    Student --> ViewCatalog
    Student --> RegCourse
    Student --> DropCourse
    Student --> ViewSched
    Student --> Billing
    Student --> EditMyProf

    %% Connect Admin
    Admin --> Login
    Admin --> ViewCatalog
    Admin --> ViewRoster
    Admin --> ViewAllStudents
    Admin --> AdminAddStudent
    Admin --> AdminEditStudent
    Admin --> AdminAddCourse
    Admin --> AdminEditCourse
    Admin --> ViewSched
    Admin --> Billing
```

### Flowchart of the main workflow
```mermaid
flowchart TD
    %% Program Start
    Start([Start Application]) --> Init[Load Data / Seed Defaults]
    Init --> LoginMenu{Login Menu}
    
    %% Login Menu Branches
    LoginMenu -- "[1] Student Login" --> StudentCheck{Student ID Check}
    LoginMenu -- "[2] Admin Login" --> AdminCheck{Admin Password Check}
    LoginMenu -- "[3] Exit" --> SaveExit[Save Data and Exit]
    SaveExit --> End([End Application])

    %% Student Authentication Flow
    StudentCheck -- "Enter 'new'" --> CreateStudent[Create Student Profile]
    CreateStudent --> StudentMenu
    StudentCheck -- "Enter existing ID" --> ValidID{Is ID Valid?}
    ValidID -- "Yes" --> StudentMenu{Student Menu}
    ValidID -- "No" --> LoginMenu

    %% Admin Authentication Flow
    AdminCheck -- "Valid Password" --> AdminMenu{Admin Menu}
    AdminCheck -- "Invalid Password" --> LoginMenu

    %% ---- Student Menu Loop ----
    StudentMenu -- "[1] View Catalog" --> S1[View Course Catalog]
    StudentMenu -- "[2] Register" --> S2[Register for Course]
    StudentMenu -- "[3] Drop" --> S3[Drop Course]
    StudentMenu -- "[4] Schedule" --> S4[View My Schedule]
    StudentMenu -- "[5] Billing" --> S5[View Billing Summary]
    StudentMenu -- "[6] Profile" --> S6[Edit My Profile]
    
    %% Return to Student Menu
    S1 & S2 & S3 & S4 & S5 & S6 --> StudentMenu
    
    StudentMenu -- "[7] Logout" --> SLogout[Save Sub-Progress]
    SLogout --> LoginMenu

    %% ---- Admin Menu Loop ----
    AdminMenu -- "[1] View Catalog" --> A1[View Course Catalog]
    AdminMenu -- "[2] View Roster" --> A2[View Class Roster]
    AdminMenu -- "[3] All Students" --> A3[View All Students]
    AdminMenu -- "[4] Add Student" --> A4[Add New Student]
    AdminMenu -- "[5] Edit Student" --> A5[Edit Student Profile]
    AdminMenu -- "[6] Add Course" --> A6[Add New Course]
    AdminMenu -- "[7] Edit Course" --> A7[Edit Course]
    AdminMenu -- "[8] View Schedule" --> A8[View Student Schedule]
    AdminMenu -- "[9] Billing" --> A9[Billing Summary]
    
    %% Return to Admin Menu
    A1 & A2 & A3 & A4 & A5 & A6 & A7 & A8 & A9 --> AdminMenu
    
    AdminMenu -- "[10] Logout" --> ALogout[Save Sub-Progress]
    ALogout --> LoginMenu
```
### Prompts
I have a Java project built for Course Enrollment. Please review the codebase to understand how the business logic works. Once you understand the system, extract the logic for the register for a course use case and rewrite a standalone, functional equivalent of it in Python. You will need to bring over any relevant models and validation rules to make it work. Please save the output file inside a new folder called python in my workspace root.
