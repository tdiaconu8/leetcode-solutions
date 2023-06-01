function chunk(arr: any[], size: number): any[][] {

    let iterator = 0;
    let res = [];
    let batch = [];

    while (iterator < arr.length) {
        if (batch.length === size) {
            res.push(batch);
            batch = [arr[iterator]];
        }
        else {
            batch.push(arr[iterator])
        }
        iterator++;
    } 
    if (batch.length) {
        res.push(batch)
    }
    return res;

};