/*
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
*/

int gcd(int a, int b)
{
    while (a != b)
    {
        if (a > b)
        {
            a -= b;
        }
        else
        {
            b -= a;
        }
    }
    return a;
}

char* gcdOfStrings(char* str1, char* str2)
{
    int str1_length = strlen(str1);
    int str2_length = strlen(str2);

    char* str1_plus_str2 = malloc(str1_length + str2_length + 1);
    char* str2_plus_str1 = malloc(str1_length + str2_length + 1);

    strcpy(str1_plus_str2, str1);
    strcat(str1_plus_str2, str2);

    strcpy(str2_plus_str1, str2);
    strcat(str2_plus_str1, str1);

    int equal = strcmp(str1_plus_str2, str2_plus_str1);

    free(str1_plus_str2);
    free(str2_plus_str1);

    if (equal != 0)
    {
        return "";
    }

    int size = gcd(str1_length, str2_length);

    // Caller responsible of freeing...
    char* gcdos = malloc(size + 1);

    strncpy(gcdos, str1, size);
    gcdos[size] = '\0';

    return gcdos;

}