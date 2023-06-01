type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {

    let res = [];

    function helper(curr, depth) {
        for (const item of curr) {
            if (typeof item === "object" && depth < n) {
                helper(item, depth+1);
            }
            else {
                res.push(item);
            }
        }
    }

    helper(arr, 0);
    return res;
};