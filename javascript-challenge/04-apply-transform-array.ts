function map(arr: number[], fn: (n: number, i: number) => number): number[] {

    arr.forEach( function callback(v, i) {
        arr[i] = fn(v,i);
    });
    return arr;

};