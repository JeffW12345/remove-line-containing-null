def solution(S):
    string = S
    string_array = string.split("\n")
    for line in string_array:
        if "NULL" in line:
            string_array.remove(line)
    new_string = "\n".join(string_array)
    return new_string


S = "id,name,age,score\n1,Jenny,NULL,14\n17,Daryll,31,11"
print(solution(S))
