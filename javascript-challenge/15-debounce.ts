type F = (...p: any[]) => any

function debounce(fn: F, t: number): F {
    let timeoutID;
    return function(...args) {
        timeoutID ? clearTimeout(timeoutID) : null;
        timeoutID = setTimeout( () => {
            return fn(...args);
        },
        t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */