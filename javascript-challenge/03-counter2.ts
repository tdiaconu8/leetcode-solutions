type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {

    let num: number = init;

    function increment() {
        num++;
        return num;
    }

    function decrement() {
        num--;
        return num;
    }

    function reset() {
        num = init;
        return num;
    }

    return {
        increment: increment,
        decrement: decrement,
        reset: reset
    }


};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */