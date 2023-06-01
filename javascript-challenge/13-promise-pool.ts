type F = () => Promise<any>;

function promisePool(functions: F[], n: number): Promise<any> {

    return new Promise( (resolve) => {
        let pending = 0;    // Number of promises pending
        let i = 0;  // Index of the last function iterated

        function pooler() {
            if (i === functions.length && pending === 0) {
                resolve(0);
            }
            while (i < functions.length && pending < n) {
                const promise = functions[i]()
                i++;
                pending++;
                promise.then(
                    () => {
                        pending--;
                        pooler();
                    }
                );

            }
        }

        pooler();
        return;

    });

};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */