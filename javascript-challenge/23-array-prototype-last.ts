declare global {
    interface Array<T> {
        last(): T | -1;
    }
}

Array.prototype.last = function() {
    let n = this.length;
    return n > 0 ? this[n-1] : -1
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */

export {};