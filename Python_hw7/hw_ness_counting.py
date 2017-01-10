#сколько в тексте разных существительных с суффиксом -ness и какое существительное из них имеет максимальную частотность.
#open_read_lower_clean_count


def open_file():
    f = open("Austen Jane. Pride and Prejudice.txt", 'r', encoding = "utf-8")
    text = f.read()
    f.close()
    return text


def clean(st):
    arr = st.split()
    for idx, word in enumerate(arr):
        arr[idx] = word.strip('\'"/.,<>:;[]{}\\|1234567890`~!@#$%^&*()_+-=?!«»…—')
        arr[idx] = arr[idx].lower()
    return arr


def find_ness(arr):
    new_arr = []
    how_many = []
    for word in arr:
        if word.endswith("ness") == True:
            if word in new_arr:
                for idx, each in enumerate(new_arr):
                    if each == word:
                        how_many[idx] += 1
            else:
                new_arr.append(word)
                how_many.append(1)
    st = ""
    for word in new_arr:
        st += word
        st += " "
    return st, new_arr, how_many


def find_max(arr, freq_arr):
    t = 0
    for number in freq_arr:
        if number > t:
            t = number
    st = ''
    for idx, each in enumerate(arr):
        if freq_arr[idx] == t:
            st += each
            st += " "
    return st
        

def main():
    text = open_file()
    arr = clean(text)
    
    st1, new_arr, how_many = find_ness(arr)
    st2 = find_max(new_arr, how_many)
    print(st1)
    print(st2)
    

main()
