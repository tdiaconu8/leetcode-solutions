function curry(fn: Function): Function {

    let argsToProcess = [];
    return function curried(...args) {
        argsToProcess = [...argsToProcess, ...args];
        if (argsToProcess.length === fn.length) {
            return fn(...argsToProcess)
        }
        else {
            return curried;
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */