def main(s):
    s = s[6:-7]
    s = (s.replace('store', '')
         .replace('array', '')
         .replace('(', '')
         .replace(')', '')
         .replace('\n', ' '))
    s = s.split('.')
    for i in range(len(s)):
        s[i] = s[i].split(':=')
    s = s[:-1]
    ans = dict()
    for i in range(len(s)):
        ans[s[i][0].replace(' ', '')] = s[i][1].split()
    return ans
