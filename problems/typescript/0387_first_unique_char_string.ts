function firstUniqChar(s: string): number {

    // T: O(n), S: O(n)

    let counter = {};

    for (let char of s) {
        counter[char] = counter[char] ? counter[char] + 1 : 1;
    }

    for (let i=0; i< s.length; i++) {
        if (counter[s[i]] === 1) {
            return i;
        }
    }
    return -1;

};