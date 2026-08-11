#include <iostream>
#include <string>
using namespace std;

class Student
{
private:
    int rollNo;
    string name;
    float cgpa;

public:
    // Function to accept student details
    void input()
    {
        cout << "Enter Roll No: ";
        cin >> rollNo;

        cin.ignore();
        cout << "Enter Name: ";
        getline(cin, name);

        cout << "Enter CGPA: ";
        cin >> cgpa;
    }

    // Function to display student details
    void display()
    {
        cout << "Roll No : " << rollNo << endl;
        cout << "Name    : " << name << endl;
        cout << "CGPA    : " << cgpa << endl;
    }

    // Getter for Roll Number
    int getRollNo()
    {
        return rollNo;
    }
};

int main()
{
    int n, choice, pos, roll;

    cout << "Enter number of students: ";
    cin >> n;

    Student s[100];

    cout << "\nEnter details of students:\n";
    for (int i = 0; i < n; i++)
    {
        cout << "\nStudent " << i + 1 << endl;
        s[i].input();
    }

    do
    {
        cout << "\n===== Student Information System =====\n";
        cout << "1. Insert Student at Given Position\n";
        cout << "2. Delete Student by Roll Number\n";
        cout << "3. Search Student by Roll Number\n";
        cout << "4. Display All Students\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter position (1 to " << n + 1 << "): ";
            cin >> pos;

            if (pos < 1 || pos > n + 1)
            {
                cout << "Invalid Position!\n";
            }
            else
            {
                for (int i = n; i >= pos; i--)
                {
                    s[i] = s[i - 1];
                }

                cout << "Enter details of new student:\n";
                s[pos - 1].input();
                n++;

                cout << "Student inserted successfully.\n";
            }
            break;

        case 2:
        {
            cout << "Enter Roll Number to delete: ";
            cin >> roll;

            int found = 0;

            for (int i = 0; i < n; i++)
            {
                if (s[i].getRollNo() == roll)
                {
                    found = 1;

                    for (int j = i; j < n - 1; j++)
                    {
                        s[j] = s[j + 1];
                    }

                    n--;
                    cout << "Student deleted successfully.\n";
                    break;
                }
            }

            if (!found)
                cout << "Student not found.\n";

            break;
        }

        case 3:
        {
            cout << "Enter Roll Number to search: ";
            cin >> roll;

            int found = 0;

            for (int i = 0; i < n; i++)
            {
                if (s[i].getRollNo() == roll)
                {
                    cout << "\nStudent Found:\n";
                    s[i].display();
                    found = 1;
                    break;
                }
            }

            if (!found)
                cout << "Student not found.\n";

            break;
        }

        case 4:
            if (n == 0)
            {
                cout << "No students available.\n";
            }
            else
            {
                cout << "\nStudent Records:\n";
                for (int i = 0; i < n; i++)
                {
                    cout << "\nStudent " << i + 1 << endl;
                    s[i].display();
                }
            }
            break;

        case 5:
            cout << "Exiting Program...\n";
            break;

        default:
            cout << "Invalid Choice!\n";
        }

    } while (choice != 5);

    return 0;
}


