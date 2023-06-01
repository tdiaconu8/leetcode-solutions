function createCounter(n: number): () => number {
    let number = n-1;
    return function() {
        number ++;
        return number;
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */