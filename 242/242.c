//Runtime: 4 ms
bool isAnagram(char* s, char* t) {
    int a = strlen(s);
    int b = strlen(t);
    if (a != b){
        return false;
    }
    int counter[26] = {0};
    for (int i = 0; i < a ; i++) {
        counter[(int) s[i] - 97]++;
        counter[(int) t[i] - 97]--;
    }
    for (int i = 0; i < 26; i++) {
        if (counter[i] != 0) {
            return false;
        }
    }
    return true;
}
