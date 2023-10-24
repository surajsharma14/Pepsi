import time
import threading

class Alarm:
    def __init__(self, time_str, action=None):
        self.time_str = time_str
        self.action = action
        self.is_triggered = False

    def trigger(self):
        self.is_triggered = True
        if self.action:
            self.action()

def set_alarm(alarm_list, time_str, action=None):
    alarm = Alarm(time_str, action)
    alarm_list.append(alarm)
    print(f'Alarm set for {time_str}')

def snooze_alarm(alarm):
    alarm.is_triggered = False
    print('Alarm snoozed')

def check_alarms(alarms):
    while True:
        current_time = time.strftime("%H:%M")
        for alarm in alarms:
            if not alarm.is_triggered and alarm.time_str == current_time:
                print(f'Alarm at {alarm.time_str} is going off!')
                alarm.trigger()
        time.sleep(60)  # Check alarms every minute

def main():
    alarms = []
    alarm_checker = threading.Thread(target=check_alarms, args=(alarms,))
    alarm_checker.daemon = True
    alarm_checker.start()

    while True:
        print("Options:")
        print("1. Set an alarm")
        print("2. Snooze an alarm")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            time_str = input("Enter the alarm time (HH:MM): ")
            set_alarm(alarms, time_str)
        elif choice == '2':
            print("Snooze an alarm:")
            for i, alarm in enumerate(alarms):
                if not alarm.is_triggered:
                    print(f"{i + 1}. {alarm.time_str}")
            alarm_idx = int(input("Enter the alarm number to snooze: ")) - 1
            if 0 <= alarm_idx < len(alarms) and not alarms[alarm_idx].is_triggered:
                snooze_alarm(alarms[alarm_idx])
            else:
                print("Invalid alarm selection.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()
