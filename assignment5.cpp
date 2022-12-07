Write C++ program for storing appointment schedule for day. Appointments are booked randomly using linked list. Set start and end time and min and max duration for visit slot.
Write functions for
 a) Display free slots
 b) Book appointment
 c) Cancel appointment ( check validity, time bounds, availability etc.)
 d) Sort list based on time
 e)Sort list based on time using pointer manipulation
*/


#include<iostream>

using namespace std;

int no_appointments;
struct Node_Structure {
    int start, end, min, max, flag;
    struct Node_Structure *next;
} *head;

class Appointment {
public:
    void create_schedule(), display_schedule(), book_appointment(), cancel_appointment(), sort_appointments();
} A1;

int main() {
    int ch;
    char ans;
    cout
            << "\n\n*** Menu ***\n1. Create Appointments\n2. Display Free Slots\n3. Book Appointment\n4. Cancel Appointment\n5. Sort slots based on Time";
    do {
        cout << "\nChoice: ";
        cin >> ch;

        switch (ch) {
            case 1:
                A1.create_schedule();
                break;
            case 2:
                A1.display_schedule();
                break;
            case 3:
                A1.book_appointment();
                break;
            case 4:
                A1.cancel_appointment();
                break;
            case 5:
                A1.sort_appointments();
                break;
            default:
                cout << "\n\033[1m\033[31mWrong choice!!!\033[0m";
        }
        cout << "\n\n\033[31mContinue?! (y/n) : \033[0m";
        cin >> ans;
    } while (ans == 'y' || ans == 'Y');
}


void Appointment::create_schedule() {
    int i;
    struct Node_Structure *temp, *last;

    head = nullptr;

    cout << "\n No. of Appointment Slots: ";
    cin >> no_appointments;

    for (i = 0; i < no_appointments; i++) {
        temp = new(struct Node_Structure);
        cout << "\n Appointment No.: " << i + 1 << "\n Start Time(in 24-hour format): ";
        cin >> temp->start;
        cout << " End Time(in 24-hour format): ";
        cin >> temp->end;
        cout << " Minimum Duration(in Minutes): ";
        cin >> temp->min;
        cout << " Maximum Duration(in Minutes): ";
        cin >> temp->max;
        temp->flag = 0;
        temp->next = nullptr;

        if (head == nullptr) {
            head = temp;
            last = head;
        } else {
            last->next = temp;
            last = last->next;
        }

    }
}


void Appointment::display_schedule() {
    int cnt = 1;
    struct Node_Structure *temp;

    cout << "\n\t\t\t\t****Appointment Schedule****";
    cout << "\n\tSr. No.\tStart\tEnd\t\tMin_Dur\t\tMax_Dur\t\tStatus";
    temp = head;
    while (temp != nullptr) {
        cout << "\n\t " << cnt;
        cout << "\t\t " << temp->start;
        cout << "\t\t " << temp->end;
        cout << "\t\t  " << temp->min;
        cout << "\t\t  " << temp->max;

        if (temp->flag)
            cout << "\t\t-Booked-";
        else
            cout << "\t\t--Free--";

        temp = temp->next;
        cnt++;
    }
}


void Appointment::book_appointment() {
    int start;
    struct Node_Structure *temp;

    cout << " Enter Appointment Time: ";
    cin >> start;

    temp = head;

    while (temp != nullptr) {
        if (start == temp->start) {
            if (temp->flag == 0) {
                cout << "\n Slot Booked!!!";
                temp->flag = 1;
            } else
                cout << "\n Slot Not Available!!!";
        }

        temp = temp->next;
    }

}


void Appointment::cancel_appointment() {
    int start;
    struct Node_Structure *temp;

    cout << "\n Enter Appointment Time: ";
    cin >> start;

    temp = head;

    while (temp != nullptr) {
        if (start == temp->start) {
            if (temp->flag == 1) {
                cout << "\n Slot Canceled!!!";
                temp->flag = 0;
            } else
                cout << "\n Appointment was Free!!!";
        }

        temp = temp->next;
    }
}


void Appointment::sort_appointments() {
    int i, val;
    struct Node_Structure *temp;


    for (i = 0; i < no_appointments - 1; i++) {
        temp = head;
        while (temp->next != nullptr) {
            if (temp->start > temp->next->start) {
                val = temp->start;
                temp->start = temp->next->start;
                temp->next->start = val;

                val = temp->end;
                temp->end = temp->next->end;
                temp->next->end = val;

                val = temp->min;
                temp->min = temp->next->min;
                temp->next->min = val;

                val = temp->max;
                temp->max = temp->next->max;
                temp->next->max = val;

            }
            temp = temp->next;
        }
    }

    cout << "\n\n\t Appointments Sorted!!!";

}

