participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(participants_1, participants_2, separator=","):
    participants_list_1 = participants_1.split(separator)
    participants_list_2 = participants_2.split(separator)
    common_participants = list(set(participants_list_1).intersection(participants_list_2))
    return common_participants

participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", participants)
