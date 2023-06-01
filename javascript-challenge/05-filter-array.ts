function filter(arr: number[], fn: (n: number, i: number) => any): number[] {

    let res: number[] = [];

    for (let i = 0; i < arr.length; i++) {
        const num = arr[i];
        if (fn(num, i)) {
            res.push(num)
        }
    }
    return res;

};