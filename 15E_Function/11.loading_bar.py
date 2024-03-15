def check_progress(bar):           #bar_current_value by the end of function it will be changed
    if bar == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{bar}% [{'%' * (bar // 10)}{'.' * (10 - bar // 10)}] \n Still loading..."

given_bar = int(input())
print(check_progress(given_bar))