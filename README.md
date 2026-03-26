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

### Flowchart of the main workflow

### Prompts
