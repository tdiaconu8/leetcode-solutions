type F = (...args: any[]) => void

function throttle(fn: F, t: number): F {
    let intervalID  = null;
    let lastArgs = null;

    function helper() {
        if (lastArgs === null) {
            clearInterval(intervalID);
            intervalID  = null;
        }
        else {
            fn(...lastArgs);
            lastArgs = null;
        }
    }

    return function (...args) {
        if (intervalID) {
            lastArgs = args;
        }
        else {
            fn(...args);
            intervalID  = setInterval(helper, t)
        }
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */